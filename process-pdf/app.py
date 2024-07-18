from flask import Flask
from flask_cors import CORS
from langchain_community.llms import Ollama

app = Flask(__name__)
CORS(app)

folder_path = "db"

llm = Ollama(model="llama3")

@app.route("/ai", methods=["POST"])
def aiPost(query, context):
    try:
        response = llm.invoke(query + context)  # Assuming llm.invoke can take a context parameter
        print(response)
        answer = {response}
    except Exception as e:  # Generic error handling, consider specifying exceptions
        print(f"Error invoking model: {e}")
        return {"error": "Failed to process query"}, 500
    return answer

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)