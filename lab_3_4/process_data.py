import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from field import field
from unique import Unique


@print_result
def f1(arg):
    return sorted(Unique(field(arg, "job-name"), ignore_case=True))


@print_result
def f2(arg):
    return filter(lambda x: x.startswith("программист"), arg)


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [
        f"{profession}, зарплата {salary} руб."
        for profession, salary in zip(arg, salaries)
    ]


if __name__ == "__main__":
    path = "lab_3_4/data_light.json"

    with open(path) as f:
        data = json.load(f)

    with cm_timer_1():
        f4(f3(f2(f1(data))))
