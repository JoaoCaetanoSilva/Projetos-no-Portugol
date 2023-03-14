from modelos import Pessoas, Usuarios

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome='Joao').first()
    # print(pessoa.idade)

def insere_pessoas():
    pessoa = Pessoas(nome='Luiza',
                     idade=15)
    print(pessoa)
    pessoa.save()

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.idade = 20
    pessoa.save()
    print('{} tem {} anos'.format(pessoa.nome, pessoa.idade))

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    # insere_usuario('Kaido', '2468')
    consulta_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()