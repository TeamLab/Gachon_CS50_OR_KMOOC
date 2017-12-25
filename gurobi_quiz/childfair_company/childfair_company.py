from gurobipy import *

def modelling():
    m = Model("childfair_company_model")
    # === Modify codes below using above variable m ===

    # ================================================

    m.update()
    m.optimize()

    return m

if __name__ == "__main__":
    model_object = modelling()
    for v in model_object.getVars():
        print(v.varName, v.x)

    print('Obj:', model_object.objVal)