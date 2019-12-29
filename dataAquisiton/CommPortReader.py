import sys

import serial.tools.list_ports
import time
import threading
import logging
import config.Constants as config

from threading import Thread



class CommPortReader(object):
    trainingStarted = False;
    logging.basicConfig(
        filename=config.LOG_FILE_NAME,
        level=config.LOG_LEVEL,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logger = logging.getLogger()

    def getPorts(self):
        self.logger.info("CommPortReader.getPorts()")
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element.device)
        return

    def startReading(self, portName):
        self.logger.info("CommPortReader.startReading(): called for " + str(portName))
        ser = serial.Serial(portName, 9600, timeout=0)
        thread = Thread(target=self.listenToPort, args=[ser])
        thread.start()
        self.thread = thread

    def listenToPort(self, serial):
        self.logger.info("CommPortReader.listenToPort(): called for " + serial.port)
        currentThread = threading.currentThread()
        while getattr(currentThread, "do_run", True):
            out = serial.read(1)
            out = out.decode("utf-8")
            if (out == "1"):
                self.notifyServer()
                time.sleep(0.5)

    def stopReading(self):
        self.logger.info("CommPortReader.stopReading()")
        self.thread.do_run = False

    def notifyServer(self):
        self.logger.info("CommPortReader.notifyServer(): value read from sernsor! sending to srever..")




if __name__ == "__main__":
    x = CommPortReader()
    x.getPorts()
    x.startReading("COM6")
    time.sleep(8)
    x.stopReading()
