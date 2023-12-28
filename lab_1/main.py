from src.biquadratic_solver import BiquadraticSolver
from src.input_handler import InputHandler


class BiquadraticEquationApp:
    def run(self) -> None:
        input_handler = InputHandler()
        solver = BiquadraticSolver()

        try:
            a, b, c = input_handler.get_coefficients()
            result = solver.solve(a, b, c)
            if len(result) == 0:
                print("There are no real valued solutions.")
            else:
                print(f"The solutions are: {result}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    app = BiquadraticEquationApp()
    app.run()
