from flask import Flask

@app.route(/user/<name>)
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)