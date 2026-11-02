def derivative():
    h = 0.001  
    f = lambda x: x**2  # Example function f(x) = x^2

    for x in [1.0, 3.0, 5.0]:  # Example points to evaluate the derivative
        derivative_value = (f(x + h) - f(x)) / h  # Numerical derivative using finite difference
        analytical_derivative = 2 * x  # The analytical derivative of f(x) = x^2 is f'(x) = 2x
        print(f"At x = {x}, numerical derivative = {derivative_value}, analytical derivative = {analytical_derivative}")
        difference = abs(derivative_value - analytical_derivative)
        print(f"Difference = {difference}\n")
derivative()