import pandas as pd

def analyze_financials(file_path):
    df = pd.read_csv(file_path)

    total_revenue = df['revenue'].sum()
    total_expense = df['expense'].sum()
    cash_flow = total_revenue - total_expense

    return {
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "cash_flow": cash_flow
    }

