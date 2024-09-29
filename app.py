from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = "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"

def get_completion(prompt):
    # Replace this URL with the actual Perplexity API endpoint
    url = "https://api.perplexity.ai/v1/query"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "query": prompt,
        # Add any additional parameters that Perplexity might require here
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get("answer", "Sorry, I couldn't find an answer.")
    else:
        return "Error: Unable to connect to the API."

@app.route("/")
def home():    
    return render_template("index.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    return response

if __name__ == "__main__":
    app.run()
