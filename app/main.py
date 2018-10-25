'''
Flask, Dash server running Dana Web
'''
import os

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from utils import logger
from challenge2 import sequential, parallel

logger = logger(os.path.basename(__file__))
__version__ = 1.0

#Flask Server
app = Flask(__name__)

# flask restful service
api = Api(app)


#arguments for restful api
param_parser = reqparse.RequestParser()
param_parser.add_argument('url', required=True)

class Sequential(Resource):
    def get(self):
        '''
        API to return Plot according to param
        '''
        result = {}
        logger.info("Made an API GET call on Sequential")
        try:
            args = param_parser.parse_args()
            url = args.get('url')
            data = sequential(url)
            result = {"data": data}
            status = {'status': 'success'}
            logger.info("Successfully Made an API GET call on Sequential")
        except Exception as e:
            logger.error("Failed to create a json file and return json - {e}".format(e=e))
            status = {'status': 'fail'}
        result.update(status)
        return result, 200


class Parallel(Resource):
    def get(self):
        '''
        API to return Plot according to param
        '''
        result = {}
        logger.info("Made an API GET call on Parallel")
        try:
            args = param_parser.parse_args()
            url = args.get('url')
            data = parallel(url)
            result = {"data": data}
            status = {'status': 'success'}
            logger.info("Successfully Made an API GET call on Parallel")
        except Exception as e:
            logger.error("Failed to create a json file and return json - {e}".format(e=e))
            status = {'status': 'fail'}
        result.update(status)
        return result, 200


#API URI for Restful
api.add_resource(Sequential, '/api/v1.0/sequential')
api.add_resource(Parallel, '/api/v1.0/parallel')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',
          port=5050)
