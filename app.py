from dotenv import load_dotenv
import os
from openai import OpenAI
from utils import ask_for_expense_recommendations , ask_for_income_recommendations, ask_for_investment_recommendations , ask_for_savings_recommendations
from flask import Flask, request, jsonify

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv('OPEN_API_KEY')

client = OpenAI(
    api_key = API_KEY
)


def chat_with_gpt(user_input= "hi Good Evening"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    content = response.choices[0].message.content
    print(response)
    return str(content)


def get_prompt_template():
    return """
    TEST Prompt.
    """

# -------------- ENDPOINTS 
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test-response')
def response():
    res = chat_with_gpt()
    return res


@app.route('/expense-rec' ,methods=['POST'])
def expense_recommendations():
    if 'type' not in request.form:
        return jsonify({"error": "No data"}), 400
    
    expenses = [('Rent', 2000), ('Food', 500), ('Groceries', 1000)]
    #expenses =  request.form['type']
    prompt = ask_for_expense_recommendations(expenses)
    #print("-------> this is the prompt -->", prompt)
    response = chat_with_gpt(prompt)
    return response


@app.route('/income-rec' ,methods=['POST'])
def income_recommendations():
    if 'type' not in request.form:
        return jsonify({"error": "No data"}), 400
    
    incomes = [('salary', 2000), ('part-time', 500)]
    #incomes =  request.form['type']
    prompt = ask_for_income_recommendations(incomes)
    response = chat_with_gpt(prompt)
    return response

@app.route('/investment-rec' ,methods=['POST'])
def investment_recommendations():
    if 'type' not in request.form:
        return jsonify({"error": "No data"}), 400
    
    investment_types = [('stocks', 500), ('bonds', 1000)]
    #investment_types =  request.form['type']
    prompt = ask_for_investment_recommendations(investment_types)
    response = chat_with_gpt(prompt)
    return response

@app.route('/savings-rec' ,methods=['POST'])
def savings_recommendations():
    if 'type' not in request.form:
        return jsonify({"error": "No data"}), 400
    
    saving_types = [('high-yield savings account', 2000), ('certificate of deposit', 5000)]
    #saving_types =  request.form['type']
    prompt = ask_for_savings_recommendations(saving_types)
    response = chat_with_gpt(prompt)
    return response


if __name__ == '__main__':
    app.run(debug=True)
