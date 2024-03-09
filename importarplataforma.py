import platform
import sys
import subprocess

sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver() if sistema == 'Windows' else platform.uname()
hostname = platform.node()
procesador = platform.processor()

print("Estamos en {} en versión: {}".format(sistema, version))
print("Tipo SO: {}".format(sistemaop))
print("Hostname: {}".format(hostname))
print("Procesador: {}".format(procesador))
