import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.begin = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        duration = self.end - self.begin
        print(duration)


@contextmanager
def cm_timer_2():
    begin = time.time()
    yield
    duration = time.time() - begin
    print(duration)


if __name__ == "__main__":
    with cm_timer_1():  # time: 5.500544786453247
        time.sleep(5.5)

    with cm_timer_2():  # time: 5.500115156173706
        time.sleep(5.5)
