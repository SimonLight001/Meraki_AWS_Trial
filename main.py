from flask import Flask, escape, request
app = Flask(__name__)

access_token = "MTc0YTFjYjgtNGM4MC00ZjFmLWJhY2QtZjUxZjIwZTEzMmE4ODljNTMyNDAtM2Qz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
bot_ID = "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2E5ZGE5ZDkwLWZjMTgtNDBiMC1iNWI3LWZmYTdlZjMxNzBmNw"

@app.route('/')
def hello():
    return "Hello World!"
