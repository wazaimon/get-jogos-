# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy
from db import db  

# Define a classe Jogo que representa a tabela 'jogos' no banco de dados
class Jogo(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'jogos'  

    # Define as colunas da tabela 'jogos'
    id = db.Column(db.Integer, primary_key=True)  # ID do jogo
    titulo = db.Column(db.String(80), nullable=False)  # Título do jogo
    genero = db.Column(db.String(80), nullable=False)  # Gênero do jogo
    ano = db.Column(db.Integer, nullable=False)  # Ano do jogo

    # Método para retornar os dados do jogo como um dicionário
    def json(self):  
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'ano': self.ano
        }