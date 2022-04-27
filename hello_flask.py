from flask import Flask,render_template,request
from vsearch import search4letters

app=Flask(__name__)




# @app.route("/categories")   #writing route
# def F2()->str:
#     return "Hello Categories"

@app.route("/search4",methods=["POST"]) 
def do_search()->"html":
    phrase=request.form["phrase"]
    letters=request.form["letters"]
    title="Welcome to the search4letters website"

    res= str(search4letters(phrase,letters))
    print(res)
    return render_template("results.html",
    the_title=title,
    the_phrase=phrase,
    the_letters=letters,
    the_result=res
    )
@app.route("/")   #annotation
@app.route("/entry") 
def entry_page()->"html":
    title="Welcome to the search4letters website!"
    return render_template("entry.html",the_title=title)    

app.run(debug=True)