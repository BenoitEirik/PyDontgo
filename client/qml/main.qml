import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import Qt.labs.animation 1.0
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 1.15


Window {
    id: window
    width: 1400
    height: 800
    minimumWidth: 1000
    minimumHeight: 400
    visible: true
    color: "#00000000"
    title: qsTr("PyDontgo")
    Material.theme: Material.Light
    Material.foreground: Material.Brown     // txt arrière plan
    Material.accent: Material.Brown         // txt premier plan

    property int nbConvs: 0

    Rectangle {
        id: left_area
        width: 250
        color: "#ffffff"
        anchors.left: side_bar.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.topMargin: 0
        anchors.bottomMargin: 0
        clip: true
        TabBar {
            id: tabBar_left_area
            width: 250
            height: 48
            Material.background: "#4A4A4A"
            Material.accent: "white"
            Material.foreground: "#CCCCCC"
            TabButton {
                id: btn_conv
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                width: 125
                anchors.top: parent.top
                display: AbstractButton.IconOnly
                icon.source: "images/chat.svg"
                onClicked: {swipeView_left_area.currentIndex = 0}
            }
            TabButton {
                id: btn_contacts
                anchors.left: parent.left
                anchors.bottom: parent.bottom
                anchors.top: parent.top
                width: 125
                display: AbstractButton.IconOnly
                icon.source: "images/agenda.svg"
                onClicked: {swipeView_left_area.currentIndex = 1}
            }
        }
        SwipeView {
            id: swipeView_left_area
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: tabBar_left_area.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            ListView {
                // index 0
                id: list_conv
                clip: true
                ScrollIndicator.vertical: ScrollIndicator {}
                model: ListModel {
                    id: listModel
                    Component.onCompleted: {
                        var jsonStr = dataConvs.getConvName()
                        var jsonObj = JSON.parse(jsonStr)

                        nbConvs = 0;
                        jsonObj.forEach(data => {
                            nbConvs++
                            listModel.append({'name': data["name"], 'load_info': "test_data_msg.qml"})
                        });
                        console.log(nbConvs)
                    }
                }
                delegate: ItemDelegate {
                    id: listDelegate
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 70
                    Row {
                        id: row_list_conv
                        anchors.fill: parent
                        Item {
                            id: conv_logo_container
                            width: 70
                            height: 70
                            Image {
                                id: conv_logo
                                width: 50
                                height: 50
                                anchors.horizontalCenter: parent.horizontalCenter
                                anchors.verticalCenter: parent.verticalCenter
                                source: "images/profile-conv.png"
                                sourceSize.width: width
                                sourceSize.height: height
                            }
                        }
                        Text {
                            text: name
                            anchors.verticalCenter: parent.verticalCenter
                            font.pixelSize: 17
                        }
                        spacing: 10
                    }
                    onClicked: {
                    }
                }
            }
            ListView {
                // index 1
                id: list_contacts
                clip: true
                ScrollIndicator.vertical: ScrollIndicator {}
                model: ListModel {
                    ListElement {
                        name: "Olaf"
                    }
                    ListElement {
                        name: "Collin"
                    }
                    ListElement {
                        name: "Shrafdine"
                    }
                    ListElement {
                        name: "Venice"
                    }
                }
                delegate: ItemDelegate {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 70
                    Row {
                        id: row_list_contacts
                        anchors.fill: parent
                        Item {
                            id: contacts_logo_container
                            width: 70
                            height: 70
                            Image {
                                id: contacts_logo
                                width: 50
                                height: 50
                                anchors.horizontalCenter: parent.horizontalCenter
                                anchors.verticalCenter: parent.verticalCenter
                                source: "images/eagle-profile-user.png"
                                sourceSize.width: width
                                sourceSize.height: height
                            }
                        }
                        Text {
                            text: name
                            anchors.verticalCenter: parent.verticalCenter
                            font.pixelSize: 17
                        }
                        spacing: 10
                    }
                }
            }
        }

    }
    Rectangle {
        id: central_area
        color: "#ffffff"
        anchors.left: left_area.right
        anchors.right: right_area.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0
        border.width: 1
        border.color: "lightgrey"
        clip: true
        Image {
            id: background_img_presentation
            anchors.top: parent.top
            anchors.topMargin: 48
            anchors.left: parent.left
            anchors.leftMargin: 1
            anchors.rightMargin: 1
            anchors.right: parent.right
            sourceSize.width: width
            sourceSize.height: height
            source: "images/background_central_repeat.jpg"
            fillMode: Image.TileHorizontally
            asynchronous : true
        }
        Item {
            id: central_content_presentation
            anchors.centerIn: parent
            width: 400
            height: 200
            Image {
                id: logo_presentation
                source: "images/eagle-borderline.png"
                width: 100
                height: 100
                sourceSize.width: width
                sourceSize.height: height
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Text {
                text: "<h1>Bienvenue !</h1>PyDontgo est un logiciel de messagerie"
                font.pixelSize: 17
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.bottom: parent.bottom
                color: "#4A4A4A"
                horizontalAlignment: Text.AlignHCenter
            }
        }
        SwipeView {
            id: swipe_conv
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: toolBar.bottom
            anchors.bottom: write_box.top
            anchors.rightMargin: 10
            anchors.bottomMargin: 0
            anchors.leftMargin: 10
            anchors.topMargin: 0
            clip: true
            Repeater {
                model: nbConvs
                Loader {
                    active: SwipeView.isCurrentItem || SwipeView.isNextItem || SwipeView.isPreviousItem
                    sourceComponent: MessageList{
                        id_conv: "TestConv"
                    }
                }
            }
        }
        Rectangle {
            id: write_box
            y: 429
            height: 60
            color: "#ffffff"
            border.color: "#ffffff"
            border.width: 0
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            anchors.bottomMargin: 0
            RectangularGlow {
                anchors.fill: radius_box
                glowRadius: 2
                spread: 0
                color: "grey"
                cornerRadius: radius_box.radius
            }
            Rectangle {
                id: radius_box
                radius: 8
                height: 55
                border.color: "#ffffff"
                border.width: 0
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.rightMargin: 20
                anchors.leftMargin: 20
                anchors.bottomMargin: 20
                anchors.topMargin: 0
                Button {
                    icon.source: "images/attach_file-24px.svg"
                    icon.width: width
                    icon.height: height
                    anchors.left: parent.left
                    anchors.bottom: parent.bottom
                    anchors.leftMargin: 5
                    height: 55
                    width: 55
                    display: AbstractButton.IconOnly
                    Material.background: "white"
                    Material.elevation: 0
                }
                TextArea {
                    id: my_msg
                    width: parent.width - 2 * 70
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 2
                    background: Rectangle {color: "transparent"}
                    wrapMode: Text.Wrap
                    clip: true
                    placeholderText: "Envoyer un message"
                    padding: 0
                    onHeightChanged: {
                        radius_box.height = my_msg.height + 9
                    }
                    Keys.onReturnPressed: {
                        // send msg
                        my_msg.clear();
                    }
                }
                Button {
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 5
                    height: 55
                    width: 55
                    display: AbstractButton.IconOnly
                    icon.source: "images/send.svg"
                    icon.width: width
                    icon.height: height
                    Material.background: "white"
                    Material.elevation: 0
                }
            }
        }
        ToolBar {
            id: toolBar
            height: 48
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            Material.background: "#4A4A4A"
            clip: false
        }
    }

    Rectangle {
        id: right_area
        x: 750
        width: 250
        color: "#fff"
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        clip: true
        TabBar {
            id: tabBar_right_area
            width: 250
            height: 48
            Material.background: "#4A4A4A"
            Material.accent: "white"
            Material.foreground: "#CCCCCC"
        }

        SwipeView {
            id: swipeView
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: tabBar_right_area.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            clip: true
            Column {
                // index 0
                id: profile_right_area
                ItemDelegate {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: width
                    Image {
                        id: profile_img_right_area
                        source: "images/eagle-profile-user.png"
                        anchors.centerIn: parent
                        width: 100
                        height: 100
                        sourceSize.width: width
                        sourceSize.height: height
                    }
                    Text {
                        anchors.top: profile_img_right_area.bottom
                        anchors.topMargin: 20
                        anchors.horizontalCenter: profile_img_right_area.horizontalCenter
                        id: profile_id_right_area
                        text: "ID: #olaf14"
                    }
                }
                ItemDelegate {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 70
                    TextField {
                        id: profile_name_right_area
                        text: "SERGENT Olaf-Marie"
                        anchors.centerIn: parent
                        width: parent.width - 10
                        font.pixelSize: 16
                        background: Rectangle {color: "transparent"}
                        selectByMouse: true
                        horizontalAlignment: TextInput.AlignHCenter
                    }
                }
                ItemDelegate {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 70
                }
            }
            ListView {
                // index 1
                id: settings_right_area
            }
        }
    }
    Rectangle {
        id: side_bar
        width: 56
        color: "#4A4A4A"
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        clip: true
        PropertyAnimation{
            id: animationMenu
            target: side_bar
            property: "width"
            to: if(side_bar.width == 56) return 250; else return 56
            duration: 400
            easing.type: Easing.InOutQuint
        }
        ItemDelegate {
            id: btn_menu
            anchors.top: parent.top
            anchors.left: parent.left
            width: 56
            height: 48
            display: AbstractButton.IconOnly
            icon.source: "images/menu-24px.svg"
            Material.background: hovered ? "#5C5C5C" : "#4A4A4A"
            Material.foreground: "#ffffff"
            Material.primary: "blue"
            Material.elevation: 0
            property bool switch_on: false
            onClicked: {
                animationMenu.start()
            }
        }
        ItemDelegate {
            id: btn_disconnect
            width: 250
            height: 56
            anchors.left: parent.left
            anchors.bottom: btn_settings.top
            display: AbstractButton.TextBesideIcon
            text: "Déconnexion"
            icon.source: "images/logout_black_24dp.svg"
            spacing: 30
            Material.background: hovered ? "#5C5C5C" : "#4A4A4A"
            Material.foreground: "#ffffff"
            Material.primary: "blue"
            Material.elevation: 0
        }
        ItemDelegate {
            id: btn_settings
            x: 0
            y: 499
            width: 250
            height: 56
            anchors.left: parent.left
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            display: AbstractButton.TextBesideIcon
            text: "Paramètres"
            icon.source: "images/settings-24px.svg"
            spacing: 30
            Material.background: hovered ? "#5C5C5C" : "#4A4A4A"
            Material.foreground: "#ffffff"
            Material.primary: "blue"
            Material.elevation: 0
        }
    }
    Rectangle {
        id: hide_view
        color: Qt.rgba(0,0,0,0.50)
        visible: true
        focus: false
        MouseArea {
            anchors.fill: parent
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}
}
##^##*/
