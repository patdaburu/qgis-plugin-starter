SET PLUGIN_NAME=qgis-starter-plugin
SET QGIS_PLUGIN_DIR=%USERPROFILE%\.qgis2\python\plugins\%PLUGIN_NAME%
mkdir %QGIS_PLUGIN_DIR%
xcopy /e /y src\* %QGIS_PLUGIN_DIR%