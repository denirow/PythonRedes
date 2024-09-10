from graphviz import Digraph

# Criação do diagrama ER
dot = Digraph()

# Entidade Generalização: Veículo
dot.node('Veículo', 'Veículo\n(ID_Veículo, Marca, Modelo, Ano)', shape='box')

# Entidades Especialização: Carro, Caminhão, Motocicleta
dot.node('Carro', 'Carro\n(Quantidade_Assentos)', shape='box')
dot.node('Caminhão', 'Caminhão\n(Capacidade_Carga)', shape='box')
dot.node('Motocicleta', 'Motocicleta\n(Cilindrada)', shape='box')

# Entidade Relacionada: Motorista
dot.node('Motorista', 'Motorista\n(ID_Motorista, Nome, Habilitação, Disponibilidade_Viagem)', shape='box')

# Conexões de Generalização/Especialização
dot.edge('Veículo', 'Carro', label='Especialização')
dot.edge('Veículo', 'Caminhão', label='Especialização')
dot.edge('Veículo', 'Motocicleta', label='Especialização')

# Conexão entre Motorista e Veículo
dot.edge('Motorista', 'Veículo', label='Pode dirigir')

# Renderizar o gráfico
dot.render('/mnt/d/git/PythonRedes/curso_bd/diagrama_er_generalizacao_especializacao', format='png', cleanup=True)
'/mnt/d/git/PythonRedes/curso_bd/diagrama_er_generalizacao_especializacao.png'