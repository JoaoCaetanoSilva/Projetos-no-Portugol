from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os
engine = create_engine('sqlite:///banco.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Testes(Base):
    __tablename__='testes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), index=True)
    valor1 = Column(Integer)
    valor2 = Column(Integer)
    palavra = Column(String(30))
    maiuscula = Column(String(30))
    minuscula = Column(String(30))

    def __repr__(self):
        return '<Teste {}>'.format(self.nome)

    def save_file(self):
        arquivo = open('salvar.txt', 'w')
        arquivo.write('salvando')
        arquivo.close()

    def edit_file(self):
        arquivo = open('salvar.txt', 'w')
        arquivo.write('editando')
        arquivo.close()

    def delete_file(self):
        os.remove("salvar.txt")

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Relacionar(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    status = Column(String(30))
    teste_id = Column(Integer, ForeignKey('testes.id'))
    teste = relationship("Testes")

    def __repr__(self):
        return '<Relacionar {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

