from app import app


@app.rote('/')
def index():
    return 'hello'
