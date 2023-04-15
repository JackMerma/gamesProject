from .interpreter import draw
from .chessPictures import *
import sys, traceback, re

def validate(code):
    for line in code.splitlines():
        if re.search("^from.*import.*", line) or re.search("^import", line):
            return [True, "You can't use import statement"]
        if re.search("^print.*", line):
            return [True, "You can't use print statement"]
    return [False, ""]

def putDataArguments(code, data, oldCode):
    output = ''
    for line in code.splitlines():
        result = re.search("(.*)draw\((.*)\)", line)

        if result:
            output += result.group(1) + "draw([" + result.group(2) + ", '" + data[0] + "', '" + data[1] + "', '''" + oldCode + "'''])"
        else:
            output += line
        output += "\n"
    return output

# retorna un booleano (error) y el error
def create(code, data):
    # statements
    exp = validate(code)
    if exp[0]:
        return exp[1] #retornando el error

    # running code
    try:
        oldCode = code
        code = putDataArguments(code, data, oldCode)
        print(code)
        exec(code)
        return ""
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    return "%s at line %d: %s" % (error_class, line_number, detail)
