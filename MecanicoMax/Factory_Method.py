from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List

class TipoVeiculo(Enum):
    SEDAN = "sedan"
    SUV = "suv"
    ESPORTIVO = "esportivo"
    CAMINHONETE = "caminhonete"


class Veiculo(ABC):
    """Classe base abstrata para veículos"""
    
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tipo = None
    
    @abstractmethod
    def get_taxa_manutencao(self) -> float:
        """Retorna multiplicador de taxa para manutenção"""
        pass
    
    def __str__(self):
        return f"{self.tipo.value.upper()} - {self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}"


class Sedan(Veiculo):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        super().__init__(placa, marca, modelo, ano)
        self.tipo = TipoVeiculo.SEDAN
    
    def get_taxa_manutencao(self) -> float:
        return 1.0 


class SUV(Veiculo):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        super().__init__(placa, marca, modelo, ano)
        self.tipo = TipoVeiculo.SUV
    
    def get_taxa_manutencao(self) -> float:
        return 1.3  #30% mais caro


class Esportivo(Veiculo):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        super().__init__(placa, marca, modelo, ano)
        self.tipo = TipoVeiculo.ESPORTIVO
    
    def get_taxa_manutencao(self) -> float:
        return 1.8  #80% mais caro


class Caminhonete(Veiculo):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        super().__init__(placa, marca, modelo, ano)
        self.tipo = TipoVeiculo.CAMINHONETE
    
    def get_taxa_manutencao(self) -> float:
        return 1.4  #40% mais caro


class FabricaVeiculos:
    """Factory Method para criar veículos"""
    
    @staticmethod
    def criar_veiculo(tipo: TipoVeiculo, placa: str, marca: str, 
                      modelo: str, ano: int) -> Veiculo:
        if tipo == TipoVeiculo.SEDAN:
            return Sedan(placa, marca, modelo, ano)
        elif tipo == TipoVeiculo.SUV:
            return SUV(placa, marca, modelo, ano)
        elif tipo == TipoVeiculo.ESPORTIVO:
            return Esportivo(placa, marca, modelo, ano)
        elif tipo == TipoVeiculo.CAMINHONETE:
            return Caminhonete(placa, marca, modelo, ano)
        else:
            raise ValueError(f"Tipo de veículo inválido: {tipo}")