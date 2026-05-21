from models.jogo_models import Jogo
from db import db
from flask import jsonify


# Função para obter todos os jogos
def get_jogos():
    jogos = Jogo.query.all()

    return jsonify({
        'mensagem': 'Lista de jogos.',
        'dados': [jogo.json() for jogo in jogos]
    })


# Função para obter um jogo específico por ID
def get_jogo_by_id(jogo_id):
    jogo = Jogo.query.get(jogo_id)

    if jogo:
        return jsonify({
            'mensagem': 'Jogo encontrado.',
            'dados': jogo.json()
        })

    return jsonify({
        'mensagem': 'Jogo não encontrado.',
        'dados': {}
    }), 404


# Função para criar um novo jogo
def create_jogo(jogo_data):

    # Valida os campos obrigatórios
    if not all(key in jogo_data for key in ['titulo', 'genero', 'ano']):
        return jsonify({
            'mensagem': 'Dados inválidos. Título, gênero e ano são obrigatórios.'
        }), 400

    # Cria o jogo
    novo_jogo = Jogo(
        titulo=jogo_data['titulo'],
        genero=jogo_data['genero'],
        ano=jogo_data['ano']
    )

    db.session.add(novo_jogo)
    db.session.commit()

    return jsonify({
        'mensagem': 'Jogo cadastrado com sucesso.',
        'jogo': novo_jogo.json()
    })


# Função para atualizar um jogo
def update_jogo(jogo_id, jogo_data):

    jogo = Jogo.query.get(jogo_id)

    # Verifica se o jogo existe
    if not jogo:
        return jsonify({
            'mensagem': 'Jogo não encontrado.'
        }), 404

    # Valida os campos obrigatórios
    if not all(key in jogo_data for key in ['titulo', 'genero', 'ano']):
        return jsonify({
            'mensagem': 'Dados inválidos. Título, gênero e ano são obrigatórios.'
        }), 400

    # Atualiza os dados
    jogo.titulo = jogo_data['titulo']
    jogo.genero = jogo_data['genero']
    jogo.ano = jogo_data['ano']

    db.session.commit()

    return jsonify({
        'mensagem': 'Jogo atualizado com sucesso.',
        'jogo': jogo.json()
    })