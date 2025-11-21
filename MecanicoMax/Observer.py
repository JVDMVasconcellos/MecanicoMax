from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List
from MecanicoMax.Factory_Method import Veiculo
from MecanicoMax.Strategy import EstrategiaPrecificacao 


class Observer(ABC):
    """Interface para observadores"""
    
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass


class Cliente(Observer):
    """Cliente que será notificado sobre mudanças"""
    
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone
        self.notificacoes: List[str] = []
    
    def atualizar(self, mensagem: str):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        notificacao = f"[{timestamp}] {mensagem}"
        self.notificacoes.append(notificacao)
        print(f"Notificação para {self.nome}: {mensagem}")
    
    def ver_historico(self):
        print(f"\nHistórico de notificações de {self.nome}:")
        for notif in self.notificacoes:
            print(f"  {notif}")


class OrdemServico:
    """Ordem de serviço que notifica observadores"""
    
    def __init__(self, veiculo: Veiculo, servico: str, 
                 estrategia_preco: EstrategiaPrecificacao):
        self.veiculo = veiculo
        self.servico = servico
        self.estrategia_preco = estrategia_preco
        self.status = "Aguardando"
        self.observadores: List[Observer] = []
        self.horas_trabalho = 0.0
        self.preco_final = 0.0
    
    def adicionar_observador(self, observador: Observer):
        self.observadores.append(observador)
    
    def remover_observador(self, observador: Observer):
        self.observadores.remove(observador)
    
    def notificar_observadores(self, mensagem: str):
        for observador in self.observadores:
            observador.atualizar(mensagem)
    
    def mudar_status(self, novo_status: str):
        self.status = novo_status
        mensagem = f"Seu veículo {self.veiculo.placa} - Status: {novo_status}"
        self.notificar_observadores(mensagem)
    
    def calcular_preco(self, horas: float):
        self.horas_trabalho = horas
        preco_base = self.estrategia_preco.calcular_preco(self.servico, horas)
        taxa_veiculo = self.veiculo.get_taxa_manutencao()
        self.preco_final = preco_base * taxa_veiculo
        
        mensagem = f"Orçamento pronto! Serviço: {self.servico} - R$ {self.preco_final:.2f}"
        self.notificar_observadores(mensagem)
    
    def __str__(self):
        return (f"OS: {self.servico} | {self.veiculo.placa} | "
                f"Status: {self.status} | R$ {self.preco_final:.2f}")