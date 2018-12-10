from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import routes

app = Flask(__name__)

app.register_blueprint(routes.api_router)

if app.debug:
    file_handler = RotatingFileHandler(
        '/tmp/nsu.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('NsuCrypto Server startup')


if __name__ == '__main__':
   app.run(debug=True)
