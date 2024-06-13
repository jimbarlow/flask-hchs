from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://harthumane.org")

if __name__ == "__main__":
  app.run()


