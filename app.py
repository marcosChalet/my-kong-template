import requests
import json

KONG_ADMIN_URL = 'http://localhost:8001'
SERVICES_JSON_NAME = 'conf.json'
PLUGINS_JSON_NAME = 'plugins.json'
CONSUMER_TEST_NAME = 'teste'

def add_service(service_data):
  response = requests.post(f'{KONG_ADMIN_URL}/services/', json=service_data)
  if response.status_code == 201:
    print(f'Serviço {service_data["name"]} adicionado com sucesso.')
    return response.json()
  else:
    print(f'Falha ao adicionar serviço {service_data["name"]}. Status code: {response.status_code}')
    return None

def add_route(service_id, route_data):
  response = requests.post(f'{KONG_ADMIN_URL}/services/{service_id}/routes', json=route_data)
  if response.status_code == 201:
    print(f'Rota {route_data["name"]} adicionada para o serviço {service_id}.')
  else:
    print(f'Falha ao adicionar rota {route_data["name"]} para o serviço {service_id}. Status code: {response.status_code}')

def add_plugin(plugin_data):
    response = requests.post(f'{KONG_ADMIN_URL}/plugins/', json=plugin_data)
    if response.status_code == 201:
      print(f'Plugin {plugin_data["name"]} adicionado com sucesso.')
    else:
      print(f'Falha ao adicionar plugin {plugin_data["name"]}. Status code: {response.status_code}')

def create_test_consumer():
    consumer_data = {
      "username": CONSUMER_TEST_NAME
    }
    response = requests.post(f'{KONG_ADMIN_URL}/consumers', json=consumer_data)
    if response.status_code == 201:
        print(f'Consumidor de teste criado com sucesso.')

        response = requests.post(f'{KONG_ADMIN_URL}/consumers/{CONSUMER_TEST_NAME}/key-auth')
        if response.status_code == 201:
          print(f'Credenciais de chave da API criadas com sucesso para o consumidor de teste.')
        else:
          print(f'Falha ao criar as credenciais de chave da API para o consumidor de teste. Status code: {response.status_code}')
    else:
        print(f'Falha ao criar consumidor de teste. Status code: {response.status_code}')


with open(SERVICES_JSON_NAME) as json_file:
  data = json.load(json_file)

with open(PLUGINS_JSON_NAME) as plugins_json_file:
  plugins_data = json.load(plugins_json_file)

create_test_consumer()

for item in data:
  service_data = item["service"]
  service_info = add_service(service_data)

  if service_info:
    service_id = service_info['id']
    routes = item.get("routes", [])
    for route in routes:
      add_route(service_id, route)

for plugin_data in plugins_data:
  add_plugin(plugin_data["plugin"])