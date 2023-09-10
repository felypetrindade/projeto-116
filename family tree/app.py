# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "alex" # escreva seu nome
    idade = "12" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
def pai():

    nome = "vitor" # escreva seu nome
    idade = "40" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)


# defina a rota para a página da mãe
def mae():

    nome = "erica" # escreva seu nome
    idade = "37" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# defina a rota para a página do amigo
def home():

    nome = "pedro" # escreva seu nome
    idade = "12" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
