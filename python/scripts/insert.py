import csv
import mysql.connector
import time
import ipaddress


def calcMask(ip):
    rede = ipaddress.IPv4Network(ip)
    return (str(rede.network_address), str(rede.broadcast_address))


# Estabeleça a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="192.168.0.15",
    user="root",
    password="",
    database=""
)

# Crie um cursor para executar comandos SQL
cursor = conexao.cursor()

sql = "INSERT INTO aux_IPv4Blocks (network, geoname_id, registered_country_geoname_id, represented_country_geoname_id, is_anonymous_proxy, is_satellite_provider, postal_code, latitude, longitude, accuracy_radius,network_min,network_max) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, INET_ATON(%s), INET_ATON(%s))"

# Abra o arquivo CSV com os dados a serem inseridos
with open('input.csv') as arquivo:
    leitor_csv = csv.reader(arquivo)
    inicio_total = time.time()
    inicio = time.time()

    contador_linhas = 0
    valores = []
    for linha in leitor_csv:
        ip = linha[0]
        rede_min, rede_max = calcMask(ip)
        valores.append(tuple(linha + [rede_min, rede_max]))
        contador_linhas += 1

        if contador_linhas == 100000:
            cursor.executemany(sql, valores)
            conexao.commit()
            tempo_total = time.time() - inicio
            print(
                f"A inserção de {len(valores)} linhas demorou {tempo_total:.2f} segundos.")
            valores = []
            inicio = time.time()
            contador_linhas = 0

    if valores:
        cursor.executemany(sql, valores)
        conexao.commit()

tempo_total = time.time() - inicio_total
print(f"A inserção de todas as linhas demorou {tempo_total:.2f} segundos.")

# Feche o cursor e a conexão
cursor.close()
conexao.close()
