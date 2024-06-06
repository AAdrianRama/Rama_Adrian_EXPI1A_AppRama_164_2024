from pathlib import Path
from flask import redirect, request, session, url_for, render_template, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *

@app.route("/films_genres_afficher/<int:id_film_sel>", methods=['GET', 'POST'])
def films_genres_afficher(id_film_sel):
    print(" films_genres_afficher id_film_sel ", id_film_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_genres_films_afficher_data = """
SELECT 
    a.id_application, 
    a.nom, 
    a.icon_url, 
    a.description, 
    a.lien_telechargement, 
    a.date_upload,
    c.nom_categorie AS GenresFilms
FROM 
    applications a
LEFT JOIN 
    categories c ON a.id_categorie = c.id_categorie
"""
                if id_film_sel == 0:
                    strsql_genres_films_afficher_data += """
GROUP BY 
    a.id_application, 
    a.nom, 
    a.icon_url, 
    a.description, 
    a.lien_telechargement, 
    a.date_upload, 
    c.nom_categorie
ORDER BY 
    a.date_upload DESC
"""
                    mc_afficher.execute(strsql_genres_films_afficher_data)
                else:
                    strsql_genres_films_afficher_data += """
WHERE a.id_application = %(value_id_film_selected)s
GROUP BY 
    a.id_application, 
    a.nom, 
    a.icon_url, 
    a.description, 
    a.lien_telechargement, 
    a.date_upload, 
    c.nom_categorie
ORDER BY 
    a.date_upload DESC
"""
                    valeur_id_film_selected_dictionnaire = {"value_id_film_selected": id_film_sel}
                    mc_afficher.execute(strsql_genres_films_afficher_data, valeur_id_film_selected_dictionnaire)

                data_genres_films_afficher = mc_afficher.fetchall()
                print("data_genres ", data_genres_films_afficher, " Type : ", type(data_genres_films_afficher))

                if not data_genres_films_afficher and id_film_sel == 0:
                    flash("""La table "applications" est vide. !""", "warning")
                elif not data_genres_films_afficher and id_film_sel > 0:
                    flash(f"L'application {id_film_sel} demandée n'existe pas !!", "warning")

        except Exception as Exception_films_genres_afficher:
            raise ExceptionFilmsGenresAfficher(f"fichier : {Path(__file__).name}  ;  {films_genres_afficher.__name__} ;"
                                               f"{Exception_films_genres_afficher}")

    print("films_genres_afficher  ", data_genres_films_afficher)
    return render_template("films_genres/films_genres_afficher.html", data=data_genres_films_afficher)


@app.route("/edit_genre_film_selected", methods=['GET', 'POST'])
def edit_genre_film_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_genres_afficher = "SELECT id_categorie, nom_categorie FROM categories ORDER BY id_categorie ASC"
                mc_afficher.execute(strsql_genres_afficher)
            data_genres_all = mc_afficher.fetchall()
            print("dans edit_genre_film_selected ---> data_genres_all", data_genres_all)

            id_film_genres_edit = request.values['id_film_genres_edit_html']
            session['session_id_film_genres_edit'] = id_film_genres_edit
            valeur_id_film_selected_dictionnaire = {"value_id_film_selected": id_film_genres_edit}

            data_genre_film_selected, data_genres_films_non_attribues, data_genres_films_attribues = \
                genres_films_afficher_data(valeur_id_film_selected_dictionnaire)

            print(data_genre_film_selected)
            lst_data_film_selected = [item['id_application'] for item in data_genre_film_selected]
            print("lst_data_film_selected  ", lst_data_film_selected, type(lst_data_film_selected))

            lst_data_genres_films_non_attribues = [item['id_categorie'] for item in data_genres_films_non_attribues]
            session['session_lst_data_genres_films_non_attribues'] = lst_data_genres_films_non_attribues
            print("lst_data_genres_films_non_attribues  ", lst_data_genres_films_non_attribues, type(lst_data_genres_films_non_attribues))

            lst_data_genres_films_old_attribues = [item['id_categorie'] for item in data_genres_films_attribues]
            session['session_lst_data_genres_films_old_attribues'] = lst_data_genres_films_old_attribues
            print("lst_data_genres_films_old_attribues  ", lst_data_genres_films_old_attribues, type(lst_data_genres_films_old_attribues))

            print(" data data_genre_film_selected", data_genre_film_selected, "type ", type(data_genre_film_selected))
            print(" data data_genres_films_non_attribues ", data_genres_films_non_attribues, "type ", type(data_genres_films_non_attribues))
            print(" data_genres_films_attribues ", data_genres_films_attribues, "type ", type(data_genres_films_attribues))

            lst_data_genres_films_non_attribues = [item['nom_categorie'] for item in data_genres_films_non_attribues]
            print("lst_all_genres gf_edit_genre_film_selected ", lst_data_genres_films_non_attribues, type(lst_data_genres_films_non_attribues))

        except Exception as Exception_edit_genre_film_selected:
            raise ExceptionEditGenreFilmSelected(f"fichier : {Path(__file__).name}  ;  {edit_genre_film_selected.__name__} ; "
                                                 f"{Exception_edit_genre_film_selected}")

    return render_template("films_genres/films_genres_modifier_tags_dropbox.html",
                           data_genres=data_genres_all,
                           data_film_selected=data_genre_film_selected,
                           data_genres_attribues=data_genres_films_attribues,
                           data_genres_non_attribues=data_genres_films_non_attribues)


@app.route("/update_genre_film_selected", methods=['GET', 'POST'])
def update_genre_film_selected():
    if request.method == "POST":
        try:
            id_film_selected = session['session_id_film_genres_edit']
            print("session['session_id_film_genres_edit'] ", session['session_id_film_genres_edit'])

            old_lst_data_genres_films_non_attribues = session['session_lst_data_genres_films_non_attribues']
            print("old_lst_data_genres_films_non_attribues ", old_lst_data_genres_films_non_attribues)

            old_lst_data_genres_films_attribues = session['session_lst_data_genres_films_old_attribues']
            print("old_lst_data_genres_films_old_attribues ", old_lst_data_genres_films_attribues)

            session.clear()

            # Limiter à une seule sélection
            new_lst_str_genres_films = request.form.getlist('name_select_tags')
            if len(new_lst_str_genres_films) > 1:
                flash("Vous ne pouvez sélectionner qu'une seule catégorie.", "warning")
                return redirect(url_for('edit_genre_film_selected'))

            new_lst_int_genre_film_old = list(map(int, new_lst_str_genres_films))
            print("new_lst_genre_film ", new_lst_int_genre_film_old, "type new_lst_genre_film ", type(new_lst_int_genre_film_old))

            lst_diff_genres_delete_b = list(set(old_lst_data_genres_films_attribues) - set(new_lst_int_genre_film_old))
            print("lst_diff_genres_delete_b ", lst_diff_genres_delete_b)

            lst_diff_genres_insert_a = list(set(new_lst_int_genre_film_old) - set(old_lst_data_genres_films_attribues))
            print("lst_diff_genres_insert_a ", lst_diff_genres_insert_a)

            strsql_insert_genre_film = "UPDATE applications SET id_categorie = %(value_fk_genre)s WHERE id_application = %(value_fk_film)s"
            strsql_delete_genre_film = "UPDATE applications SET id_categorie = NULL WHERE id_application = %(value_fk_film)s AND id_categorie = %(value_fk_genre)s"

            with DBconnection() as mconn_bd:
                for id_genre_ins in lst_diff_genres_insert_a:
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_film": id_film_selected, "value_fk_genre": id_genre_ins}
                    mconn_bd.execute(strsql_insert_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

                for id_genre_del in lst_diff_genres_delete_b:
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_film": id_film_selected, "value_fk_genre": id_genre_del}
                    mconn_bd.execute(strsql_delete_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

        except Exception as Exception_update_genre_film_selected:
            raise ExceptionUpdateGenreFilmSelected(f"fichier : {Path(__file__).name}  ;  {update_genre_film_selected.__name__} ; "
                                                   f"{Exception_update_genre_film_selected}")

    return redirect(url_for('films_genres_afficher', id_film_sel=0))


def genres_films_afficher_data(valeur_id_film_selected_dict):
    print("valeur_id_film_selected_dict...", valeur_id_film_selected_dict)
    try:
        strsql_film_selected = """
            SELECT 
                a.id_application, 
                a.nom, 
                a.icon_url, 
                a.description, 
                a.lien_telechargement, 
                a.date_upload, 
                a.id_categorie,
                c.nom_categorie
            FROM applications a
            LEFT JOIN categories c ON a.id_categorie = c.id_categorie
            WHERE a.id_application = %(value_id_film_selected)s
        """

        strsql_genres_films_non_attribues = """
            SELECT 
                c.id_categorie, 
                c.nom_categorie 
            FROM categories c 
            WHERE c.id_categorie NOT IN (
                SELECT a.id_categorie 
                FROM applications a 
                WHERE a.id_application = %(value_id_film_selected)s
            )
        """

        strsql_genres_films_attribues = """
            SELECT 
                a.id_application, 
                c.id_categorie, 
                c.nom_categorie 
            FROM applications a
            LEFT JOIN categories c ON a.id_categorie = c.id_categorie
            WHERE a.id_application = %(value_id_film_selected)s
        """

        with DBconnection() as mc_afficher:
            mc_afficher.execute(strsql_genres_films_non_attribues, valeur_id_film_selected_dict)
            data_genres_films_non_attribues = mc_afficher.fetchall()
            print("genres_films_afficher_data ----> data_genres_films_non_attribues ", data_genres_films_non_attribues, " Type : ", type(data_genres_films_non_attribues))

            mc_afficher.execute(strsql_film_selected, valeur_id_film_selected_dict)
            data_film_selected = mc_afficher.fetchall()
            print("data_film_selected  ", data_film_selected, " Type : ", type(data_film_selected))

            mc_afficher.execute(strsql_genres_films_attribues, valeur_id_film_selected_dict)
            data_genres_films_attribues = mc_afficher.fetchall()
            print("data_genres_films_attribues ", data_genres_films_attribues, " Type : ", type(data_genres_films_attribues))

            return data_film_selected, data_genres_films_non_attribues, data_genres_films_attribues

    except Exception as Exception_genres_films_afficher_data:
        raise ExceptionGenresFilmsAfficherData(f"fichier : {Path(__file__).name}  ;  {genres_films_afficher_data.__name__} ; "
                                               f"{Exception_genres_films_afficher_data}")
