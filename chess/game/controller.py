from .interpreter import draw
from .chessPictures import *
import sys, traceback, re

# funcion que valida que NO hayan algunas sentenicas aceptadas como:
#   print()
#   import
#   from ... import
def validate(code):
    for line in code.splitlines():
        # uso de expresiones regulares para identificar casos independientes
        if re.search("^from.*import.*", line) or re.search("^import", line):
            return [True, ["RuntimeError", "You can't use import statement"]]
        if re.search("^print.*", line):
            return [True, ["RuntimeError", "You can't use print statement"]]
    return [False, ["", ""]]

# Funcion que añade dos argumentos a la verdadera funcion draw
# esto se hace para poder guardar la data generada al correr el codigo
#
# En especifico está diseñado para guardar el codigo, la imagen generada
# y otros datos que se procesaran
def putDataArguments(code, data, oldCode):
    output = ''
    for line in code.splitlines():
        # expresion regular para identificar la linea de draw()
        result = re.search("(.*)draw\((.*)\)", line)

        if result:
            # se le añaden los demas parametros
            output += result.group(1) + "draw([" + result.group(2) + ", '" + data[0] + "', '" + data[1] + "', '''" + oldCode + "'''])"
        else:
            output += line
        output += "\n"
    return output

# retorna un booleano (error) y el error
def create(code, data):
    # validacion
    exp = validate(code)
    if exp[0]:
        return exp[1] # retornando el error

    # corre el codigo con 'exec'
    try:
        oldCode = code # necesario para guardar la codigo original de cada usuario
        code = putDataArguments(code, data, oldCode)
        exec(code) # de lo demás se encargara la misma funcion draw()
        return ["", ""]
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    return [error_class, "Line %d: %s" % (line_number, detail)]
