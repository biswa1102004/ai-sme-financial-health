def calculate_risk(cash_flow):
    if cash_flow > 100000:
        return 80, "Low Risk"
    elif cash_flow > 0:
        return 60, "Medium Risk"
    else:
        return 30, "High Risk"

