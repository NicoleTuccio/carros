from flask import Flask, request
from flask_cors import CORS
import db_carros
import traceback

app = Flask(__name__)

CORS(app)

@app.route("/carros", methods=["GET"])
def get_all():
    try:
        dados = db_carros.recupera_carros() #transformar de tuplas em json
        resposta = []
        for registro in dados:
            carro = {}
            carro["id"] = registro[0]
            carro["ano"] = registro[1]
            carro["montadora"] = registro[2]
            carro["modelo"] = registro[3]
            carro["placa"] = registro[4]
            resposta.append(carro)
            
        return resposta, 200
    except Exception as erro:
        traceback.print_exc()
        return{"msg": "erro na recuperação"}, 404

@app.route("/carros", methods=["POST"])
def insere_carro():
    try:
        dado = request.json
        db_carros.insert_carro(dado)
        return dado, 200
    except Exception as erro:
        traceback.print_exc()
        info = {"msg":"Erro de sistema"}
        return info, 406

app.run(debug=True)
