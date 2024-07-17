# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel, QTextEdit, QFrame
from qgis.PyQt.QtGui import QPixmap

from Office_de_leau.utils.plugin_globals import PluginGlobals


class AboutBox(QDialog):
    """
    About box of the plugin
    """

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        mainLayout = QVBoxLayout()

        logo_file_path = PluginGlobals.instance().logo_file_path
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(logo_file_path))
        mainLayout.addWidget(self.logo)


        title = u"À propos de l'extension Office de l'eau Réunion…"
        description = u"""Extension pour QGIS donnant un accès simplifié aux ressources géographiques utiles à l'Office de l'eau Réunion
Version {0}
Plus d'informations à l'adresse suivante :
{1}
        """.format(PluginGlobals.instance().PLUGIN_VERSION,
            PluginGlobals.instance().PLUGIN_SOURCE_REPOSITORY)

        self.textArea = QTextEdit()
        self.textArea.setReadOnly(True)
        self.textArea.setText(description)
        self.textArea.setFrameShape(QFrame.NoFrame)
        mainLayout.addWidget(self.textArea)

        self.setModal(True)
        self.setSizeGripEnabled(False)

        self.setLayout(mainLayout)

        self.setFixedSize(400, 250)
        self.setWindowTitle(title)
