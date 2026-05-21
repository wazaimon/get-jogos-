from flask import Flask  # Importa o framework Flask para criar a aplicação web
from db import db  # Importa a instância do banco de dados SQLAlchemy
from routes.jogo_routes import jogo_routes  # Importa as rotas do módulo de jogos

app = Flask(__name__)  # Cria a instância da aplicação Flask

# Configura a URI do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogos.db'

# Desativa o rastreamento de modificações do SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a aplicação com a instância do banco de dados
db.init_app(app)

# Registra o blueprint das rotas de jogo na aplicação Flask
app.register_blueprint(jogo_routes)

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':

    # Garante que as tabelas do banco de dados sejam criadas
    with app.app_context():
        db.create_all()

    # Inicia o servidor Flask no modo debug
    app.run(debug=True)