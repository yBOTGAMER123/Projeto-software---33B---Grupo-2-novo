🇵🇹 Português — Pronto para copiar/colar
Pré-requisitos

Python 3.10+ instalado

Arquivo main.py na raiz com app = FastAPI()

Exemplo mínimo (main.py):

from fastapi import FastAPI

app = FastAPI(title="My API")

@app.get("/status")
def health():
return {"status": "ok"}

macOS / Linux
# 1) Entrar na pasta do projeto
cd API

# 2) Criar/ativar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3) Instalar dependências
pip install --upgrade pip
pip install fastapi "uvicorn[standard]"

# 4) Iniciar o servidor
uvicorn main:app --reload

Windows (PowerShell)
# 1) Entrar na pasta do projeto
cd API

# 2) Criar/ativar ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3) Instalar dependências
python -m pip install --upgrade pip
pip install fastapi "uvicorn[standard]"

# 4) Iniciar o servidor
uvicorn main:app --reload

Teste rápido

Swagger UI: http://127.0.0.1:8000/docs

Verificar saúde:

# macOS/Linux
curl http://127.0.0.1:8000/status

# Windows
Invoke-RestMethod http://127.0.0.1:8000/status

Solução de problemas (rápido)

ModuleNotFoundError: No module named 'app' → use uvicorn main:app --reload (sem pasta app, aponte para o arquivo).

Porta ocupada → uvicorn main:app --reload --port 8001

Ambiente virtual não ativa no PowerShell → execute como Admin:
Set-ExecutionPolicy RemoteSigned e depois ative novamente.

🇬🇧 English — Ready to copy/paste
Prerequisites

Python 3.10+ installed

main.py at project root with app = FastAPI()

Minimal example (main.py):

from fastapi import FastAPI

app = FastAPI(title="My API")

@app.get("/status")
def health():
return {"status": "ok"}

macOS / Linux
# 1) Go to project folder
cd API

# 2) Create/activate virtual env
python3 -m venv .venv
source .venv/bin/activate

# 3) Install deps
pip install --upgrade pip
pip install fastapi "uvicorn[standard]"

# 4) Run the server
uvicorn main:app --reload

Windows (PowerShell)
# 1) Go to project folder
cd API

# 2) Create/activate virtual env
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3) Install deps
python -m pip install --upgrade pip
pip install fastapi "uvicorn[standard]"

# 4) Run the server
uvicorn main:app --reload

Quick test

Swagger UI: http://127.0.0.1:8000/docs

Health check:

# macOS/Linux
curl http://127.0.0.1:8000/status

# Windows
Invoke-RestMethod http://127.0.0.1:8000/status

Quick troubleshooting

ModuleNotFoundError: No module named 'app' → use uvicorn main:app --reload (no app folder, point to the file).

Port already in use → uvicorn main:app --reload --port 8001

Venv won’t activate in PowerShell → run as Admin:
Set-ExecutionPolicy RemoteSigned, then activate again.