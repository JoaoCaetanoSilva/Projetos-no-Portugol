from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'Nome':'Carlao',
     'Habilidades':['Python', 'Flask']
    },
    {
     'Nome':'Ana',
     'Habilidades':['Django', 'Php']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
            return response
        except IndexError:
            return ('Item não encontrado ou já excluido')
        except Exception:
            return ('Erro desconhecido, procure o adiministrador da API')

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ('Sucesso')

class ListarDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListarDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/dev/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)