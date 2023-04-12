from flask import Flask, render_template
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1=Jogo('TETRIS', 'Puzzle','Atari')
    jogo2=Jogo('GOD OF WAR', 'Rack n Slash', 'PS2')
    jogo3=Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

app.run(host='localhost', port=8080)
