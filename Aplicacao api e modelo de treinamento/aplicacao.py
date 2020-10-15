import os
import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from tensorflow import keras
import base64
import json

""" instanciando flask"""
aplicacao = Flask(__name__)
""" instanciando api"""
api = Api(aplicacao)


class predi(Resource):
    @aplicacao.route('/')
    def get(self):
        """Informo que retorna meu html criado """
        return render_template ('nome do html')

    """
        Carregar meu modelo 
    """
    global modelo
    modelo = keras.models.load_model('modelo1_treinado.h5')  # Dessa maneira estou  obtenho um erro porem ainda nao achei outra solução


    @aplicacao.route('/upload', methods=["POST"])
    def post(self):

        """Obter o formulario"""
        d = request.form
        """Extraio o campo de dados"""
        ext = d.get('DATA')
        ext = ext.split(',')
        """Pegamos a base64 e decodificamos """
        ext = base64.decodebytes(ext.encode())
        """Converter para um array unidimensional """
        arr = np.frombuffer(ext)

        """ Estou solução parado aqui 
        
        """
        args = request.get_json(force=True)

        return json.dumps({})



""" Adicionar a api a predição"""




if __name__ == '__main__':
    aplicacao.run(host='localhost', port='5000')
