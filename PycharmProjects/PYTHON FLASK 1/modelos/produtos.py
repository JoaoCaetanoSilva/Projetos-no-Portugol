from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///produtos.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Produtos(Base):
    __tablename__='produtos'
    id = Column(Integer, primary_key=True)
    item = Column(String(40), index=True)
    preco = Column(Integer)
    descricao = Column(String(100))
    cliente_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Produto {}>'.format(self.nome)

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