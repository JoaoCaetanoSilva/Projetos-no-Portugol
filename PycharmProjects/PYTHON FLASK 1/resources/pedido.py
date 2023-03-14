from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from modelos.pedidos import Pedidos
from modelos.produtos import Produtos
from modelos.clientes import Clientes

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

class Pedido(Resource):
    def get(self, id):
        pedido = Pedidos.query.filter_by(id=id)
        produto = Produtos.query.filter_by(id=pedido.produto_id).first()
        cliente = Clientes.query.filter_by(id=pedido.cliente_id).first()
        try:
            response = {
                'pedido_id':pedido.id,
                'data':pedido.data,
                'quantidade':pedido.quantidade,
                'valor_unitario':pedido.valor_unitario,
                'valor_total':pedido.quantidade * pedido.valor_unitario,
                'status':pedido.status,
                'informacoes_do_produto':produto.item,
                'cliente':cliente.nome
            }
        except AttributeError:
            response = {
                'status':'Pedido nao encontrado'
            }
        return response

    def put(self, id):
        pedido = Pedidos.query.filter_by(id=id).first()
        dados = request.json
        if 'data' in dados:
            pedido.data = dados['data']
        if 'quantidade' in dados:
            pedido.quantidade = dados['quantidade']
        if 'valor_unitario' in dados:
            pedido.valor_unitario = dados['valor_unitario']
        if 'status' in dados:
            pedido.status = dados['status']
        pedido.save()
        response = {
            'pedido_id': pedido.id,
            'data': pedido.data,
            'quantidade': pedido.quantidade,
            'valor_unitario': pedido.valor_unitario,
            'status': pedido.status
        }
        return response

    def delete(self, id):
        pedido = Pedidos.query.filter_by(id=id).first()
        pedido.delete()
        response = {
            'status': 'Produto deletado'
        }
        return response

class ListarPedido(Resource):
    def get(self):
        pedidos = Pedidos.query.all()
        response = [{'pedido_id':i.id,
                     'data':i.data,
                     'quantidade':i.quantidade,
                     'valor_unitario':i.valor_unitario,
                     'status':i.status,
                     'valor_total': i.quantidade * i.valor_unitario,
                     'cliente_id':i.cliente_id,
                     'produto_id':i.produto_id
                     } for i in pedidos]
        return response

class CriarPedido(Resource):
    def post(self):
        dados = request.json
        cliente = Clientes.query.filter_by(nome=dados['nome_cliente']).first()
        produto = Produtos.query.filter_by(nome=dados['item']).first()
        pedido = Pedidos(data=dados['data'],
                         status=dados['status'],
                         quantidade=dados['quantidade'],
                         valor_unitario=produto.preco,
                         produto_id=produto.id,
                         cliente_id=cliente.id
                        )
        pedido.save()
        response = {
            'pedido_id': pedido.id,
            'data': pedido.data,
            'quantidade': pedido.quantidade,
            'valor_unitario': pedido.valor_unitario,
            'valor_total': pedido.quantidade * pedido.valor_unitario,
            'status': pedido.status,
            'informacoes_do_produto': produto.item,
            'cliente': cliente.nome
        }
        return response



if __name__ == '__main__':
    app.run(debug=True)