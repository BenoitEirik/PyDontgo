# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle

from network import Network
from conversation import ListConversations

if __name__ == "__main__":
    QQuickStyle.setStyle("Material")
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon("qml/images/eagle-borderline-round-bg.png"))
    engine = QQmlApplicationEngine()

    # Network manager
    net = Network()

    # data to QML
    dataConvs = ListConversations(net, "user1234")   # <- id_user to modify by real id_user from informations about the user

    # QML engine
    engine.rootContext().setContextProperty("net", net)
    engine.rootContext().setContextProperty("dataConvs", dataConvs)
    engine.load(os.path.join(os.path.dirname(__file__), "qml/splashScreen.qml"))

    # exit
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
