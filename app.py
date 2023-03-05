from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <html>
            <body>
                <h1>Download HTML file</h1>
                <form method="post" action="/download">
                    <label for="filename">Enter filename:</label>
                    <input type="text" id="filename" name="filename"><br><br>
                    <input type="submit" value="Download">
                </form>
            </body>
        </html>
    """

@app.route("/download", methods=["POST"])
def download():
    filename = request.form["filename"]
    html_path = os.getenv("HTML_PATH") # Read the path to the HTML file from an environment variable
    file_path = os.path.join(html_path, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run()