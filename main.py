from fastapi import FastAPI

app = FastAPI()
# fornecido um id, retorno o 
# json do filme
# /movie/1
@app.get("/movie")
async def get_movie():
    return {"title": "Avatar"}

# uvicorn main:app --reload

# pip install -r requirements.txt
# source env/
# pip install fastapi uvicorn
