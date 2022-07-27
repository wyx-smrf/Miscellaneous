from gurobipy import *


# Optimization model
opt_mod = Model(name = 'linear program')

# Decision variables
x = opt_mod.addVar(name = 'x', 
                   vtype = GRB.CONTINUOUS, lb = 0)
y = opt_mod.addVar(name = 'y', 
                   vtype = GRB.CONTINUOUS, lb = 0)

# Objective function
obj_fn = 5*x + 4*y
opt_mod.setObjective(obj_fn, GRB.MINIMIZE)


# Constraints
c1 = opt_mod.addConstr(  x +   y >=  8, name='c1')
c1 = opt_mod.addConstr(2*x +   y >= 10, name='c2')
c1 = opt_mod.addConstr(  x + 4*y >= 11, name='c3')


# Solve the model
opt_mod.optimize() # solve the model
opt_mod.write("linear_model.lp") # output the LP file of the model


# Output the results
print('Objective Function value: %f' % opt_mod.objVal)
# Get values of the decision variables
for v in opt_mod.getVars():
    print('%s: %g' % (v.varName, v.x))