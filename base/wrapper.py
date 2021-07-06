import os
import sys
import json
from jsonschema import validate, ValidationError
from subprocess import check_call, CalledProcessError
import numpy as np

variable_jsonschema_template = """{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "decision variable schema",
  "type": "array",
  "minItems": 32,
  "maxItems": 32,
  "items": {
    "type": "number",
    "minimum": 0,
    "maximum": 1
  }
}"""


def print_json(dic, indent=None):
    print json.dumps(dic, indent=indent)


def print_error(err):
    print_json({
        'objective': None,
        'constraint': None,
        'error': str(err)
    })


def main():
    var_file = 'pop_vars_eval.txt'
    obj_file = 'pop_objs_eval.txt'
    con_file = 'pop_cons_eval.txt'

    x_str = raw_input()
    x = json.loads(x_str)
    validate(x, json.loads(variable_jsonschema_template))
    np.savetxt(var_file, [x], delimiter='\t')

    eval_module_name = os.environ['EVAL_MODULE']
    check_call("python %s . > /dev/null 2>&1" % (eval_module_name + '.py'), shell=True)

    objs = np.loadtxt(obj_file, delimiter='\t')
    cons = np.loadtxt(con_file, delimiter='\t')

    print_json({
        'objective': objs.tolist(),
        'constraint': cons.tolist(),
        'error': None
    })


if __name__ == '__main__':
    try:
        main()
    except ValidationError, e:
        print_error(e)
        sys.exit(10)
    except CalledProcessError, e:
        print_error(e)
        sys.exit(20)
    except Exception, e:
        print_error(e)
        sys.exit(1)
