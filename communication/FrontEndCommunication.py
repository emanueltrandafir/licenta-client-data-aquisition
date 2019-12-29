import sys
import json
from dataAquisiton.DataAquisitionManager import CommPortReader
from flask import Flask, jsonify, request, abort
import logging
import config.Constants as config

app = Flask(__name__)

STATUS_NOT_FOUND = 404
STATUS_OK = 200

@app.route('/licenta/data-aquisition/ports')
def getPorts():
    logger.info("FrontEndCommunicaton.getPorts()")
    try:
        ports = commPortReader.getPorts()
        json = jsonify(ports)
        return json, STATUS_OK
    except:
        return "null", STATUS_NOT_FOUND

@app.route('/licenta/data-aquisition/start', methods=['POST'])
def startReading():
    params = request.get_json()
    logger.info("FrontEndCommunicaton.startReading(): " + params.get('userName') + " , " + params.get('portName'))
    try:
        commPortReader.startReading(params.get('portName'), params.get('userName'))
        return "ok", STATUS_OK
    except:
        return "null", STATUS_NOT_FOUND

@app.route('/licenta/data-aquisition/stop')
def stopReading():
    logger.info("FrontEndCommunicaton.stopReading()")
    try:
        commPortReader.stopReading()
        return "ok", STATUS_OK
    except:
        return "null", STATUS_NOT_FOUND



if __name__ == '__main__':

    commPortReader = CommPortReader()
    logging.basicConfig(
        filename=config.LOG_FILE_NAME,
        level=config.LOG_LEVEL,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logger = logging.getLogger()

    app.run(port="8070")
