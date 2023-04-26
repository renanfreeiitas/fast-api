from fastapi import FastAPI

import fcntl

app = FastAPI()


@app.get('/msg')
async def message():
    return {"msg": "FastAPI na Geek University. by: Renan"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)