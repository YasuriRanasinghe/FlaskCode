def ask_for_expense_recommendations(expenses):
    prompt = """
    You are a helpful assistant.
    You are given the following expenses:
    """
    for expense in expenses:
        prompt += f"\n- {expense[0]}: {expense[1]} rs"
    
    prompt += """
    You need to generate a query to find recommendations to decrease your expenses.
    """
    return prompt

def ask_for_income_recommendations(income_details):
    prompt = """
    You are a helpful assistant.
    You are given the following income details:
    """
    for income in income_details:
         prompt += f"\n- {income[0]}: {income[1]} rs"
    
    prompt += """
    You need to generate a query to find recommendations to increase your income.
    """
    return prompt

def ask_for_investment_recommendations(investment_details):
    prompt = """
    You are a helpful assistant.
    You are given the following investment details:
    """
    for investment, amount in investment_details.items():
        prompt += f"\n- {investment}: {amount} rs"
    
    prompt += """
    You need to generate a query to find recommendations to optimize your investments.
    """
    return prompt


def ask_for_savings_recommendations(savings_details):
    prompt = """
    You are a helpful assistant.
    You are given the following savings details:
    """
    for savings_account, balance in savings_details.items():
        prompt += f"\n- {savings_account}: {balance} rs"
    
    prompt += """
    You need to generate a query to find recommendations to optimize your savings.
    """
    return prompt