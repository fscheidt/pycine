from flask import Flask, jsonify
from datetime import datetime
import requests
import json

# git clone https://github.com/fscheidt/pycine
# fastApi
app = Flask(__name__)

@app.route("/")
def hello():
    agora = datetime.now()
    return f"<h1>Seja bem vindo <br>- {agora}</h1>"

@app.route("/frase", methods=['GET'])
def frase():
    url = "https://zenquotes.io/api/today"    
    data = requests.get(url)
    frase = data.json()[0]
    return jsonify(
        {"frase": frase['q']}
    )

@app.route("/filmes")
def filmes(id):
    # todo: Implementar o filtro de busca por id:
    # localhost:5000/filmes/1000
        
    data = json.load(open('filmes.json'))
    return data


@app.route("/hora")
def hora():
    data = {
        "hora": datetime.now(),
        "pais": "pt-br"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
