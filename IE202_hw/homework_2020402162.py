from pulp import *
import pandas as pd

#Code for Question 1, Ezgi Etkin 2020402162
Plants = ["P1","P2","P3","P4"]

supply = {"P1": 290,
          "P2": 220,
          "P3": 180,
          "P4": 280}

Customers = ["C1", "C2", "C3", "C4", "C5"]

demand = {"C1": 180,
          "C2": 200,
          "C3": 160,
          "C4": 140,
          "C5": 250}


#For Question 1 Part A, "Unit costs by rail" tableau used to get costs
costs = [[8.5,7,8,6.5,9],
        [7.5,8,7,10,8.5],
        [11,6,6.5,8,7],
        [9,7,12,6,7.5]]
costs = makeDict((Plants, Customers),costs)

prob = LpProblem("Distribution_Problem",LpMinimize)

Routes = [(p,c) for p in Plants for c in Customers]

route_vars = LpVariable.dicts("Route",(Plants,Customers), cat='Integer', lowBound=0)

prob += lpSum([route_vars[p][c]*costs[p][c] for (p,c) in Routes])

#Forming supply and demand constraints just like in the example
for p in Plants: 
    prob += lpSum([route_vars[p][c] for c in Customers]) <= supply[p], "Sum of Products out of Plant %s"%p

for c in Customers:
    prob += lpSum([route_vars[p][c] for p in Plants]) >= demand[c], "Sum of Products into Customers %s"%c

prob.writeLP

prob.solve()
print("Status:", LpStatus[prob.status])

print("Total Optimal Cost = ", pulp.value(prob.objective))

for v in prob.variables():
    print(v.name, "=", v.varValue)

for name, c in list(prob.constraints.items()):
    print(name, ":", c, "\t", c.pi, "\t\t", c.slack)

o = [{'name':name, 'shadow price':c.pi, 'slack': c.slack}
for name, c in prob.constraints.items()]
print(pd.DataFrame(o))


#Part B, "Unit cost by ship" + 1/20*"Investment Cost" values, unit cost by rail when ship isn't available
costs = [[7.5,9,8,5.5,8],
        [6,6.5,8,7.5,8],
        [11,6,7,7,9.5],
        [10,7.5,10,7,7.5]]

costs = makeDict((Plants, Customers),costs)

prob = LpProblem("Distribution_Problem",LpMinimize)

Routes = [(p,c) for p in Plants for c in Customers]

route_vars = LpVariable.dicts("Route",(Plants,Customers), cat='Integer', lowBound=0)

prob += lpSum([route_vars[p][c]*costs[p][c] for (p,c) in Routes])

for p in Plants:
    prob += lpSum([route_vars[p][c] for c in Customers]) <= supply[p], "Sum of Products out of Plant %s"%p

for c in Customers:
    prob += lpSum([route_vars[p][c] for p in Plants]) >= demand[c], "Sum of Products into Customers %s"%c

prob.writeLP

prob.solve()
print("Status:", LpStatus[prob.status])

print("Total Optimal Cost = ", pulp.value(prob.objective))

for v in prob.variables():
    print(v.name, "=", v.varValue)

for name, c in list(prob.constraints.items()):
    print(name, ":", c, "\t", c.pi, "\t\t", c.slack)

o = [{'name':name, 'shadow price':c.pi, 'slack': c.slack}
for name, c in prob.constraints.items()]
print(pd.DataFrame(o))


#Part C, Minimum value for each cost from the first two cost lists
costs = [[7.5,7,8,5.5,8],
        [6,6.5,7,7.5,8],
        [11,6,6.5,7,7],
        [9,7,10,6,7.5]]

costs = makeDict((Plants, Customers),costs)

prob = LpProblem("Distribution_Problem",LpMinimize)

Routes = [(p,c) for p in Plants for c in Customers]

route_vars = LpVariable.dicts("Route",(Plants,Customers), cat='Integer', lowBound=0)

prob += lpSum([route_vars[p][c]*costs[p][c] for (p,c) in Routes])

for p in Plants: 
    prob += lpSum([route_vars[p][c] for c in Customers]) <= supply[p], "Sum of Products out of Plant %s"%p

for c in Customers: 
    prob += lpSum([route_vars[p][c] for p in Plants]) >= demand[c], "Sum of Products into Customers %s"%c

prob.writeLP

prob.solve()
print("Status:", LpStatus[prob.status])

print("Total Optimal Cost = ", pulp.value(prob.objective))

for v in prob.variables():
    print(v.name, "=", v.varValue)

for name, c in list(prob.constraints.items()):
    print(name, ":", c, "\t", c.pi, "\t\t", c.slack)

o = [{'name':name, 'shadow price':c.pi, 'slack': c.slack}
for name, c in prob.constraints.items()]
print(pd.DataFrame(o))