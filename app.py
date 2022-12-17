import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key ="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"
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text_from_user_1 = request.form["value"]
        text_from_user_2 = request.form["value1"]
        text_from_user_3 = request.form["value2"]
        text_from_user_4 = request.form["value3"]
        apppend_text="how to cook "+text_from_user_1+"with"+text_from_user_2+text_from_user_3+"on"+text_from_user_4
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=apppend_text,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )

        generated_text = completions.choices[0].text
        return redirect(url_for("index", result=generated_text))
    result = request.args.get("result")
    return render_template("index.html", result=result)
@app.route('/about', methods=("GET", "POST"))
def about():
    if request.method == "POST":
        text_from_user_1 = request.form["value"]
        text_from_user_2 = request.form["value1"]
        text_from_user_3 = request.form["value2"]
        text_from_user_4 = request.form["value3"]
        text_from_user_5 = request.form["flexRadioDefault"]
        apppend_text=text_from_user_5
        if apppend_text=="begingger":
            return render_template("about.html")
        elif apppend_text=="intermidate":
            return render_template("inter.html")
        elif apppend_text=="advance":
            return render_template("advance.html")
            # return render_template("about.html")
    return render_template("about.html")
if __name__=="__main__":
    app.run()
