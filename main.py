import urllib.request, json
print("Exemplo de IP: 8.8.8.8")
ip = input("Informe um IP:")

with urllib.request.urlopen(f"https://ipinfo.io/{ip}/json") as url:
    dados = json.loads(url.read().decode())

print('IP: ' + dados['ip'])
print('Nome da Host: ' + dados['hostname'])
print('Cidade: ' + dados['city'] + ' | Região: ' + dados['region'] + ' | País: ' + dados['country'])
print('Empresa Responsável: ' + dados['org'])
print('Endereço Postal: ' + dados['postal'])
print('TimeZone: ' + dados['timezone'])
