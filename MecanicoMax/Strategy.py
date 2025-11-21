from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List

class EstrategiaPrecificacao(ABC):
    """Interface para estratégias de cálculo de preço"""
    
    @abstractmethod
    def calcular_preco(self, servico: str, horas_trabalho: float) -> float:
        pass


class PrecoPorHora(EstrategiaPrecificacao):
    """Estratégia: preço calculado por hora de trabalho"""
    
    def __init__(self, valor_hora: float = 80.0):
        self.valor_hora = valor_hora
    
    def calcular_preco(self, servico: str, horas_trabalho: float) -> float:
        return self.valor_hora * horas_trabalho


class PrecoPorComplexidade(EstrategiaPrecificacao):
    """Estratégia: preço baseado na complexidade do serviço"""
    
    def __init__(self):
        self.tabela_complexidade = {
            "troca_oleo": 150.0,
            "alinhamento": 200.0,
            "balanceamento": 180.0,
            "revisao_completa": 800.0,
            "troca_pastilhas": 350.0,
            "diagnostico_eletronico": 250.0
        }
    
    def calcular_preco(self, servico: str, horas_trabalho: float) -> float:
        return self.tabela_complexidade.get(servico, 200.0)


class PrecoPacote(EstrategiaPrecificacao):
    """Estratégia: preço fixo por pacote de serviços"""
    
    def __init__(self):
        self.pacotes = {
            "pacote_basico": 400.0,
            "pacote_premium": 1200.0,
            "pacote_performance": 2500.0
        }
    
    def calcular_preco(self, servico: str, horas_trabalho: float) -> float:
        return self.pacotes.get(servico, 500.0)