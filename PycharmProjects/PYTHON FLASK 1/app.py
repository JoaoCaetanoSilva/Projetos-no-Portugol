from flask import Flask
from flask_restful import Api
from resources.cliente import ListarCliente, CriarCliente, Cliente, ClientesPedidos
from resources.produto import ListarProduto, CriarProduto, Produto
from resources.pedido import ListarPedido, CriarPedido, Pedido

app = Flask(__name__)
api = Api(app)

api.add_resource(ListarCliente, '/clientes')
api.add_resource(CriarCliente, '/cliente')
api.add_resource(Cliente, '/cliente/<int:id>')
api.add_resource(ClientesPedidos, '/clientes/<int:id>/pedidos')

api.add_resource(ListarProduto, '/produtos')
api.add_resource(CriarProduto, '/produto')
api.add_resource(Produto, '/produto/<int:id>')

api.add_resource(ListarPedido, '/pedidos/')
api.add_resource(CriarPedido, '/pedido/')
api.add_resource(Pedido, '/pedido/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)