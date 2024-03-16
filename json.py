#informacion del sistema ej json
import platform
import sys
import subprocess
import json

file_name = "data.json"
sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver()
name = platform.node()
procesador = platform.processor()

if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")

diccionario = {'ip':local, 'so':sistema, 'version':version, 'hostname':name, 'cpu':procesador}
#dictionaryToJson = json.dumps(diccionario)
#print(dictionaryToJson)
file = open(file_name, "w")
json.dump(diccionario, file, indent=4)
file.close()