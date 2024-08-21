from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextArea

# Here is for Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])
    submit = SubmitField('Continue', render_kw={'class': 'continue-btn'})

eleven_point_scale = [(str(i), f'Opt{i}') for i in range(11)]

# Here is the first emotion check
class EmotionForm(FlaskForm):
    emo_happiness = RadioField('Happiness', choices=eleven_point_scale, validators=[DataRequired()])
    emo_joy = RadioField('Joy', choices=eleven_point_scale, validators=[DataRequired()])
    emo_despair = RadioField('Despair', choices=eleven_point_scale, validators=[DataRequired()])
    emo_sadness = RadioField('Sadness', choices=eleven_point_scale, validators=[DataRequired()])
    emo_irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()]) 
    emo_rage = RadioField('Rage', choices=eleven_point_scale, validators=[DataRequired()])  
    # emo_confusion = RadioField('Confusion', choices=eleven_point_scale, validators=[DataRequired()])  
    
    feedback = StringField('',validators=[DataRequired()],widget=TextArea())


class ActionForm(FlaskForm):
    action = RadioField('Choose an action', validators=[DataRequired(message="You must choose an action.")])
    submit = SubmitField('Continue', render_kw={'class': 'continue-btn'})