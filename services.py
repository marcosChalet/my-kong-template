import requests
import json

KONG_ADMIN_URL = 'http://localhost:8001'
JSON_NAME = 'conf.json'

def add_service(service_data):
  response = requests.post(f'{KONG_ADMIN_URL}/services/', json=service_data)
  if response.status_code == 201:
    print(f'Serviço {service_data["name"]} adicionado com sucesso.')
    return response.json()
  else:
    print(f'Falha ao adicionar serviço {service_data["name"]}. Status code: {response.status_code}')
    return None

def add_route(service_id, route_path):
  route_data = {
    "paths": [route_path],
    "service": {"id": service_id}
  }
  response = requests.post(f'{KONG_ADMIN_URL}/routes/', json=route_data)
  if response.status_code == 201:
    print(f'Rota adicionada para o serviço {service_id}.')
  else:
    print(f'Falha ao adicionar rota para o serviço {service_id}. Status code: {response.status_code}')

with open(f'{JSON_NAME}') as json_file:
  data = json.load(json_file)

for item in data:
  service_data = item["service"]
  service_info = add_service(service_data)

  if service_info:
    service_id = service_info['id']
    routes = item.get("routes", [])
    for route in routes:
      add_route(service_id, route)