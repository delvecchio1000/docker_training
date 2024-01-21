# docker_training

1) Em qualquer lugar de sua máquina, crie uma pasta com o nome do seu projeto

2) Usar seu editor de código (VScode)

3) No VScode, entrar na pasta recém criada

4) Inicializar o git ==> "git init"

5) Criar um arquivo com o nome de ".gitignore"

6) Incluir a seguinte linha dentro do arquivo .gitignore: "**/__pycache__"

7) Dependência do ambiente virtual (só se não estiver instalado):
==> "sudo apt install python3-venv"

8) Criar o ambiente virtual (Utilizar o Terminal do VScode)
	a) ==> "python -m venv nome_do_projeto_env" 
	b) ==> ".\nome_do_projeto_env\Script\Activate.ps1"

9) Incluir o ambiente virtual dentro do arquivo .gitignore: "nome_do_projeto_env"

10) Certificar-se de qual interpretador de python está sendo utilizado:
	a) No VScode: Ctrl + shift + p / Python: Select Interpreter
	b) escolher o interpretador python do ambiente virtual

11) Instalar o Flask: ==> "pip install Flask"

12) Adcionar ao git: 
	a) ==> "git add ."
	b) ==> "git commit -m 'first commit'"

13) Para evitar a constante utilização do "pip freeze > requirements.txt":
	a) Usaremos a ferramenta "pre-commit"
	b) ==> "pip install pre-commit"
	c) Adcionar um arquivo .yaml, conforme a documentação do pre-commit
		a) ==> ".pre-commit-config.yaml"
		b) Como base, utilize o seguinte código a ser adiconado ao yaml:
			repos:
			-   repo: local
    			hooks:
      			- id: requirements
        			name: requirements
        			entry: bash -c 'venv/bin/pip3 freeze > requirements.txt; git add requirements.txt'
        			language: system
        			pass_filenames: false
        			stages: [commit]

14) Instalar SQLAlchemy: ==> "pip install SQLAlchemy"

15) Intalar o pre-commit: ==> "pre-commit install"

16) Adcionar ao git: 
	a) ==> "git add ."
	b) ==> "git commit -m 'commit 02'"

17) VEJA QUE, APÓS O COMMIT, O ARQUIVO REQUIREMENTS.TXT FOI ATUALIZADO AUTOMATICAMENTE, GRAÇAS AO PRE-COMMIT.

18) Criar um arquivo "run.py" para rodar sua aplicação

19) Dentro de run.py cole o seguinte código:
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
  return "Olá, estou na aplicação setada"

20) Para rodar o projeto Flask:
	a) ==> "export FLASK_APP=run.py"
	b) ==> "flask run"

21) Crtl + c para interromper o serviço

22) Adcionar ao git: 
	a) ==> "git add ."
	b) ==> "git commit -m 'commit 03'"

