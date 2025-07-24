from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

from app import db
from app.models import Tarefa

class tarefaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = TextAreaField("Descrição")
    status = SelectField("Status", choices=[
        ('a_fazer', 'A Fazer'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído')
    ])
    btnSubmit = SubmitField('Enviar')
    
    def save(self):
        tarefa = Tarefa(
            titulo = self.titulo.data,
            descricao = self.descricao.data,
            status = self.status.data,
        )
        db.session.add(tarefa)
        db.session.commit()