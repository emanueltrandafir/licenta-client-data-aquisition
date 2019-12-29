import requests
import logging
import sys
from model.Race import Race
import config.Constants
import json


class ServerCommunication:
    SERVER_URL = "http://localhost:8090/licenta"
    #training
    GET_RACES_PATH = "/races"
    GET_RACE_PATH = "/races/{id}"
    POST_RACE_PATH = "/races/add"

    # GET_RACE_START = "/races/{id}/start"

    POST_RACE_SITUATION = "/races/{id}/situation"
    GET_RACE_SITUATION = "/race/{id}/situation"

    #rooms
    GET_ROOMS_PATH = "/rooms"
    GET_ROOM_PATH = "/room/{id}"
    POST_ROOM_PATH = "/room"

    logging.basicConfig(
        filename='../log/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logger = logging.getLogger()

    def getAllRaces(self):
        proxies = {'http': self.SERVER_URL}
        self.logger.info("ServerCommunication.getRaces(): request = GET, url = " + self.SERVER_URL + self.GET_RACES_PATH)
        response = requests.get(url=self.SERVER_URL + self.GET_RACES_PATH, proxies=proxies)
        content = response.content.decode("utf-8")
        self.logger.info("ServerCommunication.getRaces(): response = " + str(content))
        return content

    def getRace(self, id):
        proxies = {'http': self.SERVER_URL}
        url = self.SERVER_URL + self.GET_RACES_PATH + "/" + str(id)
        self.logger.info("ServerCommunication.getRaces(): request = GET, url = " + url)
        response = requests.get(url=url, proxies=proxies)
        content = response.content.decode("utf-8")
        self.logger.info("ServerCommunication.getRace(" + str(id) + "): response = " + str(content))
        return content

    def postRace(self, name, distance):
        proxies = {'http': self.SERVER_URL}
        race = Race(name, config.Constants.USERNAME, distance)
        data = json.dumps(race.__dict__)
        url = self.SERVER_URL + self.POST_RACE_PATH
        self.logger.info("ServerCommunication.postRace(): posting race at " + url + ", data = " + data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url=url, data=data, headers=headers, proxies=proxies)
        content = response.content.decode("utf-8")
        self.logger.info("ServerCommunication.postRace(): response = " + str(content))
        return content

    def startRace(self, id):
        proxies = {'http': self.SERVER_URL}
        url = self.SERVER_URL + self.GET_RACES_PATH + "/" + str(id) + "/start"
        self.logger.info("ServerCommunication.getRaces(): request = GET, url = " + url)
        response = requests.get(url=url, proxies=proxies)
        content = response.content.decode("utf-8")
        self.logger.info("ServerCommunication.getRace(" + str(id) + "): response = " + str(content))
        return content

if __name__ == "__main__":
    s = ServerCommunication()
    s.getAllRaces()
    s.postRace("testing", 100)
    s.getRace(0)





