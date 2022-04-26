from flask import Flask
from vsearch import search4letters

app=Flask(__name__)

@app.route("/")   #annotation
def F()->str:
    return "Hello World"

# @app.route("/categories")   #writing route
# def F2()->str:
#     return "Hello Categories"

@app.route("/search4") 
def do_search()->str:
    res= str(search4letters("bir phrase gönderiyoruz","aeiöuüı"))
    print(res)
    return res




app.run()