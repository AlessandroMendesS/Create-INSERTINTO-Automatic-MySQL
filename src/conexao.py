import mysql.connector
from mysql.connector import Error

def obter_proximo_id():
    # Configurações do banco de dados
    host = 'localhost'  # Ou o endereço do seu servidor MySQL
    user = 'root' # Altere para seu usuário MySQL
    password = 'aluno'# Altere para sua senha MySQL
    database = 'PlataformaStreamingJogos'# Altere para o nome do seu banco de dados

    try:
        # Conectar ao banco de dados MySQL
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Dicionário para armazenar os próximos IDs disponíveis
            proximos_ids = {}

            # Tabelas que queremos consultar
            tabelas = ["Jogos", "Usuarios", "Transmissoes", "Comentarios"]

            for tabela in tabelas:
                # Executar SELECT MAX(id) para cada tabela
                cursor.execute(f"SELECT MAX(id) FROM {tabela};")
                resultado = cursor.fetchone()
                
                # Determinar o próximo ID disponível
                max_id = resultado[0] if resultado[0] is not None else 0
                proximos_ids[tabela] = max_id + 1

            # Fechar o cursor
            cursor.close()

            return proximos_ids

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    finally:
        if conn.is_connected():
            conn.close()