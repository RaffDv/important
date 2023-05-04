import csv
import mysql.connector
import time
import ipaddress


def calcMask(ip):
    rede = ipaddress.IPv4Network(ip)
    return (str(rede.network_address), str(rede.broadcast_address))


# Estabeleça a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="authentydev07",
    password="1EowntHhHV9kyiUgkqN9WRtXu",
    database="authentydev07"
)

# Crie um cursor para executar comandos SQL
cursor = conexao.cursor()

# Defina a consulta SQL com a sintaxe do multi-value insert
sql = "INSERT INTO aux_geolite2CityLocationsEn (  geoname_id,locale_code,continent_code,continent_name,country_iso_code,country_name,subdivision_1_iso_code,subdivision_1_name,subdivision_2_iso_code,subdivision_2_name,city_name,metro_code,is_in_european_union) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"

# Abra o arquivo CSV com os dados a serem inseridos
with open('inputV2.csv') as arquivo:
    leitor_csv = csv.reader(arquivo)
    valores = []
    for linha in leitor_csv:
        valores.append(linha)
        cursor.execute(sql, valores)
        conexao.commit()
        valores = []

    if valores:
        cursor.executemany(sql, valores)
        conexao.commit()
# Feche o cursor e a conexão
cursor.close()
conexao.close()
