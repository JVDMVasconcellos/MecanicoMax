from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List
from .Factory_Method import TipoVeiculo
from .Strategy import PrecoPorHora, PrecoPorComplexidade, PrecoPacote
from .Singleton import Oficina



def main():
    print("\n" + "="*70)
    print("SISTEMA DE GERENCIAMENTO DE OFICINA MECÂNICA")
    print("="*70 + "\n")
    
    # Singleton - Sempre retorna a mesma instância
    oficina = Oficina()

    print("\nCADASTRANDO CLIENTES")
    print("-" * 70)
    cliente1 = oficina.cadastrar_cliente("João Silva", "(19) 98765-4321")
    cliente2 = oficina.cadastrar_cliente("Maria Santos", "(19) 99876-5432")
    
    # Factory Method - Criando diferentes tipos de veículos
    print("\nCADASTRANDO VEÍCULOS")
    print("-" * 70)
    veiculo1 = oficina.cadastrar_veiculo(
        TipoVeiculo.SEDAN, "ABC-1234", "Honda", "Civic", 2020
    )
    veiculo2 = oficina.cadastrar_veiculo(
        TipoVeiculo.SUV, "XYZ-5678", "Toyota", "RAV4", 2021
    )
    veiculo3 = oficina.cadastrar_veiculo(
        TipoVeiculo.ESPORTIVO, "SPT-9999", "Porsche", "911", 2022
    )
    
    # Strategy - Diferentes estratégias de precificação
    print("\nCRIANDO ORDENS DE SERVIÇO")
    print("-" * 70)
    
    estrategia1 = PrecoPorHora(valor_hora=80.0)
    os1 = oficina.criar_ordem_servico(
        veiculo1, "revisao_geral", estrategia1, cliente1
    )
    os1.calcular_preco(horas=3.5)
    os1.mudar_status("Em execução")
    
    estrategia2 = PrecoPorComplexidade()
    os2 = oficina.criar_ordem_servico(
        veiculo2, "troca_pastilhas", estrategia2, cliente2
    )
    os2.calcular_preco(horas=2.0)  
    os2.mudar_status("Em execução")
    os2.mudar_status("Concluído")
    
    estrategia3 = PrecoPacote()
    os3 = oficina.criar_ordem_servico(
        veiculo3, "pacote_performance", estrategia3, cliente1
    )
    os3.calcular_preco(horas=0)  
    os3.mudar_status("Aguardando aprovação do cliente")
    
    # Observer - Histórico de notificações
    print("\n")
    cliente1.ver_historico()
    print("\n")
    cliente2.ver_historico()
    
    oficina.listar_ordens_servico()  
    oficina.relatorio_geral()
    
    # Singleton - Testando a instância única
    print("TESTANDO SINGLETON")
    print("-" * 70)
    oficina2 = Oficina()
    print(f"oficina é oficina2? {oficina is oficina2}")
    print(f"Mesma quantidade de ordens? {len(oficina2.ordens_servico)} OSs\n")


if __name__ == "__main__":
    main()