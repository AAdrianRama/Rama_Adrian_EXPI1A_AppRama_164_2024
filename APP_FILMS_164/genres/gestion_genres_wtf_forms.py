"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_genre_regexp = "^[A-ZÀÂÄÇÉÈÊËÎÏÔŒÙÛÜŸ][A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_wtf = StringField("Le nom de l'appliaction ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                   Regexp(nom_genre_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    description_regexp = "[A-Za-zÀ-ÖØ-öø-ÿ$$$$\.\-\s]+"
    description_wtf = StringField("La description  ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                   Regexp(description_regexp,
                                                                          message="Pas de chiffres, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    icon_regexp = "^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]+$"
    icon_wtf = StringField("L'icon de l'application ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                   Regexp(icon_regexp,
                                                                          message="En format url directement à l'image")
                                                                   ])
    download_regexp = "^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]+$"
    download_wtf = StringField("Le lien du téléchargement ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                   Regexp(download_regexp,
                                                                          message="En format url directement au téléchargement (si possible !)")
                                                                   ])

    submit = SubmitField("Enregistrer l'application")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_genre_update_regexp = "^[A-ZÀÂÄÇÉÈÊËÎÏÔŒÙÛÜŸ][A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_update_wtf = StringField("Le nom de l'application ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(nom_genre_update_regexp,
                                                                                 message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                          ])
    description_update_regexp = "[A-Za-zÀ-ÖØ-öø-ÿ$$$$\.\-\s]+"
    description_update_wtf = StringField("La description ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                          Regexp(description_update_regexp,
                                                                                 message="Pas de chiffres, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                          ])
    icon_update_regexp = "^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]+$"
    icon_update_wtf = StringField("L'icon de l'application ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                          Regexp(icon_update_regexp,
                                                                                 message="En format url directement à l'image")
                                                                          ])
    download_update_regexp = "^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]+$"
    download_update_wtf = StringField("Le lien du téléchargement ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                          Regexp(download_update_regexp,
                                                                                 message="En format url directement au téléchargement (si possible !)")
                                                                          ])
    submit = SubmitField("Mettre à jour l'application")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
