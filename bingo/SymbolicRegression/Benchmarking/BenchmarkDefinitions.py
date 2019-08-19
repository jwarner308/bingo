"""
Definitions of Benchmarks that can be used a `BenchmarkingSuite`

Benchmarks are created in this module by defining a function with a name
starting with 'bench_` that takes no input parameters and returns a `Benchmark`

Each benchmark includes its source from the literature, but most of this
collection was taken from the ones suggested by McDermott et al. (2012)
"""
# pylint: disable=missing-docstring
import numpy as np
from .Benchmark import AnalyticBenchmark


def bench_koza_1():
    name = "Koza-1"
    description = "The polynomial x^4 + x^3 + x^2 + x"
    source = "J.R. Koza. Genetic Programming: On the Programming of " + \
             "Computers by Means of Natural Selection. MIT Press 1992"
    x_dim = 1

    def eval_func(x):
        return x**4 + x**3 + x**2 + x

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_koza_2():
    name = "Koza-2"
    description = "The polynomial x^5 - 2x^3 + x"
    source = "J.R. Koza. Genetic Programming: On the Programming of " + \
             "Computers by Means of Natural Selection. MIT Press 1992"
    x_dim = 1

    def eval_func(x):
        return x**5 - 2*x**3 + x

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_koza_3():
    name = "Koza-3"
    description = "The polynomial x^6 - 2x^4 + x^2"
    source = "J.R. Koza. Genetic Programming: On the Programming of " + \
             "Computers by Means of Natural Selection. MIT Press 1992"
    x_dim = 1

    def eval_func(x):
        return x**6 - 2*x**4 + x**2

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_1():
    name = "Nguyen-1"
    description = "The polynomial x^3 + x^2 + x"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return x**3 + x**2 + x

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_3():
    name = "Nguyen-3"
    description = "The polynomial x^5 + x^4 + x^3 + x^2 + x"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return x**5 + x**4 + x**3 + x**2 + x

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_4():
    name = "Nguyen-4"
    description = "The polynomial x^6 + x^5 + x^4 + x^3 + x^2 + x"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return x**6 + x**5 + x**4 + x**3 + x**2 + x

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_5():
    name = "Nguyen-5"
    description = "sin(x^2)cos(x) - 1"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return np.sin(x**2) * np.cos(x) - 1

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 1}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_6():
    name = "Nguyen-6"
    description = "sin(x) + sin(x + x^2)"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return np.sin(x) + np.sin(x + x**2)

    train_dist = ("U", -1, 1, 20)
    test_dist = ("U", -1, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_7():
    name = "Nguyen-7"
    description = "ln(x + 1) + ln(x^2 + 1)"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return np.log(x + 1) + np.log(x**2 + 1)

    train_dist = ("U", 0, 2, 20)
    test_dist = ("U", 0, 2, 20)
    extra_info = {"const_dim": 1}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_8():
    name = "Nguyen-8"
    description = "sqrt(x)"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 1

    def eval_func(x):
        return np.sqrt(x)

    train_dist = ("U", 0, 4, 20)
    test_dist = ("U", 0, 4, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_9():
    name = "Nguyen-9"
    description = "sin(x_0) + sin(x_1**2)"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 2

    def eval_func(x):
        return (np.sin(x[:, 0]) + np.sin(x[:, 1]**2)).reshape((-1, 1))

    train_dist = ("U", 0, 1, 20)
    test_dist = ("U", 0, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)


def bench_nguyen_10():
    name = "Nguyen-10"
    description = "2sin(x_0)cos(x_1)"
    source = "Q.U. Nguyen, et al. Symantically-Based Crossover in Genetic " + \
             "Programming: Application to Real-valued Symbolic Regression." + \
             "GPEM 2011"
    x_dim = 2

    def eval_func(x):
        return (2 * np.sin(x[:, 0]) * np.cos(x[:, 1])).reshape((-1, 1))

    train_dist = ("U", 0, 1, 20)
    test_dist = ("U", 0, 1, 20)
    extra_info = {"const_dim": 0}
    return AnalyticBenchmark(name, description, source, x_dim, eval_func,
                             train_dist, test_dist, extra_info)
