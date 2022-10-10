from fastapi import FastApi

app = FastApi()
# fornecido um id, retorno o 
# json do filme
# /movie/1
@app.get("/movie")
async def get_movie():
    return {"title": "Avatar"}

# pip install -r requirements.txt
# source env/
# pip install fastapi uvicorn
