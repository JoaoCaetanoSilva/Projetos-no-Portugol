from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from modelos.clientes import Clientes
from modelos.pedidos import Pedidos
from modelos.produtos import Produtos

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

class Cliente(Resource):
    def get(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        try:
            response = {
                'cliente_id':cliente.id,
                'nome_cliente':cliente.nome,
                'idade':cliente.idade,
                'endereco':cliente.endereco,
            }
        except AttributeError:
            response = {
                'status':'Cliente nao encontrado'
            }
        return response

    def put(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome_cliente' in dados:
            cliente.nome = dados['nome_cliente']
        if 'idade' in dados:
            cliente.idade = dados['idade']
        if 'endereco' in dados:
            cliente.endereco = dados['endereco']
        cliente.save()
        response = {
            'id':cliente.id,
            'nome_cliente':cliente.nome,
            'idade':cliente.idade,
            'endereco':cliente.endereco
        }
        return response

    def delete(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        cliente.delete()
        response = {
            'status': 'Cliente deletado'
        }
        return response

class ListarCliente(Resource):
    def get(self):
        clientes = Clientes.query.all()
        response = [{'cliente_id':i.id, 'nome_cliente':i.nome, 'idade':i.idade, 'endereco':i.endereco} for i in clientes]
        return response

class CriarCliente(Resource):
    def post(self):
        dados = request.json
        cliente = Clientes(nome=dados['nome'], idade=dados['idade'], endereco=dados['endereco'])
        cliente.save()
        response = {
            'cliente_id':cliente.id,
            'nome_cliente':cliente.nome,
            'idade':cliente.idade,
            'endereco':cliente.endereco
        }
        return response

class ClientesPedidos(Resource):
    def get(self, id):
        clientes = Clientes.query.filter_by(id=id).first()
        pedidos = Pedidos.query.filter_by(cliente_id=id).all()
        produtos = Produtos.query.all()
        response = [
            {
                'cliente_id': clientes.id,
                'nome_cliente': clientes.nome,
                'idade': clientes.idade,
                'endereco': clientes.endereco,
                'pedidos': [
                    {
                        'pedido_id':i.id,
                        'data_do_pedido':i.data,
                        'quantidade':i.quantidade,
                        'valor_unitario':i.valor_unitario,
                        'status':i.status
                    } for i in pedidos
                ],
                'produtos': [
                    {
                        'produtos_id':i.id,
                        'item': i.item,
                        'preco': i.preco,
                        'descricao': i.descricao
                    } for i in produtos
                ]
            }
        ]
        return response





if __name__ == '__main__':
    app.run(debug=True)