from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List
from MecanicoMax.Observer import Cliente, OrdemServico
from MecanicoMax.Factory_Method import Veiculo, TipoVeiculo, FabricaVeiculos
from MecanicoMax.Strategy import EstrategiaPrecificacao

class Oficina:
    """Singleton para gerenciar a oficina"""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Oficina, cls).__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia
    
    def __init__(self):
        if self._inicializado:
            return
        
        self._inicializado = True
        self.nome = "Oficina AutoMaster"
        self.ordens_servico: List[OrdemServico] = []
        self.veiculos_cadastrados: List[Veiculo] = []
        self.clientes_cadastrados: List[Cliente] = []
    
    def cadastrar_cliente(self, nome: str, telefone: str) -> Cliente:
        cliente = Cliente(nome, telefone)
        self.clientes_cadastrados.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente
    
    def cadastrar_veiculo(self, tipo: TipoVeiculo, placa: str, 
                         marca: str, modelo: str, ano: int) -> Veiculo:
        veiculo = FabricaVeiculos.criar_veiculo(tipo, placa, marca, modelo, ano)
        self.veiculos_cadastrados.append(veiculo)
        print(f"Veículo cadastrado: {veiculo}")
        return veiculo
    
    def criar_ordem_servico(self, veiculo: Veiculo, servico: str,
                           estrategia: EstrategiaPrecificacao,
                           cliente: Cliente) -> OrdemServico:
        os = OrdemServico(veiculo, servico, estrategia)
        os.adicionar_observador(cliente)
        self.ordens_servico.append(os)
        os.mudar_status("Em análise")
        print(f"Ordem de serviço criada: {servico} para {veiculo.placa}")
        return os
    
    def listar_ordens_servico(self):
        print(f"\n{'='*70}")
        print(f"ORDENS DE SERVIÇO - {self.nome}")
        print(f"{'='*70}")
        for i, os in enumerate(self.ordens_servico, 1):
            print(f"{i}. {os}")
        print(f"{'='*70}\n")
    
    def relatorio_geral(self):
        total_faturamento = sum(os.preco_final for os in self.ordens_servico)
        print(f"\n{'='*70}")
        print(f"RELATÓRIO GERAL - {self.nome}")
        print(f"{'='*70}")
        print(f"Clientes cadastrados: {len(self.clientes_cadastrados)}")
        print(f"Veículos cadastrados: {len(self.veiculos_cadastrados)}")
        print(f"Ordens de serviço: {len(self.ordens_servico)}")
        print(f"Faturamento total: R$ {total_faturamento:.2f}")
        print(f"{'='*70}\n")
