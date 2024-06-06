from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class FormWTFAjouterCategorie(FlaskForm):
    nom_categorie_wtf = StringField('Nom de la catégorie', validators=[DataRequired(), Length(min=2, max=50)])
    icon_url_wtf = StringField('URL de l\'icône (SEULEMENT UN URL PNG!)', validators=[DataRequired(), URL()])
    submit = SubmitField('Ajouter')

class FormWTFUpdateCategorie(FlaskForm):
    nom_categorie_update_wtf = StringField('Nom de la catégorie', validators=[DataRequired(), Length(min=2, max=50)])
    icon_url_update_wtf = StringField('URL de l\'icône (SEULEMENT UN URL PNG!)', validators=[DataRequired(), URL()])
    submit = SubmitField('Mettre à jour')

class FormWTFDeleteCategorie(FlaskForm):
    nom_categorie_delete_wtf = StringField('Supprimer cette catégorie')
    submit_btn_conf_del = SubmitField('Confirmer la suppression')
    submit_btn_annuler = SubmitField('Annuler')
