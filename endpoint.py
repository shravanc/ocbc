import json
import logging
import pathlib
import uuid
from decimal import Decimal
from os import path

from flask import Flask, request
from flask import jsonify

from flask import send_from_directory
from flask_cors import CORS
from flask_restful import Api

from healthcheck import HealthCheck

import constant
from constant import DE_APPLICATION_NAME
#from controllers.extract_data import extract_translated_data
from exceptions.exception_logger import create_logger
from log import configure_logger, DE_LOG_FILE_PATH
from params import Param

class DataExtractorJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return json.JSONEncoder.default(self, o)


class DEConfig:
    RESTFUL_JSON = {"cls": DataExtractorJSONEncoder}


app = Flask(DE_APPLICATION_NAME)
configure_logger(app.logger, logging.INFO, DE_LOG_FILE_PATH)
create_logger(DE_LOG_FILE_PATH)
app.config.from_object(DEConfig)
CORS(app)

api = Api(app, catch_all_404s=True)


app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: de_health.run())



@app.route('/', methods=["GET"])
def home_page_route():
    resp = send_from_directory("static", "index.html")
    return resp


@app.route('/extract', methods=["POST"])
def extract_data_route():
    file = request["file"]

    print("--1--", request)
    params = Param(request)
    file.save(params.file_location)
    print("--2--")
    print(params.file_location)
    data = parse_document()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host=constant.HOST, port=constant.PORT_NUMBER)
