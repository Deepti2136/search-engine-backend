from flask import Flask, render_template, request
from search import search_engine

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = {}
    message = None
    searched = False   # track if user searched

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        searched = True   # user clicked search

        if query:
            results = search_engine(query)

        # File upload
        file = request.files.get("file")
        image = request.files.get("image")

        if file and file.filename != "":
            message = "File uploaded: " + file.filename

        if image and image.filename != "":
            message = "Image uploaded: " + image.filename

    return render_template(
        "index.html",
        results=results,
        message=message,
        searched=searched
    )

if __name__ == "__main__":
    app.run(debug=True)