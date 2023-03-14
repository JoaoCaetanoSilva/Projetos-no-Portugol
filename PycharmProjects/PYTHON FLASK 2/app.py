import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'Nome':'Carlao',
     'Habilidades':['Python', 'Flask']
    },
    {
     'Nome':'Ana',
     'Habilidades':['Django', 'Php']
    }
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            return jsonify(response)
        except IndexError:
            return('Item já excluido')
        except Exception:
            return('Erro desconhecido, procure o adiministrador da API')

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    else:
        desenvolvedores.pop(id)
        return('Sucesso')

@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'GET':
        return jsonify(desenvolvedores)

    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

if __name__ == '__main__':
    app.run(debug=True)
