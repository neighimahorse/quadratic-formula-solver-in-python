#Quadratic Formula Solver
# (-b +- sqrt(b^2 - 4ac)) / 2a
def QuadraticFormulaXSolver(a, b, c):
    squareroot = (b ** 2.0 - 4.*(a*c))**(1/2)
    resultPositive = (-b + squareroot)/(2*a)
    resultNegative = (-b - squareroot)/(2*a)
    return resultPositive, resultNegative

if __name__ == "__main__":
    #test, should output 5 and -3
   print(QuadraticFormulaXSolver(2,-4,-30))