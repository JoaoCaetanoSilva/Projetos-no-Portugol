from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from modelos.clientes import Clientes
from modelos.produtos import Produtos

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

class Produto(Resource):
    def get(self, id):
        produto = Produtos.query.filter_by(id=id).first()

        try:
            response = {
                'produto_id':produto.id,
                'itens':produto.item,
                'preco':produto.preco,
                'descricao':produto.descricao
            }
        except AttributeError:
            response = {
                'status':'Produto nao encontrado'
            }
        return response

    def put(self, id):
        produto = Produtos.query.filter_by(id=id).first()
        dados = request.json
        if 'item' in dados:
            produto.item = dados['item']
        if 'preco' in dados:
            produto.preco = dados['preco']
        if 'descricao' in dados:
            produto.descricao = dados['descricao']
        produto.save()
        response = {
            'produto_id':produto.id,
            'itens':produto.item,
            'preco':produto.preco,
            'descricao':produto.descricao
        }
        return response

    def delete(self, id):
        produto = Produtos.query.filter_by(id=id).first()
        produto.delete()
        response = {
            'status': 'Produto deletado'
        }
        return response

class ListarProduto(Resource):
    def get(self):
        produtos = Produtos.query.all()
        response = [{'produto_id':i.id, 'itens':i.item, 'preco':i.preco, 'descricao':i.descricao} for i in produtos]
        return response

class CriarProduto(Resource):

    def post(self):
        dados = request.json
        cliente = Clientes.query.filter_by(nome=dados['nome_cliente']).first()
        produto = Produtos(item=dados['itens'], preco=dados['preco'], descricao=dados['descricao'])
        produto.save()
        response = {
            'produto_id':produto.id,
            'nome_cliente':cliente.nome,
            'itens':produto.item,
            'preco':produto.preco,
            'descricao':produto.descricao
        }
        return response



if __name__ == '__main__':
    app.run(debug=True)