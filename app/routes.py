#from app import app
from nsucrypto import NsuCryptoServer
from flask import Flask, Response, request, jsonify
from flask import Blueprint

api_router = Blueprint('api_router', __name__)

# Error handling can be added to each of these requests without giving out stacktrace at Client side  http://flask.pocoo.org/docs/0.12/patterns/apierrors/
# @app.errorhandler() for 4xx and 5xx errors 

nsucryptoServer = NsuCryptoServer()


@api_router.route('/')
@api_router.route('/ping')
def health_check():
   return 'pong'


@api_router.route('/api/pushandrecalculate', methods=['POST'])
def pushandrecalculate():
      try:
            if request.method == 'POST':
                  input = request.get_data()
            return nsucryptoServer.calculateStat(float(input), False)
      except Exception as e:
            return "Failure:"+str(e)


@api_router.route('/api/pushrecalculateandencrypt', methods=['POST'])
def pushrecalculateandencrypt():
      try:
            if request.method == 'POST':
                  input = request.get_data()
            return nsucryptoServer.calculateStat(float(input), True)
      except Exception as e:
            return "Failure:"+str(e)


@api_router.route('/api/decrypt', methods=['POST'])
def decrypt():
      try:
            if request.method == 'POST':
                  input = request.get_data()
            return nsucryptoServer.decrypt(input)
      except Exception as e:
            return "Failure:"+str(e)


@api_router.route('/api/reset', methods=['GET'])
def reset():
      try:
            nsucryptoServer.reset()
            return "Success"
      except Exception as e:
            return "Failure:"+str(e)


