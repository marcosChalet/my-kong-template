# Instruções para rodar o projeto

Este guia fornece um conjunto de configurações usuais para a utilização do Kong.

## Requisitos
- OpenSSL
- Docker

## Passos para usar
1. Entre na pasta para certificados
```
cd certs
```

2. Gere uma chave privada

```
openssl genpkey -algorithm RSA -out localhost.key
```

3. Gere um certificado autoassinado

```
openssl req -new -x509 -key localhost.key -out localhost.crt -days 365
```

4. Rode o projeto

```
docker compose up -d
```
