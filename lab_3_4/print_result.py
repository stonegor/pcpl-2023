from typing import Callable, Iterable


def print_result(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, dict):
            for key in result:
                print(f"{key} = {result[key]}")
        elif isinstance(result, Iterable) and not isinstance(result, str):
            for item in result:
                print(item)
        else:
            print(result)

        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return "iu5"


@print_result
def test_3():
    return {"a": 1, "b": 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == "__main__":
    print("!!!!!!!!")
    test_1()
    test_2()
    test_3()
    test_4()
