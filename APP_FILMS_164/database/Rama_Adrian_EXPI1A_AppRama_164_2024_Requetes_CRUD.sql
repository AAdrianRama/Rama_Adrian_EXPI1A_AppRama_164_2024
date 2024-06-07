/* Pour insérer une nouvelle application dans la table "applications" */

INSERT INTO applications (nom, icon_url, description, lien_telechargement, id_categorie)
VALUES ('New Application', 'https://example.com/icon.png', 'This is a new application.', 'https://example.com/download', 1);

/* Pour lire toutes les applications de la table "applications" */

SELECT * FROM applications;

/* Pour lire une application spécifique par son "id_application" */

SELECT * FROM applications WHERE id_application = 1;

/* Pour mettre à jour les informations d'une application existante */

UPDATE applications
SET nom = 'Updated Application', description = 'This is an updated description.'
WHERE id_application = 1;

/* Pour supprimer une application de la table "applications" */

DELETE FROM applications WHERE id_application = 1;

/* Pour insérer une nouvelle catégorie dans la table "categories" */

INSERT INTO categories (nom_categorie, icon_url)
VALUES ('New Category', 'https://example.com/icon.png');

/* Pour lire toutes les catégories de la table "categories" */

SELECT * FROM categories;

/* Pour lire une catégorie spécifique par son "id_categorie" */

SELECT * FROM categories WHERE id_categorie = 1;

/* Pour mettre à jour les informations d'une categorie existante */

UPDATE categories
SET nom_categorie = 'Updated Category'
WHERE id_categorie = 1;

/* Pour supprimer une catégorie de la table "categories" */

DELETE FROM categories WHERE id_categorie = 1;

/* Pour insérer un nouvel utilisateur dans la table "utilisateurs" */

INSERT INTO utilisateurs (nom, prenom, date_naiss, nom_utilisateur, mot_de_passe, mail, id_role)
VALUES ('New', 'User', '1990-01-01', 'newuser', 'password123', 'newuser@example.com', 1);

/* Pour lire toutes les utilisateurs de la table "utilisateurs" */

SELECT * FROM utilisateurs;

/* Pour lire un utilisateur spécifique par son "id_utilisateur" */

SELECT * FROM utilisateurs WHERE id_utilisateur = 1;

/* Pour mettre à jour les informations d'un utilisateur existant */

UPDATE utilisateurs
SET mot_de_passe = 'newpassword123'
WHERE id_utilisateur = 1;

/* Pour supprimer un utilisateur de la table "utilisateurs" */

DELETE FROM utilisateurs WHERE id_utilisateur = 1;