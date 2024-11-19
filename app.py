import requests
from flask import Flask, render_template, url_for
from flask import request as req #flask own request function is used here.


#encapsulation
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.methods == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = req.form["data"]

        minL = 20#int(input) #minimum length
        # maxL = 70#int(input) #maximum length
        maxL = int(req.form["maxL"])


        def query(payload): #run query on background
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        
        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]

        return render_template("index.html",result= output["summary_text"])
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug= True
    app.run()

