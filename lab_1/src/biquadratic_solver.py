from math import sqrt
from typing import Set


class BiquadraticSolver:
    def solve(self, a: float, b: float, c: float) -> Set[float]:
        D = b**2 - 4 * a * c

        roots = set()

        if a == 0:
            raise Exception("Equation must be biquadratic (a != 0).")

        if D >= 0:
            quadratic_roots = [
                (-b - sqrt(D)) / (2 * a),
                (-b + sqrt(D)) / (2 * a),
            ]

            for root in quadratic_roots:
                if root >= 0:
                    roots.add(sqrt(root))
                    roots.add(-sqrt(root))
        return roots
