from flask import render_template, request, redirect, url_for, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.utilisateurs.gestion_utilisateurs_wtf_forms import FormWTFAjouterUtilisateur, FormWTFUpdateUtilisateur, FormWTFDeleteUtilisateur
from datetime import datetime

@app.route("/utilisateurs_afficher/<string:order_by>/<int:id_utilisateur_sel>", methods=['GET', 'POST'])
def utilisateurs_afficher(order_by, id_utilisateur_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_utilisateur_sel == 0:
                    strsql_utilisateurs_afficher = """SELECT u.id_utilisateur, u.nom, u.prenom, u.mail, u.date_naiss, u.nom_utilisateur, u.icon_url, r.nom_role 
                                                     FROM utilisateurs u
                                                     LEFT JOIN roles r ON u.id_role = r.id_role
                                                     ORDER BY u.id_utilisateur ASC"""
                    mc_afficher.execute(strsql_utilisateurs_afficher)
                elif order_by == "ASC":
                    valeur_id_utilisateur_selected_dictionnaire = {"value_id_utilisateur_selected": id_utilisateur_sel}
                    strsql_utilisateurs_afficher = """SELECT u.id_utilisateur, u.nom, u.prenom, u.mail, u.date_naiss, u.nom_utilisateur, u.icon_url, r.nom_role 
                                                     FROM utilisateurs u
                                                     LEFT JOIN roles r ON u.id_role = r.id_role
                                                     WHERE u.id_utilisateur = %(value_id_utilisateur_selected)s"""
                    mc_afficher.execute(strsql_utilisateurs_afficher, valeur_id_utilisateur_selected_dictionnaire)
                else:
                    strsql_utilisateurs_afficher = """SELECT u.id_utilisateur, u.nom, u.prenom, u.mail, u.date_naiss, u.nom_utilisateur, u.icon_url, r.nom_role 
                                                     FROM utilisateurs u
                                                     LEFT JOIN roles r ON u.id_role = r.id_role
                                                     ORDER BY u.id_utilisateur ASC"""
                    mc_afficher.execute(strsql_utilisateurs_afficher)

                data_utilisateurs = mc_afficher.fetchall()

                if not data_utilisateurs and id_utilisateur_sel == 0:
                    flash("""La table "utilisateurs" est vide. !!""", "warning")
                elif not data_utilisateurs and id_utilisateur_sel > 0:
                    flash(f"L'utilisateur demandé n'existe pas !!", "warning")

        except Exception as e:
            raise Exception(f"Erreur : {e}")

    return render_template("utilisateurs/utilisateurs_afficher.html", data=data_utilisateurs)

@app.route("/utilisateurs_ajouter", methods=['GET', 'POST'])
def utilisateurs_ajouter_wtf():
    form = FormWTFAjouterUtilisateur()
    try:
        # Charger les rôles depuis la base de données
        with DBconnection() as mc:
            strsql_roles = """SELECT id_role, nom_role FROM roles ORDER BY nom_role DESC"""
            mc.execute(strsql_roles)
            roles = mc.fetchall()
            form.id_role.choices = [(role['id_role'], role['nom_role']) for role in roles]

        if request.method == "POST":
            if form.validate_on_submit():
                nom = form.nom.data
                prenom = form.prenom.data
                mail = form.mail.data
                date_naiss = form.date_naiss.data
                nom_utilisateur = form.nom_utilisateur.data
                mot_de_passe = form.mot_de_passe.data
                id_role = form.id_role.data
                icon_url = "https://images.freeimages.com/fic/images/icons/573/must_have/256/user.png?fmt=webp&w=500"

                valeurs_insertion_dictionnaire = {
                    "nom": nom,
                    "prenom": prenom,
                    "mail": mail,
                    "date_naiss": date_naiss,
                    "nom_utilisateur": nom_utilisateur,
                    "mot_de_passe": mot_de_passe,
                    "id_role": id_role,
                    "icon_url": icon_url
                }

                strsql_insert_utilisateur = """INSERT INTO utilisateurs (nom, prenom, mail, date_naiss, nom_utilisateur, mot_de_passe, id_role, icon_url) 
                                               VALUES (%(nom)s, %(prenom)s, %(mail)s, %(date_naiss)s, %(nom_utilisateur)s, %(mot_de_passe)s, %(id_role)s, %(icon_url)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_utilisateur, valeurs_insertion_dictionnaire)

                flash(f"Utilisateur ajouté !!", "success")
                return redirect(url_for('utilisateurs_afficher', order_by='ASC', id_utilisateur_sel=0))

    except Exception as e:
        raise Exception(f"Erreur lors du chargement des rôles : {e}")

    return render_template("utilisateurs/utilisateurs_ajouter_wtf.html", form=form)

@app.route("/utilisateurs_update", methods=['GET', 'POST'])
def utilisateurs_update_wtf():
    id_utilisateur_update = request.values.get('id_utilisateur_btn_edit_html')
    form_update = FormWTFUpdateUtilisateur()
    try:
        if request.method == "POST" and form_update.submit.data:
            nom = form_update.nom.data
            prenom = form_update.prenom.data
            mail = form_update.mail.data
            date_naiss = datetime.strptime(str(form_update.date_naiss.data), '%Y-%m-%d').strftime('%Y-%m-%d')
            nom_utilisateur = form_update.nom_utilisateur.data
            mot_de_passe = form_update.mot_de_passe.data
            id_role = form_update.id_role.data

            valeur_update_dictionnaire = {
                "value_id_utilisateur": id_utilisateur_update,
                "nom": nom,
                "prenom": prenom,
                "mail": mail,
                "date_naiss": date_naiss,
                "nom_utilisateur": nom_utilisateur,
                "mot_de_passe": mot_de_passe,
                "id_role": id_role
            }

            str_sql_update_utilisateur = """UPDATE utilisateurs SET nom = %(nom)s, prenom = %(prenom)s, mail = %(mail)s, 
                                            date_naiss = %(date_naiss)s, nom_utilisateur = %(nom_utilisateur)s, 
                                            mot_de_passe = %(mot_de_passe)s, id_role = %(id_role)s 
                                            WHERE id_utilisateur = %(value_id_utilisateur)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_utilisateur, valeur_update_dictionnaire)

            flash(f"Utilisateur mis à jour !!", "success")
            return redirect(url_for('utilisateurs_afficher', order_by="ASC", id_utilisateur_sel=0))

        elif request.method == "GET":
            str_sql_id_utilisateur = "SELECT id_utilisateur, nom, prenom, mail, date_naiss, nom_utilisateur, mot_de_passe, id_role FROM utilisateurs WHERE id_utilisateur = %(value_id_utilisateur)s"
            valeur_select_dictionnaire = {"value_id_utilisateur": id_utilisateur_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_utilisateur, valeur_select_dictionnaire)
                data_utilisateur = mybd_conn.fetchone()

                if data_utilisateur:
                    form_update.nom.data = data_utilisateur["nom"]
                    form_update.prenom.data = data_utilisateur["prenom"]
                    form_update.mail.data = data_utilisateur["mail"]
                    form_update.date_naiss.data = data_utilisateur["date_naiss"]
                    form_update.nom_utilisateur.data = data_utilisateur["nom_utilisateur"]
                    form_update.mot_de_passe.data = data_utilisateur["mot_de_passe"]
                    form_update.id_role.data = data_utilisateur["id_role"]
                else:
                    flash(f"Aucun utilisateur trouvé pour l'ID {id_utilisateur_update}", "warning")
                    return redirect(url_for('utilisateurs_afficher', order_by="ASC", id_utilisateur_sel=0))

            with DBconnection() as mc_afficher:
                strsql_roles_afficher = """SELECT id_role, nom_role FROM roles ORDER BY id_role ASC"""
                mc_afficher.execute(strsql_roles_afficher)
                data_roles = mc_afficher.fetchall()
                form_update.id_role.choices = [(role['id_role'], role['nom_role']) for role in data_roles]

    except Exception as e:
        raise Exception(f"Erreur : {e}")

    return render_template("utilisateurs/utilisateurs_update_wtf.html", form_update=form_update)


@app.route("/utilisateurs_delete", methods=['GET', 'POST'])
def utilisateurs_delete_wtf():
    id_utilisateur_delete = request.values.get('id_utilisateur_btn_delete_html')
    form_delete = FormWTFDeleteUtilisateur()
    try:
        if request.method == "POST":
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("utilisateurs_afficher", order_by="ASC", id_utilisateur_sel=0))

            if form_delete.submit_btn_conf_del.data:
                valeur_delete_dictionnaire = {"value_id_utilisateur": id_utilisateur_delete}

                str_sql_delete_utilisateur = """DELETE FROM utilisateurs WHERE id_utilisateur = %(value_id_utilisateur)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_utilisateur, valeur_delete_dictionnaire)

                flash(f"Utilisateur définitivement effacé !!", "success")
                return redirect(url_for('utilisateurs_afficher', order_by="ASC", id_utilisateur_sel=0))

        elif request.method == "GET":
            str_sql_id_utilisateur = "SELECT id_utilisateur, prenom FROM utilisateurs WHERE id_utilisateur = %(value_id_utilisateur)s"
            valeur_select_dictionnaire = {"value_id_utilisateur": id_utilisateur_delete}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_utilisateur, valeur_select_dictionnaire)
                data_nom_utilisateur = mybd_conn.fetchone()

                if data_nom_utilisateur:
                    form_delete.nom_utilisateur_delete_wtf.data = data_nom_utilisateur["prenom"]
                else:
                    flash(f"Aucun utilisateur trouvé pour l'ID {id_utilisateur_delete}", "warning")
                    return redirect(url_for('utilisateurs_afficher', order_by="ASC", id_utilisateur_sel=0))

    except Exception as e:
        raise Exception(f"Erreur : {e}")

    return render_template("utilisateurs/utilisateurs_delete_wtf.html", form_delete=form_delete)

