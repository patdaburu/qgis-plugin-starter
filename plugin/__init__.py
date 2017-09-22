

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """

    :param iface: a QGIS interface instance
    :return: :py:class:`QgsInterface`
    """
    from plugin import Plugin
    return Plugin(iface)
