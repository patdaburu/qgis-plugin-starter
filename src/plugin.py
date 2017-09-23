#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: plugin
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This module contains the QGIS plugin implementation.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#noinspection PyPep8Naming
#noinspection PyUnresolvedReferences
class Plugin:
    def __init__(self, iface):
        """

        :param iface: An interface instance that will be passed to this class which provides the hook by which you
            can manipulate the QGIS application at run time.
        :type iface: :py:class:`QgsInterface`
        """
        self.iface = iface
        self._plugin_name = "My Starter Plugin"

    #noinspection PyAttributeOutsideInit
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.action = QAction("Run", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.onRun)
        self.iface.addPluginToMenu(self._plugin_name, self.action)

    def unload(self):
        """Remove the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu(self._plugin_name, self.action)

    def onRun(self):
        """Run method that performs all the real work."""
        QMessageBox.information(self.iface.mainWindow(), "debug", "Running")


