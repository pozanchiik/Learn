from sympy import symbols, ln
x = symbols('x')
function = x ** 2 * ln(x ** 2 + 5 * x)
diff_function = function.diff(x)
print(diff_function)
print(diff_function.subs(x, 2.5).evalf())