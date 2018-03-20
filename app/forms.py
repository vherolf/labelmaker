from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LabelForm(FlaskForm):
    labeltext = TextAreaField('Label Text', validators=[DataRequired()] )
    generate_pdf_only = BooleanField('Generate PDF only')
    submit = SubmitField('Print label')

class TapeForm(FlaskForm):
    tapewidth = SelectField('Tape Width', choices=[('9', '9mm'), ('12', '12mm'), ('19', '19mm')], )
    tapetext = StringField('Tape Text', validators=[DataRequired()] )
    generate_pdf_only = BooleanField('Generate PDF only')
    submit = SubmitField('Print Tape')