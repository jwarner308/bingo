import random
import sys

from mpi4py import MPI

from .Archipelago import Archipelago

class ParallelArchipelago(Archipelago):

    def __init__(self, island):
        self.comm = MPI.COMM_WORLD
        self.comm_rank = self.comm.Get_rank()
        self.comm_size = self.comm.Get_size()
        super().__init__(island, self.comm_size)
        self._best_indv = None
        self._converged = False

    def step_through_generations(self, num_steps, non_block=True,
                                 when_to_update=10):
        if non_block:
            self._non_blocking_execution(num_steps, when_to_update)

            self.comm.Barrier()

            if self.comm_rank == 0:
                status = MPI.Status()
                while self.comm.iprobe(source=MPI.ANY_SOURCE,
                                       tag=2,
                                       status=status):

                    self.comm.recv(source=status.Get_source(), tag=2)
        else:
            for _ in range(num_steps):
                self._island.execute_generational_step()

        self.archipelago_age += num_steps

    def coordinate_migration_between_islands(self):
        """Shuffles island populations for migration and performs
        migration by swapping pairs of individuals between islands
        """
        if self.comm_rank == 0:
            island_partners = self._shuffle_island_indices()
        else:
            island_partners = None

        island_partners = self.comm.bcast(island_partners, root=0)
        island_index = island_partners.index(self.comm_rank)

        self._partner_exchange_program(island_index, island_partners)

    def test_for_convergence(self, error_tol):
        """Tests that the fitness of individuals is less than
        or equal to the specified error tolerance

        Parameters
        ----------
        error_tol : int
            Upper bound for acceptable fitness of an individual

        Returns
        -------
        bool :
            Indicates whether a chromosome has converged.
        """
        best_indvs = self._island.best_individual()
        self._best_inv = best_indvs
        best_indvs = self.comm.gather(best_indvs, root=0)

        list_of_best_indvs = []
        converged = None
        if self.comm.rank == 0:
            for indv in best_indvs:
                list_of_best_indvs.append(indv)
            list_of_best_indvs.sort(key=lambda x: x.fitness)
            best_indv = list_of_best_indvs[0]
            converged = best_indv.fitness <= error_tol
            self._best_indv = best_indv
            self._converged = converged

        converged = self.comm.bcast(converged, root=0)
        self._converged = converged

        return converged


    def get_best_individual(self):
        """Returns the best individual if the islands converged to an
        acceptable fitness.

        Returns
        -------
        Chromosome :
            The best individual whose fitness was within the error
            tolerance.
        """
        if MPI.COMM_WORLD.Get_rank() == 0:
            return self._best_indv
        else:
            return None

    def _shuffle_island_indices(self):
        indices = list(range(self._num_islands))
        random.shuffle(indices)
        return indices

    def _partner_exchange_program(self, island_index, island_partners):
        primary_partner = (island_index % 2 == 0)
        if primary_partner:
            if island_index + 1 >= self.comm_size:
                my_partner = None
            else:
                my_partner = island_partners[island_index + 1]

                partner_island = self.comm.recv(source=my_partner, tag=4)

                indexes_to_send, partners_indexs_to_send = \
                    Archipelago.assign_send_receive(self._island, partner_island)

                self.comm.send(partners_indexs_to_send, dest=my_partner, tag=4)

        else:
            my_partner = island_partners[island_index - 1]
            self.comm.send(self._island, dest=my_partner, tag=4)

            indexes_to_send = self.comm.recv(source=my_partner, tag=4)

        if my_partner is not None:
            indexes_to_partner = set(indexes_to_send)
            indvs_to_send = [self._island.population[indv] \
                            for indv in indexes_to_partner]
            traded_individuals = self.comm.sendrecv(indvs_to_send,
                                                    my_partner,
                                                    sendtag=4,
                                                    source=my_partner,
                                                    recvtag=4)
            new_population = [indv for i, indv, \
                             in enumerate(self._island.population) \
                             if i not in indexes_to_partner] \
                             + traded_individuals
            self._island.load_population(new_population)


    def _non_blocking_execution(self, num_steps, when_to_update=10):
        total_age = {}
        average_age = self.archipelago_age
        target_age = self.archipelago_age + num_steps

        while average_age < target_age:
            if self._island.generational_age % when_to_update == 0:
                if self.comm_rank == 0:
                    total_age.update({0: self._island.generational_age})
                    status = MPI.Status()
                    while self.comm.iprobe(source=MPI.ANY_SOURCE,
                                           tag=2,
                                           status=status):
                        data = self.comm.recv(source=status.Get_source(),
                                              tag=2)
                        total_age.update(data)
                    average_age = (sum(total_age.values())) / self.comm.size
                    # if average_age >= num_steps:
                    #     self.comm.bcast(average_age, root=0)
                        #average_age = self.comm.bcast(average_age, root=0)

                        
                    # send average to all other ranks if time to stop
                    #self.comm.bcast(average_age, root=0)
                # for every other rank, store rank:age, and send it off to 0
                else:
                    data = {self.comm_rank : self._island.generational_age}
                    req = self.comm.isend(data, dest=0, tag=2)
                    req.Wait()
            # if there is a message from 0 to stop, update averageAge
            average_age = self.comm.bcast(average_age, root=0)
            # print("rank ", self.comm_rank, " average age before bcast: ", average_age)
            # sys.stdout.flush()
            #average_age = self.comm.bcast(average_age, root=0)
            print("rank ", self.comm_rank, " average age after bcast: ", average_age)
            sys.stdout.flush()
            self._island.execute_generational_step()

