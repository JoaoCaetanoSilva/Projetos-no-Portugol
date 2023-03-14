from flask import Flask, request
from flask_restful import Resource, Api
from projeto1.estrutura import Testes, Relacionar

app = Flask(__name__)
api = Api(app)

class Teste(Resource):
    def get(self, id):
        try:
            teste = Testes.query.filter_by(id=id).first()
            response = {
                'id':teste.id,
                'nome':teste.nome,
                'valor1':teste.valor1,
                'valor2':teste.valor2,
                'valor_final':teste.valor1 * teste.valor2,
                'palavra':teste.palavra,
                'codigo':[ord(x) - 97 for x in teste.palavra],
                'maiuscula':teste.maiuscula.upper(),
                'minuscula':teste.minuscula.lower()
            }
        except:
            response = {
                'status':'Teste nao encontrado'
            }
        return response

    def put(self, id):
        try:
            teste = Testes.query.filter_by(id=id).first()
            dados = request.json
            if 'nome' in dados:
                teste.nome = dados['nome']
            if 'valor1' in dados:
                teste.valor1 = dados['valor1']
            if 'valor2' in dados:
                teste.valor2 = dados['valor2']
            if 'palavra' in dados:
                teste.palavra = dados['palavra']
            if 'maiuscula' in dados:
                teste.maiuscula = dados['maiuscula']
            if 'minuscula' in dados:
                teste.minuscula = dados['minuscula']
            teste.save()
            teste.edit_file()
            response = {
                'id':teste.id,
                'nome':teste.nome,
                'valor1':teste.valor1,
                'valor2':teste.valor2,
                'valor_final': teste.valor1 * teste.valor2,
                'palavra':teste.palavra,
                'codigo':[ord(x) - 97 for x in teste.palavra],
                'maiuscula':teste.maiuscula,
                'minuscula':teste.minuscula
            }
        except:
            response = {
                'status':'Teste nao encontrado'
            }
        return response

    def delete(self, id):
        try:
            teste = Testes.query.filter_by(id=id).first()
            mensagem = 'Pessoa {} excluida com sucesso'.format(teste.nome)
            teste.delete()
            teste.delete_file()
            return {'status':'sucesso', 'mensagem':mensagem}
        except:
            response = {
                'status':'Teste nao encontrado'
            }
        return response
# Se excluido 2 nomes o 2° cai na excecao mais exclui
class ListaTestes(Resource):
    def get(self):
        try:
            testes = Testes.query.all()
            response = [{'id':i.id,
                         'nome':i.nome,
                         'valor1':i.valor1,
                         'valor2':i.valor2,
                         'valor_final':i.valor1 * i.valor2,
                         'palavra':i.palavra,
                         'codigo':i.palavra,
                         'maiuscula':i.maiuscula.upper(),
                         'minuscula':i.minuscula.lower()} for i in testes]
        except:
            response = {
                'status': 'Teste não encontrado'
            }
        return response

    def post(self):
        try:
            dados = request.json
            teste = Testes(nome=dados['nome'],
                           valor1=dados['valor1'],
                           valor2=dados['valor2'],
                           palavra=dados['palavra'],
                           maiuscula=dados['maiuscula'],
                           minuscula=dados['minuscula'])
            teste.save()
            teste.save_file()
            response = {
                'id':teste.id,
                'nome':teste.nome,
                'valor1':teste.valor1,
                'valor2':teste.valor2,
                'palavra':teste.palavra,
                'codigo':[ord(x) - 97 for x in teste.palavra],
                'maiuscula':teste.maiuscula,
                'minuscula':teste.minuscula
            }
        except:
            response = {
                'status':'Algum campo não preenchido'
            }
        return response

class Relacionamentos(Resource):
    def get(self, id):
        try:
            relacionamentos = Relacionar.query.filter_by(id=id).first()
            response = {
                'id': relacionamentos.id,
                'status': relacionamentos.status,
                'nome': relacionamentos.teste.nome,
            }
        except:
            response = {
                'status': ' Relacionamento não encontrado'
            }
        return response

    def delete(self, id):
        try:
            relacionamentos = Relacionar.query.filter_by(id=id).first()
            mensagem = 'Relacionamento {} excluido com sucesso'.format(relacionamentos.id)
            relacionamentos.delete()
            return {'status':'sucesso', 'mensagem':mensagem}
        except:
            response = {
                'status':'Relacionamento nao encontrado'
            }
        return response

class ListaRelacionar(Resource):
    def get(self):
        relacionar = Relacionar.query.all()
        try:
            response = [{'id':i.id,
                         'status':i.status,
                         'nome':i.teste.nome} for i in relacionar]
        except:
            response = {
                'status':'Relacionamento nao encontrado'
            }
        return response

    def post(self):
        dados = request.json
        teste = Testes.query.filter_by(nome=dados['nome']).first()
        relacionar = Relacionar(status=dados['status'], teste=teste)
        try:
            relacionar.save()
            response = {
                'id': relacionar.id,
                'id/teste': relacionar.teste.id,
                'status': relacionar.status,
                'nome': relacionar.teste.nome
            }
        except:
            response = {
                'status':'Id nao encontrado'
            }
        return response

api.add_resource(Teste, '/teste/<int:id>/')
api.add_resource(ListaTestes, '/testes/')
api.add_resource(Relacionamentos, '/relacionar/<int:id>/')
api.add_resource(ListaRelacionar, '/relacionar/')


if __name__ == '__main__':
    app.run(debug=True)
