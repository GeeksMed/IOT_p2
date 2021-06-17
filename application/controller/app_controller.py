from application import app
from flask import Flask, jsonify, request
import json
from datetime import datetime
from application.model.entity.medicoes import Medicoes
from application.model.dao.medicoesDAO import MedicoesDAO


def escrever_json(lista):
    medicoes = {"medicoes":lista}
    with open(r'application\medicoes.json', 'w') as f:
        json.dump(medicoes, f)


def carregar_json():
    with open(r'application\medicoes.json', 'r') as f:
        return json.load(f)


def carregar_lista():
    jsonfile = carregar_json()
    medicoes_dao = MedicoesDAO(jsonfile)
    return medicoes_dao.mostrar_medicoes()["medicoes"]


@app.route("/medicoes", methods=['GET'])
def list_medicoes():
    medicoes_list = carregar_lista()
    medicoes_dict_list = []
    for medicao in medicoes_list:
        medicoes_dict_list.append(medicao)
    return jsonify(medicoes_dict_list)


@app.route("/medicoes", methods=['POST'])
def add_medicoes():
    medicoes_list = carregar_lista()
    id = int(request.json.get('id', None))
    ozonio = float(request.json.get('ozonio', None))
    material_particulado = float(request.json.get('material_particulado', None))
    monoxido_carbono = float(request.json.get('monoxido_carbono', None))
    #dioxido_enxofre = float(request.json.get('dioxido_enxofre', None))
    oxido_nitroso = float(request.json.get('oxido_nitroso', None))
    data = datetime.strptime(request.json.get('data', None), '%d/%m/%Y %H:%M')
    medicao = Medicoes(id, ozonio, material_particulado, monoxido_carbono, oxido_nitroso, data)
    medicoes_list.append(medicao.toDict())
    escrever_json(medicoes_list)
    return medicao.toDict(), 201


@app.route("/medicoes/<int:id>", methods=['GET'])
def view_medicoes_id(id: int):
    medicoes_list = carregar_lista()
    for medicao in medicoes_list:
        if medicao["id"] == id:
            return medicao
    return jsonify({"error": "Medição não encontrada"}), 404


@app.route("/medicoes/<dd>/<mm>/<aaaa>", methods=['GET'])
def view_medicoes_data(dd:str, mm:str, aaaa:str):
    medicoes_list = carregar_lista()
    medicoes_list_data = []
    for medicao in medicoes_list:
        print(str(medicao["data"])[0:10])
        if str(medicao["data"])[0:10] == f'{dd}/{mm}/{aaaa}':
            medicoes_list_data.append(medicao)
    if len(medicoes_list_data) > 0:
        return jsonify(medicoes_list_data)
    return jsonify({"error": "Medição não encontrada"}), 404