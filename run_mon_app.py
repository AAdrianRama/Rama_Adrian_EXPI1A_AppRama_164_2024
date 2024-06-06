from APP_FILMS_164 import app
from APP_FILMS_164 import SECRET_KEY_FLASK
from APP_FILMS_164 import DEBUG_FLASK
from APP_FILMS_164 import ADRESSE_SRV_FLASK
from APP_FILMS_164 import PORT_FLASK
from flask_cors import CORS

from APP_FILMS_164.utilisateurs import gestion_utilisateurs_crud

CORS(app)

if __name__ == '__main__':
    app.secret_key = SECRET_KEY_FLASK
    app.run(debug=DEBUG_FLASK, host=ADRESSE_SRV_FLASK, port=PORT_FLASK)
