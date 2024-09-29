from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = "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"  

def get_completion(prompt):
    url = "https://api.perplexity.ai/chat/completions"
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {"role": "system", "content": "Respond to greeting simply and precisely."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": "84",  
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        return response_json['choices'][0]['message']['content']
    else:
        return "Error: API loading failed."

@app.route("/")
@app.route("/home")
def home():    
    return render_template("home.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    return response

@app.route("/chat")
def chat():    
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
