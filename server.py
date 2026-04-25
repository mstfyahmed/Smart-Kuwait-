from flask import Flask, request, jsonify
from flask_cors import CORS
import g4f

app = Flask(__name__)
CORS(app)

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    question = data.get('question', '')
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "حل المسألة التالية لطلاب الهندسة بأرقام فقط: " + question}],
        )
        return jsonify({"result": response})
    except:
        return jsonify({"result": "السيرفر مشغول، حاول ثانية."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
