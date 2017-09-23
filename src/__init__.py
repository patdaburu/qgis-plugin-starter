#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: sample
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This script initializes the plugin, making it known to QGIS.
"""


#noinspection PyPep8Naming
def classFactory(iface):
    """

    :param iface: a QGIS interface instance
    :return: :py:class:`QgsInterface`
    """
    from plugin import Plugin
    return Plugin(iface)
