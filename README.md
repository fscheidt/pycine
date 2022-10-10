# Configuração do ambiente

- [Setup flask e virtual env](https://github.com/fscheidt/dev/blob/master/flask/setup-projeto-flask.md)

## Requirements.txt

Salvar as depêndencias (bibliotecas) instaladas no virtual env:

```bash
pip freeze > requirements.txt
```

Permite restaurar o ambiente virtual em outras máquinas/ambientes de desenvolvimento:
# git clone https://github.com/fscheidt/pycine

```bash
cd pycine
# quem fez clone:
# python3 -m venv env (root)

python3 -m venv env --without-pip --system-site-packages

source env/bin/activate
pip install -r requirements.txt
```
