# **MecanicoMax 🔧**

Sistema de Gerenciamento de Oficina Mecânica desenvolvido em Python, implementando padrões de projeto de software para demonstrar boas práticas de arquitetura e design orientado a objetos.

## **Descrição do Projeto**

**MecanicoMax** é uma aplicação console que simula o gerenciamento completo de uma oficina mecânica, incluindo:

* ✅ Cadastro de clientes e veículos  
* ✅ Criação e gerenciamento de ordens de serviço  
* ✅ Sistema de notificações automáticas para clientes  
* ✅ Múltiplas estratégias de precificação de serviços  
* ✅ Relatórios gerenciais e histórico de atendimentos

O sistema foi projetado para demonstrar a aplicação prática de **4 padrões de projeto** fundamentais, proporcionando uma arquitetura flexível, extensível e de fácil manutenção.

## **Objetivo Acadêmico**

Este projeto foi desenvolvido como parte da disciplina de **Padrões e Arquitetura de Software** do curso de Sistemas de Informação, com foco no estudo e aplicação prática de Design Patterns descritos no livro "Design Patterns: Elements of Reusable Object-Oriented Software" (Gang of Four) e disponíveis na plataforma [Refactoring.Guru](https://refactoring.guru).

## **Padrões de Projeto Implementados**

### **1\. Factory Method (Criacional)**

* **Arquivo:** `MecanicoMax/Factory_Method.py`  
* **Classes:** `FabricaVeiculos`, `Veiculo` (abstrata), `Sedan`, `SUV`, `Esportivo`, `Caminhonete`  
* **Propósito:** Centraliza a criação de diferentes tipos de veículos, permitindo extensão sem modificar código existente  
* **Localização no código:**  
  * Linha 69-81: Método `criar_veiculo()` da classe `FabricaVeiculos`  
  * Linhas 13-66: Hierarquia de classes de veículos

### **2\. Singleton (Criacional)**

* **Arquivo:** `MecanicoMax/Singleton.py`  
* **Classe:** `Oficina`  
* **Propósito:** Garante uma única instância da oficina em todo o sistema, mantendo consistência de dados  
* **Localização no código:**  
  * Linhas 10-18: Implementação do padrão usando `__new__` e `__init__`  
  * Linha 12: Atributo de classe `_instancia` que armazena a única instância

### **3\. Strategy (Comportamental)**

* **Arquivo:** `MecanicoMax/Strategy.py`  
* **Classes:** `EstrategiaPrecificacao` (abstrata), `PrecoPorHora`, `PrecoPorComplexidade`, `PrecoPacote`  
* **Propósito:** Permite alternar entre diferentes algoritmos de cálculo de preço de serviços  
* **Localização no código:**  
  * Linhas 6-10: Interface `EstrategiaPrecificacao`  
  * Linhas 13-55: Implementações concretas das três estratégias

### **4\. Observer (Comportamental)**

* **Arquivo:** `MecanicoMax/Observer.py`  
* **Classes:** `Observer` (abstrata), `Cliente`, `OrdemServico`  
* **Propósito:** Notifica automaticamente clientes sobre mudanças no status de seus veículos  
* **Localização no código:**  
  * Linhas 8-12: Interface `Observer`  
  * Linhas 15-30: Classe `Cliente` implementando Observer  
  * Linhas 33-67: Classe `OrdemServico` implementando Subject com métodos de gerenciamento de observadores

## **Estrutura do Projeto**

MecanicoMax/  
│  
├── MecanicoMax/  
│   ├── \_\_init\_\_.py              \# Inicialização do pacote Python  
│   ├── Factory\_Method.py        \# Padrão Factory Method \- Criação de veículos  
│   ├── Strategy.py              \# Padrão Strategy \- Estratégias de precificação  
│   ├── Observer.py              \# Padrão Observer \- Sistema de notificações  
│   ├── Singleton.py             \# Padrão Singleton \- Gerenciamento da oficina  
│   └── Main.py                  \# Arquivo principal com demonstração  
│  
├── .vscode/  
│   └── launch.json              \# Configurações de debug do VS Code  
│  
├── README.md                    \# Este arquivo  
├── RESUMO.md                    \# Documentação técnica detalhada dos padrões

└── requirements.txt             \# Dependências do projeto (se houver)

## **Instruções de Execução**

### **Pré-requisitos**

* **Python 3.8 ou superior** instalado  
* Sistema operacional: Windows, Linux ou macOS

### **Verificar Instalação do Python**

bash  
python \--version  
*\# ou*

python3 \--version

### **Opção 1: Executar como Módulo (Recomendado)**

Navegue até o diretório raiz do projeto e execute:

bash

python \-m MecanicoMax.Main

Ou no Linux/macOS:

bash

python3 \-m MecanicoMax.Main

### **Opção 2: Executar Diretamente**

Defina o PYTHONPATH e execute o arquivo Main:

**Windows (PowerShell):**

powershell  
$env:PYTHONPATH="."

python MecanicoMax/Main.py

**Windows (CMD):**

cmd  
set PYTHONPATH=.

python MecanicoMax\\Main.py

**Linux/macOS:**

bash  
export PYTHONPATH=.  
python3 MecanicoMax/Main.py  
\`\`\`

*\#\#\# Opção 3: Usando VS Code*

Se estiver usando Visual Studio Code:

1. Abra o projeto no VS Code  
2. Pressione \`F5\` ou vá em \*\*Run → Start Debugging\*\*  
3. Selecione a configuração \*\*"Python: Run MecanicoMax as module"\*\*

*\#\# Saída Esperada*

Ao executar o programa, você verá:  
\`\`\`  
\======================================================================  
SISTEMA DE GERENCIAMENTO DE OFICINA MECÂNICA  
\======================================================================

CADASTRANDO CLIENTES  
\----------------------------------------------------------------------  
Cliente João Victor Vasconcellos cadastrado com sucesso\!  
Cliente Vitor Carnevalli cadastrado com sucesso\!

CADASTRANDO VEÍCULOS  
\----------------------------------------------------------------------  
Veículo cadastrado: SEDAN \- Honda Civic (2020) \- Placa: NTC-5H67  
Veículo cadastrado: SUV \- Mitsubishi Outlander (2021) \- Placa: GDW-7G89  
Veículo cadastrado: ESPORTIVO \- Chevrolet Onix RS (2022) \- Placa: STI-4D14

CRIANDO ORDENS DE SERVIÇO  
\----------------------------------------------------------------------  
Ordem de serviço criada: revisao\_geral para NTC-5H67  
Notificação para João Victor Vasconcellos: Seu veículo NTC-5H67 \- Status: Em análise  
Notificação para João Victor Vasconcellos: Orçamento pronto\! Serviço: revisao\_geral \- R$ 280.00  
Notificação para João Victor Vasconcellos: Seu veículo NTC-5H67 \- Status: Em execução  
\[...\]

\======================================================================  
ORDENS DE SERVIÇO \- Oficina AutoMaster  
\======================================================================  
1. OS: revisao\_geral | NTC-5H67 | Status: Em execução | R$ 280.00  
2. OS: troca\_pastilhas | GDW-7G89 | Status: Concluído | R$ 455.00  
3. OS: pacote\_performance | STI-4D14 | Status: Aguardando aprovação | R$ 4500.00  
\======================================================================

TESTANDO SINGLETON  
\----------------------------------------------------------------------  
oficina é oficina2? True

Mesma quantidade de ordens? 3 OSs

## **Fluxo de Execução**

1. **Inicialização do Singleton:** A oficina é criada como instância única  
2. **Cadastro de Clientes:** Clientes são registrados como observadores do sistema  
3. **Cadastro de Veículos:** Diferentes tipos de veículos são criados via Factory Method  
4. **Criação de Ordens de Serviço:**  
   * Associação entre veículo, cliente e estratégia de preço  
   * Notificações automáticas são enviadas aos clientes  
5. **Mudanças de Status:** Clientes são notificados automaticamente  
6. **Cálculo de Preços:** Diferentes estratégias são aplicadas  
7. **Relatórios:** Exibição de histórico e resumo geral  
8. **Validação do Singleton:** Confirmação de instância única

## **Como Testar os Padrões**

### **Testar Factory Method**

Modifique o `Main.py` para criar novos tipos de veículos:

python  
*\# Adicione novos veículos*  
veiculo4 \= oficina.cadastrar\_veiculo(  
    TipoVeiculo.CAMINHONETE, "ABC-1234", "Ford", "Ranger", 2023

)

### **Testar Singleton**

Adicione no `Main.py`:

python  
oficina3 \= Oficina()

print(f"Todas as instâncias são iguais? {oficina is oficina2 is oficina3}")

### **Testar Strategy**

Crie novas estratégias ou modifique valores:

python  
*\# Nova estratégia com valor diferente*  
estrategia\_premium \= PrecoPorHora(valor\_hora\=150.0)

os\_premium \= oficina.criar\_ordem\_servico(veiculo1, "manutencao\_especial", estrategia\_premium, cliente1)

### **Testar Observer**

Adicione múltiplos clientes à mesma ordem de serviço:

python  
os1.adicionar\_observador(cliente2)  *\# Dois clientes notificados*

os1.mudar\_status("Serviço concluído")  *\# Ambos recebem notificação*

## **🛠️ Extensões Futuras**

O projeto foi projetado para fácil extensão:

* **Novos tipos de veículos:** Adicione classes em `Factory_Method.py`  
* **Novas estratégias de preço:** Implemente `EstrategiaPrecificacao` em `Strategy.py`  
* **Novos observadores:** Crie classes que implementem `Observer` (ex: sistema de SMS, email)  
* **Persistência de dados:** Adicione um banco de dados (SQLite, PostgreSQL)  
* **Interface gráfica:** Integre com Tkinter, PyQt ou crie uma API REST

## **Documentação Adicional**

Para entender em profundidade os padrões implementados, consulte:

* **RESUMO.md:** Documentação técnica completa com:  
  * Descrição detalhada de cada padrão  
  * Justificativas de implementação  
  * Comparações entre padrões  
  * Exemplos de código com e sem padrões  
  * Trade-offs e lições aprendidas

## **Autores**

* **João Victor Vasconcellos**  
* **Vitor Carnevalli**

**Disciplina:** Padrões e Arquitetura de Software  
 **Curso:** Sistemas de Informação  
 **Instituição:** \[Nome da Instituição\]

## **Referências**

* [Refactoring.Guru \- Design Patterns](https://refactoring.guru/design-patterns)  
* Gamma, E. et al. \- Design Patterns: Elements of Reusable Object-Oriented Software  
* Freeman, E. & Robson, E. \- Head First Design Patterns

## **Licença**

Este projeto foi desenvolvido para fins educacionais como parte de atividade acadêmica.

