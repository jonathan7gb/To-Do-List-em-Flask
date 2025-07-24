from app import app
from app.models import db, Tarefa 
from datetime import datetime

with app.app_context():
    tarefas = [
        Tarefa(titulo='Documentar sistema de avisos', descricao='Criar uma documentação explicando como o sistema de avisos funciona.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Criar layout no Figma', descricao='Desenhar as telas principais no Figma com responsividade.', status='em_andamento', data_envio=datetime.now()),
        Tarefa(titulo='Testar responsividade', descricao='Verificar como o site se comporta em celulares e tablets.', status='concluido', data_envio=datetime.now()),
        Tarefa(titulo='Corrigir bug no filtro de status', descricao='Ajustar a lógica que filtra tarefas por status.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Enviar para revisão do professor', descricao='Mandar o projeto final para validação e feedback.', status='concluido', data_envio=datetime.now()),
        Tarefa(titulo='Integrar back-end Java com HTML', descricao='Conectar as rotas Java com os formulários HTML.', status='em_andamento', data_envio=datetime.now()),
        Tarefa(titulo='Criar README do projeto', descricao='Escrever instruções e descrição do projeto.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Organizar pastas no GitHub', descricao='Estruturar o repositório com pastas claras e separadas.', status='concluido', data_envio=datetime.now()),
        Tarefa(titulo='Pesquisar deploy no Render', descricao='Estudar como fazer deploy de um Flask no Render.', status='em_andamento', data_envio=datetime.now()),
        Tarefa(titulo='Refatorar código duplicado', descricao='Limpar repetições e melhorar legibilidade do código.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Criar tela de login', descricao='Fazer o HTML + CSS da tela de login do sistema.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Melhorar usabilidade mobile', descricao='Ajustar interações e tamanho de elementos no mobile.', status='em_andamento', data_envio=datetime.now()),
        Tarefa(titulo='Fazer deploy no Vercel', descricao='Subir versão estática do front no Vercel pra testes.', status='concluido', data_envio=datetime.now()),
        Tarefa(titulo='Implementar botão de logout', descricao='Adicionar botão funcional de logout com redirecionamento.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Reunião com equipe de QA', descricao='Discutir testes e bugs encontrados.', status='em_andamento', data_envio=datetime.now()),
        Tarefa(titulo='Testar integração com API externa', descricao='Ver se o sistema puxa dados corretamente da API.', status='concluido', data_envio=datetime.now()),
        Tarefa(titulo='Criar validador de formulário', descricao='Validar campos obrigatórios no front e no back.', status='a_fazer', data_envio=datetime.now()),
        Tarefa(titulo='Corrigir layout quebrado no Safari', descricao='Verificar e consertar CSS que não funciona no Safari.', status='em_andamento', data_envio=datetime.now()),
        Tarefa(titulo='Finalizar documentação técnica', descricao='Fechar todos os documentos técnicos do projeto.', status='concluido', data_envio=datetime.now()),
        Tarefa(titulo='Publicar versão 1.0', descricao='Fazer release final com todas as funcionalidades prontas.', status='a_fazer', data_envio=datetime.now()),
    ]

    db.session.add_all(tarefas)
    db.session.commit()
    print("Banco populado com sucesso! 🔥")