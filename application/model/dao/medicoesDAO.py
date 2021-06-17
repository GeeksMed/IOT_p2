from application.model.entity.medicoes import Medicoes

class MedicoesDAO:
    def __init__(self, medicoes_list):
        self.__medicoes_list = medicoes_list

    def mostrar_medicoes(self):
        return self.__medicoes_list