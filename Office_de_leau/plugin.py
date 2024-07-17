# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import QAction, QMenu
from qgis.PyQt.QtCore import Qt

import os.path

from Office_de_leau.utils.plugin_globals import PluginGlobals
from Office_de_leau.gui.dock import DockWidget
from Office_de_leau.gui.about_box import AboutBox
from Office_de_leau.gui.param_box import ParamBox
from Office_de_leau.nodes.tree_node_factory import TreeNodeFactory
from Office_de_leau.nodes.tree_node_factory import download_tree_config_file


class SimpleAccessPlugin:
    """
    Plugin initialisation.
    A json config file is read in order to configure the plugin GUI.
    """

    def __init__(self, iface):
        self.iface = iface
        self.dock = None

        PluginGlobals.instance().set_plugin_path(os.path.dirname(os.path.abspath(__file__)))
        PluginGlobals.instance().set_plugin_iface(self.iface)
        PluginGlobals.instance().reload_globals_from_qgis_settings()

        config_struct = None
        config_string = ""

        # Téléchargez la config si nécessaire
        if self.need_download_tree_config_file():
            download_tree_config_file(PluginGlobals.instance().CONFIG_FILE_URLS[0])

        # Lisez le fichier de l'arborescence des ressources et mettez à jour l'interface graphique
        self.ressources_tree = TreeNodeFactory(PluginGlobals.instance().config_file_path).root_node

    def need_download_tree_config_file(self):
        """
        Doit-on télécharger une nouvelle version du fichier de l'arborescence des ressources ?
        Deux raisons possibles :
        - l'utilisateur veut qu'il soit téléchargé au démarrage du plugin
        - le fichier est actuellement manquant
        """

        return (PluginGlobals.instance().CONFIG_FILES_DOWNLOAD_AT_STARTUP > 0 or
                not os.path.isfile(PluginGlobals.instance().config_file_path))

    def initGui(self):
        """
        Initialisation de l'interface graphique du plugin.
        Crée un élément de menu dans le menu de QGIS
        Crée un DockWidget contenant l'arborescence des ressources
        """

        # Créez un menu
        self.createPluginMenu()

        # Créez un panneau amovible avec une arborescence des ressources
        self.dock = DockWidget()
        self.dock.set_tree_content(self.ressources_tree)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def createPluginMenu(self):
        """
        Crée le menu principal du plugin
        """
        plugin_menu = self.iface.pluginMenu()
        self.plugin_menu = QMenu(u"Office de leau", plugin_menu)
        plugin_menu.addMenu(self.plugin_menu)

        show_panel_action = QAction(u'Afficher le panneau latéral', self.iface.mainWindow())
        show_panel_action.triggered.connect(self.showPanelMenuTriggered)
        self.plugin_menu.addAction(show_panel_action)

        param_action = QAction(u'Paramétrer le plugin…', self.iface.mainWindow())
        param_action.triggered.connect(self.paramMenuTriggered)
        self.plugin_menu.addAction(param_action)

        about_action = QAction(u'À propos…', self.iface.mainWindow())
        about_action.triggered.connect(self.aboutMenuTriggered)
        self.plugin_menu.addAction(about_action)

    def showPanelMenuTriggered(self):
        """
        Affiche le widget dock
        """
        self.dock.show()
        pass

    def aboutMenuTriggered(self):
        """
        Affiche la boîte de dialogue À propos
        """
        dialog = AboutBox(self.iface.mainWindow())
        dialog.exec_()

    def paramMenuTriggered(self):
        """
        Affiche la boîte de dialogue des paramètres
        """
        dialog = ParamBox(self.iface.mainWindow(), self.dock)
        dialog.exec_()

    def unload(self):
        """
        Supprime le menu du plugin
        """
        self.iface.pluginMenu().removeAction(self.plugin_menu.menuAction())
