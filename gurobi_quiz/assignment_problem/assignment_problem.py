from gurobipy import *

def modelling():
    m = Model("Assignment_Problem_Model")
    # === Modify codes below using above variable m ===

    # ================================================
    m.optimize()
    return m

def minimized_cost():
    minimized_cost = 0
    return minimized_cost

if __name__ == "__main__":
    model_object = modelling()
    for v in model_object.getVars():
        print(v.varName, v.x)

    print('Obj:', model_object.objVal)
    print(model_object.objVal/2)