from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
  return "Olá, estou na aplicação setada"

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0') # Descomentar quando em PRODUÇÂO
    app.run(debug=True) # Descomentar quando em DESENVOLVIMENTO