from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Regexp

class FormWTFAjouterGenres(FlaskForm):
    nom_genre_regexp = "^[A-ZÀÂÄÇÉÈÊËÎÏÔŒÙÛÜŸ][A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_wtf = StringField("Le nom de l'application ", validators=[Length(min=2, max=50, message="min 2 max 50"),
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
    nom_genre_update_regexp = "^[A-ZÀÂÄÇÉÈÊËÎÏÔŒÙÛÜŸ][A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_update_wtf = StringField("Le nom de l'application ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(nom_genre_update_regexp,
                                                                                 message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                          ])
    description_update_regexp = "[A-Za-zÀ-ÖØ-öø-ÿ$$$$\.\-\s]+"
    description_update_wtf_essai = StringField("La description ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                          Regexp(description_update_regexp,
                                                                                 message="Pas de chiffres, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                          ])
    icon_update_regexp = "^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]+$"
    icon_update_wtf_essai = StringField("L'icon de l'application ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                          Regexp(icon_update_regexp,
                                                                                 message="En format url directement à l'image")
                                                                          ])
    download_update_regexp = "^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]+$"
    download_update_wtf_essai = StringField("Le lien du téléchargement ", validators=[Length(min=2, max=500, message="min 2 max 500"),
                                                                          Regexp(download_update_regexp,
                                                                                 message="En format url directement au téléchargement (si possible !)")
                                                                          ])
    submit = SubmitField("Mettre à jour l'application")


class FormWTFDeleteGenre(FlaskForm):
    nom_genre_delete_wtf = StringField("Effacer cette application")
    submit_btn_del = SubmitField("Effacer application")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")