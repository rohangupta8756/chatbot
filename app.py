import openai
from flask import Flask, request, jsonify, render_template
import config

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = config.OPENAI_API_KEY

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['input']
    prompt = f"The user says: {user_input}\nThe chatbot responds:"
    response_text = generate_response(prompt)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
