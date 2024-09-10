from graphviz import Digraph

# Ajustando o Diagrama de Entidade-Relacionamento (DER) com as cardinalidades claras

dot = Digraph(comment='DER - Sistema de Gerenciamento de Biblioteca')

# Entidade Usuário
dot.node('Usuário', '''Usuário
---------------
Código (PK)
Nome
E-mail
Telefone''')

# Entidade Livro
dot.node('Livro', '''Livro
---------------
Código (PK)
Título
Autor
Editora
Ano de Publicação
Qtd. Exemplares''')

# Entidade Empréstimo
dot.node('Empréstimo', '''Empréstimo
---------------
Código (PK)
Data Início
Data Devolução Prev.
Data Devolução Efet.
Multa''')

# Relacionamento Realiza (Usuário - Empréstimo)
dot.edge('Usuário', 'Empréstimo', label='1:N Realiza')

# Relacionamento Refere-se (Empréstimo - Livro)
dot.edge('Empréstimo', 'Livro', label='1:N Contém')

# Renderizar o diagrama com as cardinalidades ajustadas
dot.render('/mnt/d/git/PythonRedes/java script/DER_Biblioteca_Cardinalidades', format='png')
'/mnt/d/git/PythonRedes/java script/DER_Biblioteca_Cardinalidades.png'
