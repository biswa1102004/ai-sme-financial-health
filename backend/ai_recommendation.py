def generate_recommendations(risk_level):
    if risk_level == "High Risk":
        return [
            "Reduce operational expenses",
            "Improve receivables collection"
        ]
    elif risk_level == "Medium Risk":
        return [
            "Optimize working capital",
            "Negotiate supplier payments"
        ]
    else:
        return [
            "Eligible for working capital loan",
            "Consider business expansion"
        ]

