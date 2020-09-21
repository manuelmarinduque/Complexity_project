from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

prob = LpProblem('Example', LpMaximize)
x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')
x3 = LpVariable('x3', lowBound=0, cat='Integer')
x4 = LpVariable('x4', lowBound=0, cat='Integer')
x5 = LpVariable('x5', lowBound=0, cat='Integer')
x6 = LpVariable('x6', lowBound=0, cat='Integer')
x7 = LpVariable('x7', lowBound=0, cat='Integer')
prob += 2*x1 + 5*x2 + 1*x3 + 4*x4 + 3*x5 + 6*x6 + 7*x7
prob += x1 + x2 + 2*x3 + 2*x4 + x5 + x6 + x7 <= 1000
prob += 2*x1 + 4*x2 + 1*x3 + 1*x4 + 1*x5 + 3*x6 + 2*x7 <= 2000
prob += 5*x1 + 4*x2 + 4*x3 + 1.5*x4 + 5*x5 + 3.5*x6 + 4.5*x7 <= 3500
prob += 4*x2 + 2*x5 + 3*x7 >= 1000
print(LpStatus[prob.status])
prob.solve()
print(value(x1))
print(value(x2))
print(value(x3))
print(value(x4))
print(value(x5))
print(value(x6))
print(value(x7))
print(value(prob.objective))