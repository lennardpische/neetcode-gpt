class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for  i  in range(iterations):
            # Objective function: f(x) = x^2
            func = x**2
            # Derivative:         f'(x) = 2x
            der = 2*x
            # Update rule:        x = x - learning_rate * f'(x)
            x = x - learning_rate * der 
            # Round final answer to 5 decimal places
        return round(x,5)    
        pass
