from fastapi import FastAPI

app = FastAPI()#instance creation

@app.get('/')
def index():
    return {"data":{"course":"distributed systems"}}

@app.get('/about')
def about():
    return {'data':{"This is the About page"}}


#Import, Instance, Function, Decorate to get an API