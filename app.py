from flask import Flask, jsonify
from flask_cors import CORS

from connector.database import databaseConnector
from transformJson.cliente import clienteJson, clientePlataformasJson, clienteEstrategiasJson, clienteCampanhasJson

app = Flask(__name__)
CORS(app)

#dados do cliente (os que podem ser mostrados)
@app.route('/cliente/1', methods=['GET'])
def get_cliente():
    pathDataBase= '../banco-de-dados/AgencIA.db'
    query = "SELECT * FROM user"
    cliente = databaseConnector(pathDataBase, query)
    return jsonify(clienteJson(cliente))

#plataformas
@app.route('/cliente/1/plataformas', methods=['GET'])
def get_cliente_plataformas():
    pathDataBase= '../banco-de-dados/AgencIA.db'
    query = "SELECT * FROM plataforma"
    plataformas = databaseConnector(pathDataBase, query)
    return jsonify(clientePlataformasJson(plataformas))

#estrategias
@app.route('/cliente/1/estrategias', methods=['GET'])
def get_cliente_estrategias():
    pathDataBase= '../banco-de-dados/AgencIA.db'
    query = "SELECT * FROM estrategia"
    estrategias = databaseConnector(pathDataBase, query)
    return jsonify(clienteEstrategiasJson(estrategias))

#campanhas
@app.route('/cliente/1/estrategias/1/campanhas', methods=['GET'])
def get_cliente_estrategia_campanhas():
    pathDataBase= '../banco-de-dados/AgencIA.db'
    query = "SELECT * FROM campanha"
    campanhas = databaseConnector(pathDataBase, query)
    return jsonify(clienteCampanhasJson(campanhas))



if __name__ == '__main__':
    app.run(debug=True)