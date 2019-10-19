#!/usr/bin/python
import yaml


# Default location
# location = "/etc/ansible/hosts"
location = "/etc/ansible/hosts"
try:
    stream = open(location, 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)
    # Verificar archivo abierto correctamente
    # print(dump(data, Dumper=yaml.Dumper))
except (IOError):
    mensaje = "Error de lectura del archivo de configuraci&oacute;n"


# Crear objeto python a partir de yaml
# Exportar objeto python a BD
