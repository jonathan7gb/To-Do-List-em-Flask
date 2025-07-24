from app import app
from app.models import db, Tarefa 
from datetime import datetime

with app.app_context():
    tarefas = [
         Tarefa(titulo='Criar painel de administrador', descricao='Montar uma interface para admins verem todas as tarefas e usuários.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Adicionar confirmação de exclusão', descricao='Criar modal para confirmar antes de apagar uma tarefa.', status='em_andamento', data_envio=datetime.now()),
    Tarefa(titulo='Subir banco na nuvem', descricao='Migrar o banco local para um PostgreSQL no Railway.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Fazer testes automatizados', descricao='Criar testes com pytest para rotas e funções críticas.', status='concluido', data_envio=datetime.now()),
    Tarefa(titulo='Estilizar mensagens de erro', descricao='Deixar os alertas de erro mais bonitos e visíveis.', status='em_andamento', data_envio=datetime.now()),
    Tarefa(titulo='Configurar variáveis de ambiente', descricao='Tirar dados sensíveis do código e usar .env.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Criar card para tarefa urgente', descricao='Destaque visual nas tarefas com prazo curto.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Implementar dark mode', descricao='Deixar o layout alternável entre claro e escuro.', status='em_andamento', data_envio=datetime.now()),
    Tarefa(titulo='Melhorar acessibilidade', descricao='Adicionar atributos ARIA e navegação por teclado.', status='concluido', data_envio=datetime.now()),
    Tarefa(titulo='Gerar relatório de tarefas', descricao='Exportar tarefas em PDF com filtro por status.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Criar animações com CSS', descricao='Dar mais vida aos botões e cards do sistema.', status='em_andamento', data_envio=datetime.now()),
    Tarefa(titulo='Fazer deploy no Heroku', descricao='Testar como fica o back-end rodando no Heroku.', status='concluido', data_envio=datetime.now()),
    Tarefa(titulo='Adicionar autenticação por token', descricao='Usar JWT para proteger rotas da API.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Criar loading ao buscar tarefas', descricao='Mostrar um spinner enquanto os dados são carregados.', status='em_andamento', data_envio=datetime.now()),
    Tarefa(titulo='Criar função de reset de senha', descricao='Enviar e-mail com link de redefinição.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Revisar textos da interface', descricao='Melhorar clareza e padronização das mensagens.', status='concluido', data_envio=datetime.now()),
    Tarefa(titulo='Fazer benchmark do back-end', descricao='Ver tempos de resposta e gargalos das rotas.', status='em_andamento', data_envio=datetime.now()),
    Tarefa(titulo='Substituir ícones por SVGs', descricao='Trocar PNGs por ícones em vetor pra otimizar.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Adicionar favoritos nas tarefas', descricao='Permitir marcar tarefas importantes com estrela.', status='a_fazer', data_envio=datetime.now()),
    Tarefa(titulo='Criar dashboard com gráficos', descricao='Mostrar tarefas por status em gráficos de pizza.', status='em_andamento', data_envio=datetime.now()),
    ]

    db.session.add_all(tarefas)
    db.session.commit()
    print("Banco populado com sucesso! 🔥")