from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class FormWTFAjouterRole(FlaskForm):
    nom_role_wtf = StringField('Nom du rôle', validators=[DataRequired(), Length(min=2, max=50)])
    icon_url_wtf = StringField('URL de l\'icône (SEULEMENT UN URL PNG!)', validators=[DataRequired(), URL()])
    submit = SubmitField('Ajouter')

class FormWTFUpdateRole(FlaskForm):
    nom_role_update_wtf = StringField('Nom du rôle', validators=[DataRequired(), Length(min=2, max=50)])
    icon_url_update_wtf = StringField('URL de l\'icône (SEULEMENT UN URL PNG!)', validators=[DataRequired(), URL()])
    submit = SubmitField('Mettre à jour')

class FormWTFDeleteRole(FlaskForm):
    nom_role_delete_wtf = StringField('Supprimer ce rôle')
    submit_btn_conf_del = SubmitField('Confirmer la suppression')
    submit_btn_annuler = SubmitField('Annuler')
