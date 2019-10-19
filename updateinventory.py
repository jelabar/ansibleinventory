#!/usr/bin/python
import yaml

# Default location
# location = "/etc/ansible/hosts"
location = "./hosts.yml"
# Database location
db = "a"
try:
    stream = open(location, 'r')
    print("Abierto correctamente")
    data = yaml.load(stream, Loader=yaml.FullLoader)
    # Verificar archivo abierto correctamente
    # print(dump(data, Dumper=yaml.Dumper))
except (IOError):
    mensaje = "Error de lectura del archivo de configuraci&oacute;n"


# Construir objeto Python a partir de DB
def get_inventory():
    return "nada"

# Consultar BB
