import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="########",  # ou outro usuário
    password="############",  # sua senha
    database="trackmydelivery"
)
cursor = conn.cursor()

# Inicializa o Faker
fake = Faker('pt_BR')

# Lista de cidades e UFs
cidades = [
    ("São Paulo", "SP", -23.5505, -46.6333),
    ("Rio de Janeiro", "RJ", -22.9068, -43.1729),
    ("Belo Horizonte", "MG", -19.9167, -43.9345),
    ("Porto Alegre", "RS", -30.0346, -51.2177),
    ("Curitiba", "PR", -25.4284, -49.2733),
    ("Salvador", "BA", -12.9714, -38.5014)
]

# Status possíveis
status_entrega = [
    "Pedido Recebido",
    "Em Separação",
    "Saiu para Entrega",
    "Entregue",
    "Entrega Falhou"
]

# Lista de transportadoras fictícias
transportadoras = [
    "TransBrasil", 
    "LogExpress", 
    "ViaRápida", 
    "CargasNorte", 
    "FreteFácil"
]

# Função para gerar entregas
def gerar_entregas(qtd=100):
    for _ in range(qtd):
        pedido_id = fake.uuid4()[:8].upper()
        cliente = fake.name()
        status = random.choice(status_entrega)
        cidade, uf, lat, long = random.choice(cidades)
        transportadora = random.choice(transportadoras)  # <<<<< NOVO AQUI

        # Data aleatória
        dias_atras = random.randint(0, 30)
        data_entrega = datetime.now() - timedelta(days=dias_atras)
        atualizado_em = datetime.now()

        # Inserção com transportadora
        cursor.execute("""
            INSERT INTO entregas 
            (pedido_id, cliente, status, data_entrega, latitude, longitude, cidade, uf, atualizado_em, transportadora)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (pedido_id, cliente, status, data_entrega.date(), lat, long, cidade, uf, atualizado_em, transportadora))

    conn.commit()
    print(f"{qtd} entregas geradas com sucesso!")

# Executar a função
gerar_entregas(200)

# Fechar conexões
cursor.close()
conn.close()
