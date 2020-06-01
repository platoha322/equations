import math


def linear_equation(a: float, b: float):
  """
  Solves linear equation a*x + b = 0
  """
  # special cases
  if a == 0:
    if b == 0:
      return "All real numbers"
    else:
      return "No solution"
  else:
  # general method
    x = - b / a
    return x


def quadr_equation(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return ("No solutions")
    disroot = math.sqrt(discriminant)
    if a == 0:
        solution = linear_equation(b, c)
        return solution
    else:
        if discriminant > 0:
            x1 = (-b + disroot) / (2 * a)
            x2 = (-b - disroot) / (2 * a)
            return x1, x2
        elif discriminant == 0:
            x = -b / 2 * a
            return x


coefx2 = 1
coefx = 0
const = 3
solutions = quadr_equation(coefx2, coefx, const)
print(solutions)

