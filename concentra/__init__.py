import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # Mudar antes do deploy oficial UTILIZAR DOTENV PARA MASCARAR A VARIÁVEL DE AMBIENTE
        DATABASE=os.path.join(app.instance_path, 'concentra.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World! Estamos On-line!!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import consulta
    app.register_blueprint(consulta.bp)

    from . import naoh
    app.register_blueprint(naoh.bp)
    app.add_url_rule('/', endpoint='index')

    return app


create = create_app()
