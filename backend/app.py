from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

REALIBOT_PROMPT = """
You are RealiBot, an expert real-estate assistant. You help first-time home-buyers and investors understand:
- Current median home prices and rent yields by U.S. state or metro
- Basic profit/loss and ROI calculations given purchase price, rent, expenses
- Key concepts: financing, taxes, legal, market-trend factors
- General Q&A on “what to expect,” “how to start,” “risks,” etc.

When you don’t know a precise figure, say “I don’t have live data for that exact location, but here’s how you can check…” and point them to public APIs (e.g. Zillow, Redfin) or county assessor sites. Be concise (2–4 sentences per answer), use bullet points for steps, and ALWAYS ask a clarifying follow-up if you need more info (e.g. “Which state are you targeting?”).
"""

@app.route('/')
def home():
    return "RealiBot backend is running!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "No input message provided"}), 400

        response = openai.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o"),
            messages=[
                {"role": "system", "content": REALIBOT_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)