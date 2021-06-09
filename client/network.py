import requests
from requests.auth import HTTPBasicAuth
from PySide2.QtCore import QObject, Slot


class Network(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.urlBase = None
        self.username = None
        self.password = None
        self.session = None
        #self.openSession("http://127.0.0.1:5000/", "admin", "5GdFP7u8MYFiFc*A3dJ3TAqnBhgeqBmsjYVMaJY@PS#&bgQr")

    @Slot(str, str, str, result=bool)
    def openSession(self, urlBase, username, password):
        self.urlBase = 'http://' + urlBase + '/api'
        self.username = username
        self.password = password
        self.session = requests.session()
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        try:
            res = self.session.get(self.urlBase)
            res.raise_for_status()
            print(res.text)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def get(self, resource):
        res = self.session.get(self.urlBase + resource)
        return res

    def closeSession(self):
        self.session.close()
        
