from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import groq
from groq import Groq


def groq_llm(text):
    client = Groq(
        # This is the default and can be omitted
        api_key = "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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "YWelcome! I am your Personal AI Healthcare Chatbot"
            },
            {
                "role": "user",
                "content": text,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the web page

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    # Dummy chatbot logic (Replace this with your AI or rule-based logic)
    if "headache" in user_message.lower():
        response = "Please stay hydrated and rest. If the pain persists, consult a doctor."
    elif "fever" in user_message.lower():
        response = "Monitor your temperature and rest. Take prescribed medications."
    else:
        response = groq_llm(user_message)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
