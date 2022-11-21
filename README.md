# Configuração do ambiente

- [Setup flask e virtual env](https://github.com/fscheidt/dev/blob/master/flask/setup-projeto-flask.md)

## Requirements.txt

Salvar as depêndencias (bibliotecas) instaladas no virtual env:

```bash
pip freeze > requirements.txt
```

Permite restaurar o ambiente virtual em outras máquinas/ambientes de desenvolvimento

---

### git clone https://github.com/fscheidt/pycine

```bash
cd pycine
# quem fez clone:
# python3 -m venv env (root)

python3 -m venv env --without-pip --system-site-packages

source env/bin/activate
pip install -r requirements.txt
```

## ModuleNotFound

Se ocorrer o erro "ModuleNotFound", abrir o terminal (na mesma pasta do projeto) e rodar o comando:

```bash
export PYTHONPATH=.
```

---

## ➭ 21/11



---

## ➭ 07/11

### Exemplos da api:

https://developers.themoviedb.org/3/getting-started/introduction

### Teste da api

Formato da url:
> https://api.themoviedb.org/3/discover/movie?api_key=CHAVE&sort_by=popularity.desc

Testar o endpoint *discover* com sort by "media dos votos"

> https://api.themoviedb.org/3/discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc&api_key=d1da20fbfa65312b857fb7b517bf855c

### Filmes mais populares: 
Request:
> https://api.themoviedb.org/3/discover/movie/?api_key=d1da20fbfa65312b857fb7b517bf855c&certification_country=US&certification=R&sort_by=vote_count.desc

Resultado:
- 1º Deadpool, 
- 2º Fight club


### Descobrir filmes populares por genero
Teste: gênero == drama

- Fight club
- Django

> https://api.themoviedb.org/3/discover/movie/?api_key=d1da20fbfa65312b857fb7b517bf855c&certification_country=US&certification=R&sort_by=vote_count.desc&with_genres=18

### Obter dados de um filme

> https://api.themoviedb.org/3/movie/293660?api_key=d1da20fbfa65312b857fb7b517bf855c&language=en-US


### 🔥 Atividade
1. Obter informações de um artista (person)
> testar: Arnold Schwarzenegger

2. Obter elenco do filme: **"Deadpool"**
    - artistas associados ao filme.

