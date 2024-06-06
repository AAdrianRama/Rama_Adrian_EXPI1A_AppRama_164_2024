from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.categories.gestion_categories_wtf_forms import FormWTFAjouterCategorie, FormWTFUpdateCategorie, FormWTFDeleteCategorie
from APP_FILMS_164.roles.gestion_roles_wtf_forms import FormWTFAjouterRole, FormWTFUpdateRole, FormWTFDeleteRole

@app.route('/index', methods=['GET', 'POST'])
def roles_afficher():
    try:
        with DBconnection() as mc_afficher:
            strsql_roles_afficher = """SELECT id_role, nom_role, icon_url FROM roles ORDER BY id_role DESC"""
            mc_afficher.execute(strsql_roles_afficher)
            data_roles = mc_afficher.fetchall()
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération des rôles: {e}")

    return render_template("roles/roles_afficher.html", data=data_roles)

@app.route('/roles_ajouter', methods=['GET', 'POST'])
def roles_ajouter_wtf():
    form = FormWTFAjouterRole()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_role = form.nom_role_wtf.data
                icon_url = form.icon_url_wtf.data

                valeurs_insertion_dictionnaire = {
                    "value_nom_role": nom_role,
                    "value_icon_url": icon_url
                }

                strsql_insert_role = """INSERT INTO roles (nom_role, icon_url) VALUES (%(value_nom_role)s, %(value_icon_url)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_role, valeurs_insertion_dictionnaire)

                flash(f"Rôle ajouté !!", "success")
                return redirect(url_for('roles_afficher'))

        except Exception as e:
            raise Exception(f"Erreur lors de l'ajout du rôle : {e}")

    return render_template("roles/roles_ajouter_wtf.html", form=form)

@app.route('/role_update', methods=['GET', 'POST'])
def role_update_wtf():
    id_role_update = request.values.get('id_role_btn_edit_html')
    form_update = FormWTFUpdateRole()
    try:
        if request.method == "POST" and form_update.submit.data:
            nom_role = form_update.nom_role_update_wtf.data
            icon_url = form_update.icon_url_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_role": id_role_update,
                "value_nom_role": nom_role,
                "value_icon_url": icon_url
            }

            str_sql_update_role = """UPDATE roles SET nom_role = %(value_nom_role)s, icon_url = %(value_icon_url)s WHERE id_role = %(value_id_role)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_role, valeur_update_dictionnaire)

            flash(f"Rôle mis à jour !!", "success")
            return redirect(url_for('roles_afficher'))

        elif request.method == "GET":
            str_sql_id_role = "SELECT id_role, nom_role, icon_url FROM roles WHERE id_role = %(value_id_role)s"
            valeur_select_dictionnaire = {"value_id_role": id_role_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_role, valeur_select_dictionnaire)
                data_nom_role = mybd_conn.fetchone()

                if data_nom_role:
                    form_update.nom_role_update_wtf.data = data_nom_role["nom_role"]
                    form_update.icon_url_update_wtf.data = data_nom_role["icon_url"]
                else:
                    flash(f"Aucun rôle trouvé pour l'ID {id_role_update}", "warning")
                    return redirect(url_for('roles_afficher'))

    except Exception as e:
        raise Exception(f"Erreur : {e}")

    return render_template("roles/role_update_wtf.html", form_update=form_update)

@app.route('/role_delete', methods=['GET', 'POST'])
def role_delete_wtf():
    id_role_delete = request.values.get('id_role_btn_delete_html')
    form_delete = FormWTFDeleteRole()
    try:
        if request.method == "POST":
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("roles_afficher"))

            if form_delete.submit_btn_conf_del.data:
                valeur_delete_dictionnaire = {"value_id_role": id_role_delete}

                str_sql_delete_role = """DELETE FROM roles WHERE id_role = %(value_id_role)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_role, valeur_delete_dictionnaire)

                flash(f"Rôle supprimé !!", "success")
                return redirect(url_for('roles_afficher'))

        elif request.method == "GET":
            str_sql_id_role = "SELECT id_role, nom_role FROM roles WHERE id_role = %(value_id_role)s"
            valeur_select_dictionnaire = {"value_id_role": id_role_delete}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_role, valeur_select_dictionnaire)
                data_nom_role = mybd_conn.fetchone()

                if data_nom_role:
                    form_delete.nom_role_delete_wtf.data = data_nom_role["nom_role"]
                else:
                    flash(f"Aucun rôle trouvé pour l'ID {id_role_delete}", "warning")
                    return redirect(url_for('roles_afficher'))

    except Exception as e:
        raise Exception(f"Erreur : {e}")

    return render_template("roles/role_delete_wtf.html", form_delete=form_delete)

@app.route('/')
@app.route('/homepage')
def mapageprincipale():
    return render_template("home.html")

@app.route('/essai')
def route_hommage_a_u_x_V_ictim_es_du_monstre_du_mod_1_6_4():
    return redirect(url_for('categories_afficher', order_by='ASC', id_categorie_sel=0))

@app.route('/utilisateurs')
def afficher_utilisateurs():
    try:
        with DBconnection() as mc_afficher:
            strsql_utilisateurs_afficher = """
                SELECT u.id_utilisateur, u.nom, u.prenom, u.mail, u.icon_url, u.nom_utilisateur, u.date_naiss, u.mot_de_passe, r.nom_role
                FROM utilisateurs u
                LEFT JOIN roles r ON u.id_role = r.id_role
                ORDER BY u.id_utilisateur ASC
            """
            mc_afficher.execute(strsql_utilisateurs_afficher)
            data_utilisateurs = mc_afficher.fetchall()
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération des utilisateurs: {e}")

    return render_template("utilisateurs/utilisateurs_afficher.html", data=data_utilisateurs)

@app.route('/categories_afficher/<string:order_by>/<int:id_categorie_sel>', methods=['GET', 'POST'])
def categories_afficher(order_by, id_categorie_sel):
    try:
        with DBconnection() as mc_afficher:
            if order_by == "ASC" and id_categorie_sel == 0:
                strsql_categories_afficher = """SELECT id_categorie, nom_categorie, icon_url FROM categories ORDER BY id_categorie ASC"""
                mc_afficher.execute(strsql_categories_afficher)
            elif order_by == "ASC":
                valeur_id_categorie_selected_dictionnaire = {"value_id_categorie_selected": id_categorie_sel}
                strsql_categories_afficher = """SELECT id_categorie, nom_categorie, icon_url FROM categories WHERE id_categorie = %(value_id_categorie_selected)s"""
                mc_afficher.execute(strsql_categories_afficher, valeur_id_categorie_selected_dictionnaire)
            else:
                strsql_categories_afficher = """SELECT id_categorie, nom_categorie, icon_url FROM categories ORDER BY id_categorie ASC"""
                mc_afficher.execute(strsql_categories_afficher)

            data_categories = mc_afficher.fetchall()
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération des catégories: {e}")

    return render_template("categories/categories_afficher.html", data=data_categories)

@app.route('/categories_ajouter', methods=['GET', 'POST'])
def categories_ajouter_wtf():
    form = FormWTFAjouterCategorie()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_categorie = form.nom_categorie_wtf.data
                icon_url = form.icon_url_wtf.data

                valeurs_insertion_dictionnaire = {
                    "value_nom_categorie": nom_categorie,
                    "value_icon_url": icon_url
                }

                strsql_insert_categorie = """INSERT INTO categories (nom_categorie, icon_url) VALUES (%(value_nom_categorie)s, %(value_icon_url)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_categorie, valeurs_insertion_dictionnaire)

                flash(f"Catégorie ajoutée !!", "success")
                return redirect(url_for('categories_afficher', order_by='ASC', id_categorie_sel=0))

        except Exception as e:
            raise Exception(f"Erreur lors de l'ajout de la catégorie : {e}")

    return render_template("categories/categories_ajouter_wtf.html", form=form)

@app.route('/categorie_update', methods=['GET', 'POST'])
def categorie_update_wtf():
    id_categorie_update = request.values.get('id_categorie_btn_edit_html')
    form_update = FormWTFUpdateCategorie()
    try:
        if request.method == "POST" and form_update.submit.data:
            nom_categorie = form_update.nom_categorie_update_wtf.data
            icon_url = form_update.icon_url_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_categorie": id_categorie_update,
                "value_nom_categorie": nom_categorie,
                "value_icon_url": icon_url
            }

            str_sql_update_categorie = """UPDATE categories SET nom_categorie = %(value_nom_categorie)s, icon_url = %(value_icon_url)s WHERE id_categorie = %(value_id_categorie)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_categorie, valeur_update_dictionnaire)

            flash(f"Catégorie mise à jour !!", "success")
            return redirect(url_for('categories_afficher', order_by="ASC", id_categorie_sel=0))

        elif request.method == "GET":
            str_sql_id_categorie = "SELECT id_categorie, nom_categorie, icon_url FROM categories WHERE id_categorie = %(value_id_categorie)s"
            valeur_select_dictionnaire = {"value_id_categorie": id_categorie_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_categorie, valeur_select_dictionnaire)
                data_nom_categorie = mybd_conn.fetchone()

                if data_nom_categorie:
                    form_update.nom_categorie_update_wtf.data = data_nom_categorie["nom_categorie"]
                    form_update.icon_url_update_wtf.data = data_nom_categorie["icon_url"]
                else:
                    flash(f"Aucune catégorie trouvée pour l'ID {id_categorie_update}", "warning")
                    return redirect(url_for('categories_afficher', order_by="ASC", id_categorie_sel=0))

    except Exception as e:
        raise Exception(f"Erreur : {e}")

    return render_template("categories/categorie_update_wtf.html", form_update=form_update)


@app.route('/categorie_delete', methods=['GET', 'POST'])
def categorie_delete_wtf():
    id_categorie_delete = request.values.get('id_categorie_btn_delete_html')
    form_delete = FormWTFDeleteCategorie()
    try:
        if request.method == "POST":
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("categories_afficher", order_by="ASC", id_categorie_sel=0))

            if form_delete.submit_btn_conf_del.data:
                valeur_delete_dictionnaire = {"value_id_categorie": id_categorie_delete}

                str_sql_delete_categorie = """DELETE FROM categories WHERE id_categorie = %(value_id_categorie)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_categorie, valeur_delete_dictionnaire)

                flash(f"Catégorie supprimée !!", "success")
                return redirect(url_for('categories_afficher', order_by="ASC", id_categorie_sel=0))

        elif request.method == "GET":
            str_sql_id_categorie = "SELECT id_categorie, nom_categorie FROM categories WHERE id_categorie = %(value_id_categorie)s"
            valeur_select_dictionnaire = {"value_id_categorie": id_categorie_delete}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_categorie, valeur_select_dictionnaire)
                data_nom_categorie = mybd_conn.fetchone()

                if data_nom_categorie:
                    form_delete.nom_categorie_delete_wtf.data = data_nom_categorie["nom_categorie"]
                else:
                    flash(f"Aucune catégorie trouvée pour l'ID {id_categorie_delete}", "warning")
                    return redirect(url_for('categories_afficher', order_by="ASC", id_categorie_sel=0))

    except Exception as e:
        raise Exception(f"Erreur : {e}")

    return render_template("categories/categorie_delete_wtf.html", form_delete=form_delete)
