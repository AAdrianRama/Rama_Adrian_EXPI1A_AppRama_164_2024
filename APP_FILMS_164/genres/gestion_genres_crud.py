from pathlib import Path
from flask import redirect, request, session, url_for, flash, render_template
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres, FormWTFDeleteGenre, FormWTFUpdateGenre

@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT * FROM applications ORDER BY id_application ASC"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT * FROM applications WHERE id_application = %(value_id_genre_selected)s"""
                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT * FROM applications ORDER BY id_application DESC"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                if not data_genres and id_genre_sel == 0:
                    flash("""La table "applications" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    flash(f"L'application demandée n'existe pas !!", "warning")
                else:
                    flash(f"Données applications affichées !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    return render_template("genres/genres_afficher.html", data=data_genres)


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_genre_wtf = form.nom_genre_wtf.data.lower()
                description = form.description_wtf.data
                icon = form.icon_wtf.data
                download = form.download_wtf.data

                valeurs_insertion_dictionnaire = {
                    "value_intitule_genre": name_genre_wtf,
                    "value_description": description,
                    "value_icon": icon,
                    "value_download": download,
                }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO applications (nom, icon_url, description, lien_telechargement) 
                                         VALUES (%(value_intitule_genre)s, %(value_icon)s, %(value_description)s, %(value_download)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    id_genre_update = request.values['id_genre_btn_edit_html']
    form_update = FormWTFUpdateGenre()
    try:
        if request.method == "POST" and form_update.submit.data:
            name_genre_update = form_update.nom_genre_update_wtf.data.lower()
            description_update = form_update.description_update_wtf_essai.data
            icon_update = form_update.icon_update_wtf_essai.data
            download_update = form_update.download_update_wtf_essai.data

            valeur_update_dictionnaire = {
                "value_id_genre": id_genre_update,
                "value_name_genre": name_genre_update,
                "value_description": description_update,
                "value_icon": icon_update,
                "value_download": download_update
            }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_genre = """UPDATE applications SET nom = %(value_name_genre)s, 
                                      description = %(value_description)s, 
                                      icon_url = %(value_icon)s, 
                                      lien_telechargement = %(value_download)s 
                                      WHERE id_application = %(value_id_genre)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_genre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_genre_update))

        elif request.method == "GET":
            str_sql_id_genre = "SELECT id_application, nom, description, icon_url, lien_telechargement FROM applications WHERE id_application = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_genre_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                data_nom_genre = mybd_conn.fetchone()
                print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre))

            form_update.nom_genre_update_wtf.data = data_nom_genre["nom"]
            form_update.description_update_wtf_essai.data = data_nom_genre["description"]
            form_update.icon_update_wtf_essai.data = data_nom_genre["icon_url"]
            form_update.download_update_wtf_essai.data = data_nom_genre["lien_telechargement"]

    except Exception as Exception_genre_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    id_genre_delete = request.values['id_genre_btn_delete_html']

    form_delete = FormWTFDeleteGenre()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            if form_delete.submit_btn_conf_del.data:
                data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer l'application de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_genre = """DELETE FROM t_genre_film WHERE fk_genre = %(value_id_genre)s"""
                str_sql_delete_idgenre = """DELETE FROM applications WHERE id_application = %(value_id_genre)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idgenre, valeur_delete_dictionnaire)

                flash(f"Application définitivement effacée !!", "success")
                print(f"Application définitivement effacée !!")

                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_genre": id_genre_delete}
            print(id_genre_delete, type(id_genre_delete))

            str_sql_genres_films_delete = """SELECT id_genre_film, nom_film, id_genre, intitule_genre FROM t_genre_film 
                                            INNER JOIN t_film ON t_genre_film.fk_film = t_film.id_film
                                            INNER JOIN t_genre ON t_genre_film.fk_genre = t_genre.id_genre
                                            WHERE fk_genre = %(value_id_genre)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_films_attribue_genre_delete = mydb_conn.fetchall()
                print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

                session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                str_sql_id_genre = "SELECT id_application, nom FROM applications WHERE id_application = %(value_id_genre)s"

                mydb_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                data_nom_genre = mydb_conn.fetchone()
                print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                      data_nom_genre["nom"])

            form_delete.nom_genre_delete_wtf.data = data_nom_genre["nom"]

            btn_submit_del = False

    except Exception as Exception_genre_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_delete_wtf.__name__} ; "
                                      f"{Exception_genre_delete_wtf}")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_genre_delete)