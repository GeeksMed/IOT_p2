from datetime import datetime


"""
Nosso sensor se concentra nos cinco componentes do Índice de Qualidade do Ar da Agência de
Proteção Ambiental: ozônio, material particulado, monóxido de carbono, dióxido de enxofre e óxido
nitroso. Este dispositivo detecta todos esses poluentes, exceto o dióxido de enxofre. 
"""
class Medicoes:
    def __init__(self, id: int, ozonio: float, material_particulado: float, monoxido_carbono: float, oxido_nitroso: float, data: datetime):
        self.__id = id
        self.__ozonio = ozonio #ppm -> partes por milhao
        self.__material_particulado = material_particulado #µm -> <50 já detectável; <10 mal a saúde; <2,5 muito mal
        self.__monoxido_carbono = monoxido_carbono #ppm -> partes por milhao
        #self.__dioxido_enxofre = dioxido_enxofre #ppm -> partes por milhao
        self.__oxido_nitroso = oxido_nitroso #ppm -> partes por milhao
        self.__data = data

    @property
    def id(self) -> int:
        return self.__id

    @property
    def ozonio(self) -> float:
        return self.__ozonio

    @ozonio.setter
    def ozonio(self, value: int) -> None:
        self.__ozonio = value

    @property
    def material_particulado(self) -> float:
        return self.__material_particulado
               
    @material_particulado.setter
    def material_particulado(self, value: int) -> None:
        self.__material_particulado = value

    @property
    def monoxido_carbono(self) -> float:
        return self.__monoxido_carbono
    
    @monoxido_carbono.setter
    def monoxido_carbono(self, value: int) -> None:
        self.__monoxido_carbono = value

    '''
    @property
    def dioxido_enxofre(self) -> float:
        return self.__dioxido_enxofre
        
    @dioxido_enxofre.setter
    def dioxido_enxofre(self, value: int) -> None:
        self.__dioxido_enxofre = value
    '''

    @property
    def oxido_nitroso(self) -> float:
        return self.__oxido_nitroso

    @oxido_nitroso.setter
    def oxido_nitroso(self, value: int) -> None:
        self.__oxido_nitroso = value

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, value: datetime) -> None:
        self.__data = value

    def toDict(self) -> dict:
        return {
            "id": self.__id,
            "ozonio": self.__ozonio,
            "material_particulado": self.__material_particulado,
            "monoxido_carbono": self.__monoxido_carbono,
            #"dioxido_enxofre": self.__dioxido_enxofre,
            "oxido_nitroso": self.__oxido_nitroso,
            "data": self.__data.strftime('%d/%m/%Y %H:%M')
        }