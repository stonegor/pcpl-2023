import sys
from typing import Tuple


class InputHandler:
    def get_float_from_terminal(self) -> float:
        valid_input = False
        while not valid_input:
            inp = input()
            try:
                result = float(inp)
                valid_input = True
            except Exception as e:
                print(f"Invalid input. {e}. Please try again: ")
        return result

    def get_coefficients(self) -> Tuple[float, float, float]:
        if len(sys.argv) < 3:
            print("Input coefficients:")

            a = self.get_float_from_terminal()
            b = self.get_float_from_terminal()
            c = self.get_float_from_terminal()
        else:
            try:
                args = sys.argv[1:]
                a = float(args[0])
                b = float(args[1])
                c = float(args[2])
            except Exception as e:
                raise e
        return a, b, c
