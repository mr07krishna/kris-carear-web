from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
  return "Hello, kris!"
print(__name__ )
if __name__ == '__main__':
  print("im in side the now")
  app.run(host='0.0.0.0', debug=True)