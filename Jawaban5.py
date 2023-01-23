from fastapi import FastAPI
from database_connection import connection
from model.models import users as table
from user import User as orm

app = FastAPI()


@app.get("/users")
def read():
    result = connection.execute(table.select()).fetchall()
    
    return {
        "result": result
    }


@app.post('/users/insert')
def insert(user: orm):
    data = connection.execute(
        table
        .insert()
        .values(
            name=user.name,
            email=user.email
        )
    )

    return {
        "status": data.is_insert
    }


@app.put('/users/update/{id}')
async def update(id: int, user: orm):
    data = connection.execute(
        table
        .update()
        .values(
            name=user.name,
            email=user.email
        )
        .where(table.c.id == id)
    )

    if data:
        return {
            "status": True,
        }

    else:
        return {
            "status": False,
        }


@app.delete('/users/delete/{id}')
async def delete(id: int):
    data = connection.execute(
        table
        .delete()
        .where(table.c.id == id)
    )

    if data:
        return {
            "status": True,
        }

    else:
        return {
            "status": False,
        }


@app.get('/users/search/{name}')
async def search(name: str):
    data = connection.execute(
        table
        .select()
        .where(table.c.name.like('%'+name+'%'))
    ).fetchall()

    return {
        "status": True,
        "data": data
    }
