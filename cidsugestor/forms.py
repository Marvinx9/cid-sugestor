from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FormBase(FlaskForm):
    texto = StringField("Texto", validators=[DataRequired(), Length(10, 200)])
    botao_submit = SubmitField("Receber Sugestão")