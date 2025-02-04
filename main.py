from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://harthumane.org/putts-for-paws")
    # return render_template('home.html')

if __name__ == "__main__":
  app.run()


