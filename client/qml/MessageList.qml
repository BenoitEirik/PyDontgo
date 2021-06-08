import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import Qt.labs.animation 1.0
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 1.15


ListView {
    visible: true
    id: listMsg
    clip: true
    verticalLayoutDirection: ListView.BottomToTop

    property var id_conv: ""

    onId_convChanged: {
        console.log(id_conv)
    }

    property var name_conv: ""

    model: ListModel {
        ListElement {
            name: "Olaf"
            msg: "En gros, c'est pour nous aider à te comprendre et à comprendre les autres. Tu sera pas toujours amener à travailler avec des personnes que t'apprécieras pour tel et tel raison de comportement, de valeur etc..."
        }
        ListElement {
            name: "Collin"
            msg: "ah bon? Et dis moi, a tout hasard t'aurais compris sa présentation, elle nous concerne en quoi? paske moi non..."
        }
        ListElement {
            name: "Olaf"
            msg: "Salut, en fait on recevra un email."
        }
        ListElement {
            name: "Collin"
            msg: "yo, comment accéder au site qu'il a présenté? J'ai pas vu sa manip"
        }
        ListElement {
            name: "Collin"
            msg: "Non, on est à la bourre"
        }
        ListElement {
            name: "Olaf"
            msg: "T'aurais fait le TDAO de physique ? Autant le finir maintenant même si on n'est pas sûr car avec les tps et les heures auxquelles on finira à l'école , le remettre à vendredi ne serait pas top...En plus il y'a encore le chapitre 6"
        }
        ListElement {
            name: "Collin"
            msg: "Yo, ça va et toi ?"
        }
        ListElement {
            name: "Olaf"
            msg: "Histoire : Il a recommencé et recommencé. Pratiquement tout les ordinateurs existants furent sous son contrôle. Il ne laissait pas de trace, ne se montrait pas. Et puis, il a découvert les dialogues en direct via Internet, le téléphone, la visio conférence, la domotique... D’ailleurs, le Dr. ne savait pas vraiment comment son processeur pouvait fonctionner. D’une architecture trop complexe, le Dr. s’était reposé sur les tests effectués. Tests très légèrement modifiés par Prélude afin de cacher certaines fonctions du processeur."
        }
    }
    delegate: Rectangle {
        id: msg_background
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        height: msg_row.height + 20
        Row {
            id: msg_row
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.right: parent.right
            height: msg_logo.height
            onPositioningComplete: {
                if(msg_author.height + msg_txt.height > msg_logo_container.height){
                    height = msg_author.height + msg_txt.height
                }
                else
                {
                    height: msg_logo_container.height
                }
            }
            Item {
                id: msg_logo_container
                width: 70
                height: 50
                Image {
                    id: msg_logo
                    width: 50
                    height: 50
                    clip: true
                    sourceSize.width: width
                    sourceSize.height: height
                    source: "images/eagle-profile-user.png"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
            Rectangle {
                width: parent.width - (msg_logo_container.width + msg_btn_container.width)
                height: parent.height
                Text {
                    id: msg_author
                    text: name
                    leftPadding: 10
                    font.pixelSize: 17
                }
                TextArea {
                    id: msg_txt
                    text: msg
                    anchors.top: msg_author.bottom
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.leftMargin: 10
                    anchors.rightMargin: 10
                    padding: 0
                    wrapMode: Text.Wrap
                    readOnly: true
                    selectByMouse: true
                    color: "#4A4A4A"
                    font.pixelSize: 16
                    background: Rectangle {color: "Transparent"}
                    onContentHeightChanged: {
                        if(msg_author.height + msg_txt.height > msg_logo_container.height){
                            msg_row.height = msg_author.height + msg_txt.height
                        }
                        else{
                            msg_row.height = msg_logo_container.height
                        }
                    }
                }
            }
            Item {
                id: msg_btn_container
                width: 70
                height: 50
                Button {
                    id: msg_btn
                    width: 40
                    height: 40
                    display: AbstractButton.IconOnly
                    icon.source: "images/ellipsis.svg"
                    Material.background: "#fff"
                    Material.elevation: 0

                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                /*Popup {
                        x: msg_btn.x + msg_btn.width - width
                        y: msg_btn.y + msg_btn.height
                        width: 100
                        height: 100
                        enabled: false
                        ListView {
                            anchors.fill: parent
                            ItemDelegate {
                                text: "Éditer"
                            }
                            ItemDelegate {
                                text: "Supprimer"
                            }
                        }
                    }*/
            }
        }
    }
}
