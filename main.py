from fastapi import FastAPI


app = FastAPI()

@app.get('/home')
def home():
    return "Hello world!!"


@app.get('/about')
def about():
    return "This is the about page"
