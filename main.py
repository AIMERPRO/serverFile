from typing import Any

import uvicorn
from fastapi import FastAPI, Query, Form, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
@app.post("/")
async def index(data: Any = Body()):
    data = str(data)
    with open("data.txt", "w") as file:
        file.write(data)
    return "ok"

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.12.12.12",
        port=8881,
        reload=True
    )
