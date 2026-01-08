from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/tools/text-utility", methods=["GET", "POST"])
def text_utility():
    result = None

    if request.method == "POST":
        text = request.form.get("text", "")

        cleaned_text = " ".join(text.split())
        word_count = len(cleaned_text.split())
        char_count = len(cleaned_text)

        result = {
            "word_count": word_count,
            "char_count": char_count,
            "cleaned_text": cleaned_text
        }

    return render_template("text_tool.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

