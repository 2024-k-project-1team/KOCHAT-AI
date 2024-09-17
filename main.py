import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Flask 애플리케이션 초기화
app = Flask(__name__)
client = OpenAI(api_key=api_key)

# system_prompt 파일 읽기
with open("system_prompt.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get("question")
    print(f"user_question : {user_question}")

    if not user_question:
        return jsonify({"error": "질문을 입력해 주세요."}), 400

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
    )

    answer = completion.choices[0].message.content
    print(f"answer: {answer}")
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
