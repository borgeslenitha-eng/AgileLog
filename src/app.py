from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO_TAREFAS = os.path.join(os.path.dirname(__file__), 'tarefas.json')

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    tarefas = carregar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefas = carregar_tarefas()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": request.form['titulo'],
        "status": "A Fazer"
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/atualizar/<int:id>/<string:status>')
def atualizar(id, status):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id:
            t["status"] = status
            break
    salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def excluir(id):
    tarefas = [t for t in carregar_tarefas() if t["id"] != id]
    salvar_tarefas(tarefas)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
