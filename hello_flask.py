from flask import Flask
app=Flask(__name__)
@app.route("/")   #annotation
def F()->str:
    return "Hello World"
@app.route("/categories")   #writing route
def F2()->str:
    return "Hello Categories"
app.run()  