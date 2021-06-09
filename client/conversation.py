import requests
from PySide2.QtCore import QObject, Slot


class ListConversations(QObject):
    def __init__(self, net, id_user):
        QObject.__init__(self)
        self.net = net
        self.id_user = id_user
        self.url = "/conversations/list_convs/" + str(id_user)
        self.jsonStr = ""
        self.jsonObject = None
        self.listObjConvs = []

    @Slot()
    def updateListObjConvs(self):
        # Request
        res = self.net.get(self.url)
        print(res)
        self.jsonStr = res.text
        self.jsonObject = res.json()
        # Add Conversation
        for data in self.jsonObject:
            newConv = Conversation(self.net, data['id'])
            result = False
            for conv in self.listObjConvs:
                if newConv == conv:
                    result = True
            if result is True:
                del newConv
            else:
                self.listObjConvs.append(newConv)

    @Slot(result=str)
    def getConvName(self):
        return self.jsonStr


class Conversation(QObject):
    def __init__(self, net, id_conv):
        QObject.__init__(self)
        self.net = net
        self.id_conv = id_conv
        self.url = "api/conversations/conv/" + str(id_conv) + "/" + "get_msg" + "/" + "0123456789"
        
    def getMsgs(self, timestamp):
        res = self.net.get(self.url)
        self.jsonStr = res.text
        self.jsonObject = res.json()
        print(self.jsonStr)
        # TODO @Slot fot QML

    def __eq__(self, other):
        if (isinstance(other, Conversation)):
            return self.id_conv == other.id_conv
        return False
