from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Plugin:
    def __init__(self, iface):
        self.iface = iface
        self._plugin_name = "My Starter Plugin"

    def initGui(self):
        self.action = QAction("Run", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.onRun)
        self.iface.addPluginToMenu(self._plugin_name, self.action)

    def unload(self):
        self.iface.removePluginMenu(self._plugin_name, self.action)

    def onRun(self):
        QMessageBox.information(self.iface.mainWindow(), "debug", "Running")


