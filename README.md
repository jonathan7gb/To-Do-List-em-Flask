# 📝 To-Do List em Flask

Este é um projeto de uma lista de tarefas (To-Do List) desenvolvido com **Flask** e **SQLite**, com um front simples e funcional em HTML e CSS. É ideal pra praticar CRUD, filtros, ordenações e manipulação de rotas com Flask.

## 📌 Funcionalidades

- ✅ Adicionar tarefas com título, descrição e status
- 📋 Visualizar todas as tarefas com filtros por status, pesquisa e ordenação
- 📝 Editar tarefas existentes **// Melhoria Futura**
- ❌ Deletar tarefas **// Melhoria Futura**
- 🔎 Filtrar por status (A Fazer, Em Andamento, Concluído)
- 🔠 Ordenar por título (A-Z, Z-A) e por data (mais recente/mais antiga)

## 🛠️ Tecnologias Usadas
- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite
- HTML
- CSS3 

## 🎨 Style Guide
- Tipografia -> Fonte usada: Space Grotesk (Google Fonts)
- Cores (Color Hunt)  -> Primária: #3E5F44 
         -> Secundária: #5E936C
         -> Background Color: #eefde3 

## 🚀 Como executar o projeto

1. **Clone o repositório no Git Bash**
   ```bash
   git clone https://github.com/jonathan7gb/To-Do-List-em-Flask.git
   cd To-Do-List-em-Flask
   ```
   
2. **Crie e ative um ambiente virtual**
   ```bash
    python -m venv venv
    venv\Scripts\activate    # no Windows
    source venv/bin/activate # no Linux/Mac
   ```
   
3. **Instale as dependências**
   ```bash
    pip install -r requirements.txt
   ```
   
4. **Configure o banco de dados**
   ```bash
    flask db init
    flask db migrate -m "Criação inicial"
    flask db upgrade
   ```
   
5. **Execute o arquivo 'main.py'**
   ```bash
    python main.py
   ```
   
6. **Acesse no navegador**
   ```bash
    http://127.0.0.1:5000/
   ```

## Telas do Site
- Tela Inicial
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/cb8c21d5-d85b-4398-8a78-1f5fe3aec8b6" />

- Tela de Cadastro
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/85b272b6-ad75-4916-901d-3228e4cbff67" />

- Tela da Lista de Tarefas
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/9857a247-fd26-447a-8422-56c3bf29de46" />



