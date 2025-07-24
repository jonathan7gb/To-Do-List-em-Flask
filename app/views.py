from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import tarefaForm
from app.models import Tarefa

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/tarefa/', methods=['GET', 'POST'])
def tarefas():
    form = tarefaForm()
    context = {}

    pesquisa = request.args.get('pesquisa', '')

    if form.validate_on_submit():
        form.save()
    
    dados = Tarefa.query.order_by('data_envio')
    
    if pesquisa != '':
        dados = dados.filter(Tarefa.titulo.ilike(f'%{pesquisa}%'))

    status_dict = {
        'a_fazer': 'A Fazer',
        'em_andamento': 'Em Andamento',
        'concluido': 'Concluído'
    }
    context = {'dados': dados.all()}
    return render_template('tarefas.html', context=context, form=form, status_dict = status_dict)


@app.route('/tarefa/lista')
def listaTarefas():
    dados2 = Tarefa.query.order_by('data_envio')

    pesquisa2 = request.args.get('pesquisa2', '')
    ordenar = request.args.get('ordenar', '')
    status = request.args.get('status', '')
    
    if pesquisa2 != '':
        dados2 = dados2.filter(Tarefa.titulo.ilike(f'%{pesquisa2}%'))

    if status and status != 'Todos':
        dados2 = dados2.filter(Tarefa.status == status)

    if ordenar == 'data_desc':
        dados2 = dados2.order_by(Tarefa.data_envio.desc())
    elif ordenar == 'data_asc':
        dados2 = dados2.order_by(Tarefa.data_envio.asc())
    elif ordenar == 'titulo_az':
        dados2 = dados2.order_by(Tarefa.titulo.asc())
    elif ordenar == 'titulo_za':
        dados2 = dados2.order_by(Tarefa.titulo.desc())
    else:
        dados2 = dados2.order_by(Tarefa.data_envio.desc())
    
    status_dict2 = {
            'a_fazer': 'A Fazer',
            'em_andamento': 'Em Andamento',
            'concluido': 'Concluído'
        }

    context2 = {'dados2' : dados2.all()}
    return render_template('tarefas_lista.html', context2=context2, status_dict2=status_dict2, status=status, ordenar=ordenar, pesquisa2=pesquisa2)