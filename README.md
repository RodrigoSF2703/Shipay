# API REST — Desafio Técnico Shipay

## 📖 Sobre
Esta API foi desenvolvida como parte de um desafio técnico, com o objetivo de demonstrar boas práticas de engenharia de software, separação de responsabilidades, manutenibilidade e clareza de execução.

A aplicação expõe endpoints REST para:

- Criação de usuários

- Consulta de papéis (roles) de usuários

O projeto foi estruturado utilizando FastAPI, SQLAlchemy assíncrono e PostgreSQL, com suporte a execução local via Docker.
 
---

## 👥 Autor 
 | Nome                         | Função               |
|------------------------------|----------------------|
| Rodrigo de Souza Francisco   | Desenvolvedor Backend  |


---

## 🚀 Tecnologias utilizadas
- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy 2.0 (Async)
- Pydantic
- PostgreSQL 15
- Passlib + Bcrypt (hash de senha)
- Docker
- Docker Compose

---

## 📦 Estrutura do Projeto

```
app/
├── api/
│   └── v1/
│       ├── routes_users.py
│       └── routes_roles.py
├── core/
│   ├── config.py
│   ├── database.py
│   ├── init_db.py
│   ├── security.py
│   └── seed.py
├── models/
│   ├── base.py
│   ├── user.py
│   ├── user_claim.py
│   ├── role.py
│   └── claim.py
├── repositories/
│   ├── user_repository.py
│   └── role_repository.py
├── services/
│   ├── user_service.py
│   └── role_service.py
├── schemas/
│   ├── user.py
│   └── role.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── main.py
├── requirements.txt
├── .env
└── README.md

```
### Observações:
- repositories: acesso a dados
- services: regras de negócio
- schemas: validação e contratos da API
- models: mapeamento ORM
- api: definição das rotas


---

## 🛠 Execução do projeto em ambiente local
### Pré-requisitos
- Docker
- Docker Compose

### 🔑 Configuração das variáveis de ambiente

Crie um arquivo .env na raiz do projeto:
```
DATABASE_URL=postgresql+asyncpg://shipay_user:shipay_pass@db:5432/shipay
SEED_DATABASE=true
```

### ▶️ Subir a aplicação localmente
**Dentro do diretorio docker, execute:**
```
docker compose up --build
```

Após a inicialização:

API disponível em:
http://localhost:8000

Documentação automática (Swagger):
http://localhost:8000/docs


## Deploy em produção (Google Cloud Run)
A aplicação é containerizada e pode ser implantada em ambientes serverless, como o Google Cloud Run.
Em produção, não deve ser utilizado Docker Compose. O serviço deve se conectar a um banco de dados PostgreSQL gerenciado (ex: Cloud SQL, RDS, Supabase, Neon).

- Build da imagem
```
docker build -t shipay-api .
```
- Configurar projeto GCP
```
gcloud config set project nomeprojeto
```
- Tag da imagem
```
docker tag shipay-api gcr.io/nomeprojeto/shipay-api:latest
```
- Enviar imagem para o Container Registry
```
docker push gcr.io/nomeprojeto/shipay-api:latest
```
- Deploy no Cloud Run
```
gcloud run deploy shipay-api --image gcr.io/nomeprojeto/shipay-api:latest --platform managed --allow-unauthenticated --set-env-vars "SEED_DATABASE=false,DATABASE_URL=postgresql+asyncpg://shipay_user:shipay_pass@host_do_banco:5432/shipay"
```
As variáveis sensíveis devem ser configuradas diretamente no provedor de cloud e nunca versionadas.
