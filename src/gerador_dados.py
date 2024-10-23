from faker import Faker
import random

# Definindo o Faker para português
fake = Faker('pt_BR')

def gerar_inserts_jogos(qtd=10, proximos_ids=None):
    # Inicializa uma lista vazia para armazenar os comandos INSERT
    inserts = []

    # Itera 'qtd' vezes para gerar o número desejado de inserts
    # Ignorando a variável: O uso de _ sugere que você está ignorando o valor da variável que está sendo gerada pelo loop.
    for _ in range(qtd):  
        # Usar o próximo ID disponível da tabela Jogos
        id = proximos_ids["Jogos"]  
        
        # Gera um título aleatório com no máximo 20 caracteres
        titulo = fake.text(max_nb_chars=20)  
        
        # Gera um nome de desenvolvedor aleatório
        desenvolvedor = fake.company()  
        
        # Seleciona um gênero aleatório da lista
        genero = random.choice(['Ação', 'RPG', 'Estratégia', 'Esportes', 'Corrida','FPS'])  
        
        # Cria a instrução SQL para inserir um novo jogo com os dados gerados e adiciona à lista de inserts
        inserts.append(f"INSERT INTO Jogos (id, titulo, desenvolvedor, genero) VALUES ({id}, '{titulo}', '{desenvolvedor}', '{genero}');")  
        
        # Incrementa o próximo ID para o próximo jogo a ser gerado
        proximos_ids["Jogos"] += 1  
    
    # Retorna a lista de comandos INSERT gerados
    return inserts  


def gerar_inserts_usuarios(qtd=15, proximos_ids=None):
    inserts = []
    for _ in range(qtd):
        id = proximos_ids["Usuarios"]  # Usar o próximo ID disponível
        nome = fake.name()
        username = fake.user_name()
        email = fake.email()
        data_registro = fake.date_this_year()
        inserts.append(f"INSERT INTO Usuarios (id, nome, username, email, data_registro) VALUES ({id}, '{nome}', '{username}', '{email}', '{data_registro}');")
        proximos_ids["Usuarios"] += 1  # Incrementar o próximo ID
    return inserts

def gerar_inserts_transmissoes(qtd=30, proximos_ids=None):
    inserts = []
    for _ in range(qtd):
        id = proximos_ids["Transmissoes"]  # Usar o próximo ID disponível
        usuario_id = random.randint(1, proximos_ids["Usuarios"] - 1)  # Considerando a quantidade de usuários gerados
        jogo_id = random.randint(1, proximos_ids["Jogos"] - 1)  # Considerando a quantidade de jogos gerados
        data_transmissao = fake.date_time_this_year()
        visualizacoes = random.randint(0, 1000)
        inserts.append(f"INSERT INTO Transmissoes (id, usuario_id, jogo_id, data_transmissao, visualizacoes) VALUES ({id}, {usuario_id}, {jogo_id}, '{data_transmissao}', {visualizacoes});")
        proximos_ids["Transmissoes"] += 1  # Incrementar o próximo ID
    return inserts

def gerar_inserts_comentarios(qtd=50, proximos_ids=None):
    inserts = []
    for _ in range(qtd):
        id = proximos_ids["Comentarios"]  # Usar o próximo ID disponível
        transmissao_id = random.randint(1, proximos_ids["Transmissoes"] - 1)  # Considerando a quantidade de transmissões geradas
        usuario_id = random.randint(1, proximos_ids["Usuarios"] - 1)  # Considerando a quantidade de usuários gerados
        comentario = fake.sentence(nb_words=10)
        data_comentario = fake.date_time_this_year()
        inserts.append(f"INSERT INTO Comentarios (id, transmissao_id, usuario_id, comentario, data_comentario) VALUES ({id}, {transmissao_id}, {usuario_id}, '{comentario}', '{data_comentario}');")
        proximos_ids["Comentarios"] += 1  # Incrementar o próximo ID
    return inserts

def gerar_deletes(caminho):
    # Definindo as tabelas e a ordem correta para deletar
    tabelas = {
        "Comentarios": "DELETE FROM Comentarios;",
        "Transmissoes": "DELETE FROM Transmissoes;",
        "Usuarios": "DELETE FROM Usuarios;",
        "Jogos": "DELETE FROM Jogos;"
    }

    # Formatar o nome do arquivo de deletes
    nome_arquivo = caminho + 'deletes.sql'

    # Abrindo arquivo para escrita
    with open(nome_arquivo, 'w') as f:
        for tabela in tabelas:
            f.write(tabelas[tabela] + '\n')

    print("Arquivo de deletes gerado com sucesso!")
