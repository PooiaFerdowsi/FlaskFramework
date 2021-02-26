from flask import ( 
  Flask , render_template )

app = Flask("__main__") # also can ve Flask(__name__)

@app.route('/')
def index():
  return render_template("index.htm")
