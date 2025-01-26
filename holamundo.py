from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    contenidoHtml = "<h1>Hola Mundo</h1>"
    return render_template_string(contenidoHtml)

if __name__ == '__main__':
    app.run(debug=True)