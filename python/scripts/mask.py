import ipaddress

# Endereço IP da rede e máscara de sub-rede (CIDR)
endereco_rede = '223.255.255.0/24'

# Converter o endereço de rede em um objeto da classe IPv4Network
rede = ipaddress.IPv4Network(endereco_rede)

# Endereço IP inicial da rede
endereco_inicial = str(rede[0])

# Endereço IP final da rede
endereco_final = str(rede[-1])

# Exibir o resultado
print(f'Endereço inicial da rede: {endereco_inicial}')
print(f'Endereço final da rede: {endereco_final}')
