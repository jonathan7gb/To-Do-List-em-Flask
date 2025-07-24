from app import db
from datetime import datetime

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=True)
    descricao = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="a_fazer")
    data_envio = db.Column(db.DateTime, default=datetime.now())