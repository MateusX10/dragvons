from flask import Flask, render_template 

app = Flask(__name__)



@app.route("/") 
def homepage():
    return render_template("index.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def about_us():
    return render_template("sobre.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/usuarios")
def buscar_usuarios():
    return render_template("buscar_usuarios.html")
#colocar o site no ar

if __name__ == "__main__":
    app.run(debug=True) 