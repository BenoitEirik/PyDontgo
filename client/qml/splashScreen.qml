import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "components"

Window {
    id: splashScreen
    width: 340
    height: 540
    visible: true
    color: "transparent"
    title: qsTr("PyDontgo")

    // Remove Title Bar
    flags: Qt.SplashScreen | Qt.FramelessWindowHint

    // Internal Functions
    QtObject{
        id: internal

        function checkLogin(server, username, password){
            var check = net.openSession(server, username, password)
            if(check){
                // Load list conv information
                dataConvs.updateListObjConvs()

                // Load main page
                var component = Qt.createComponent("main.qml")
                var win = component.createObject()
                win.show()
                visible = false
            }
        }

        function register(username, password){
            // TODO
        }
    }

    Rectangle {
        id: bg
        x: 78
        y: 131
        anchors.fill: parent
        color: "#151515"
        radius: 8
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        z: 1

        Image {
            id: logoImage
            x: 85
            width: 120
            height: 120
            opacity: 1
            anchors.top: parent.top
            source: "images/eagle-splashscreen.png"
            anchors.topMargin: 45
            anchors.horizontalCenter: parent.horizontalCenter
            fillMode: Image.PreserveAspectFit
            sourceSize.width: width
            sourceSize.height: height
        }

        CustomTextField {
            id: textUrlServer
            x: 30
            y: 365
            opacity: 1
            anchors.bottom: textUsername.top
            anchors.bottomMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            placeholderText: qsTr("127.0.0.1:5000 or your online server")
            ToolTip.text: placeholderText
        }

        CustomTextField {
            id: textUsername
            x: 30
            y: 365
            opacity: 1
            anchors.bottom: textPassword.top
            anchors.bottomMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            placeholderText: qsTr("Username")
            ToolTip.text: placeholderText
        }

        CustomTextField {
            id: textPassword
            x: 30
            y: 418
            opacity: 1
            anchors.bottom: btnLogin.top
            anchors.bottomMargin: 20
            anchors.horizontalCenter: parent.horizontalCenter
            placeholderText: qsTr("Password")
            echoMode: TextInput.Password
            ToolTip.text: placeholderText
        }

        CustomButton {
            id: btnLogin
            x: 30
            y: 469
            width: 250
            height: 50
            opacity: 1
            text: qsTr("Sign in")
            anchors.bottom: btnRegister.top
            font.pointSize: 10
            font.family: "Segoe UI"
            colorPressed: "#558b1f"
            colorMouseOver: "#7ece2d"
            colorDefault: "#67aa25"
            anchors.bottomMargin: 0
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: internal.checkLogin(textUrlServer.text, textUsername.text, textPassword.text)
        }

        CustomButton {
            id: btnRegister
            x: 30
            y: 469
            width: 250
            height: 50
            opacity: 1
            text: qsTr("Register")
            anchors.bottom: parent.bottom
            font.pointSize: 10
            font.family: "Segoe UI"
            colorPressed: "#558b1f"
            colorMouseOver: "#7ece2d"
            colorDefault: "#67aa25"
            anchors.bottomMargin: 40
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: internal.checkLogin(textUrlServer.text, textUsername.text, textPassword.text)
        }

        Label {
            id: titleLogo
            x: 100
            y: 294
            opacity: 1
            color: "#ffffff"
            text: qsTr("PyDontgo")
            anchors.bottom: textUrlServer.top
            anchors.bottomMargin: 25
            font.family: "Segoe UI"
            font.pointSize: 16
            anchors.horizontalCenter: parent.horizontalCenter
        }

        CustomButton {
            id: btnClose
            x: 20
            width: 30
            height: 30
            opacity: 1
            text: "X"
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.topMargin: 15
            anchors.rightMargin: 15
            colorPressed: "#558b1f"
            font.family: "Segoe UI"
            colorMouseOver: "#7ece2d"
            colorDefault: "#67aa25"
            font.pointSize: 10
            onClicked: splashScreen.close()
        }
    }
}
