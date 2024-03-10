from fastapi import FastAPI


app = FastAPI()

@app.get('/home')
def home():
    return "Hello world!!"


@app.get('/about')
def about():
    return "This is the about page"


@app.get('/contact-us')
def about():
    return "Mobile Number: 9004008904, email: amanupadhyay32@gmail.com"