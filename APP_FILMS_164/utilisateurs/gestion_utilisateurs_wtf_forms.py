from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterUtilisateur(FlaskForm):
    nom_utilisateur = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2, max=50)])
    nom = StringField('Nom', validators=[DataRequired(), Length(min=2, max=50)])
    prenom = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=50)])
    mail = StringField('Email', validators=[DataRequired(), Length(min=6, max=50)])  # Enlever le validateur Email
    date_naiss = DateField('Date de naissance', validators=[DataRequired()], format='%Y-%m-%d')
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=8, max=50)])
    id_role = SelectField('Rôle', choices=[], validators=[DataRequired()])
    submit = SubmitField('Ajouter utilisateur')

class FormWTFUpdateUtilisateur(FlaskForm):
    nom_utilisateur = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2, max=50)])
    nom = StringField('Nom', validators=[DataRequired(), Length(min=2, max=50)])
    prenom = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=50)])
    mail = StringField('Email', validators=[DataRequired(), Length(min=6, max=50)])  # Enlever le validateur Email
    date_naiss = DateField('Date de naissance', validators=[DataRequired()], format='%Y-%m-%d')
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=8, max=50)])
    id_role = SelectField('Rôle', choices=[], validators=[DataRequired()])
    submit = SubmitField('Mettre à jour utilisateur')

class FormWTFDeleteUtilisateur(FlaskForm):
    nom_utilisateur_delete_wtf = StringField('Effacer cet utilisateur')
    submit_btn_conf_del = SubmitField('Confirmer la suppression')
    submit_btn_annuler = SubmitField('Annuler')

