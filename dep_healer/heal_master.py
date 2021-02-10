#try main code
import os
import subprocess
import argparse
from dep_healer import heal
# import random

argparser = argparse.ArgumentParser()
argparser.add_argument('-s','--script', required=True)
argparser.add_argument('-e','--errorfile', default='py_error')

args = argparser.parse_args()
script_name = args.script
error_name = args.errorfile

main_cmd = f'python {script_name}'.split()
# err_main_cmd = f'python {script_name} > {error_name}'.split()
is_not_healed = True
script_out = ''
while is_not_healed:
    try:
        print('Trying to run script...')
        script_out = subprocess.run(main_cmd, check= True, capture_output= True).stdout
        is_not_healed = False
        print('Script run successful...')
    except :
        print('Retrying with healing algorithm....')
        error_report = subprocess.run(main_cmd, capture_output= True, text= True).stderr
        py_error_dir = f'./error_cache/'
        py_error_path = os.path.join(py_error_dir, error_name + '.txt')
        if not os.path.exists(py_error_dir):
            os.mkdir(py_error_dir)
        with  open(py_error_path, 'w') as py_error:
            py_error.write(error_report)
        healer_response = heal(script_name, py_error_path)
        if not healer_response:
            print('This is not a Module Not Found error')
            break
if script_out:
    print('Script output :', script_out)
    print('Run successful ...')
else:
    print('Run unsuccessful...')
#if main code returns error - get error file
#run healing script
#run main code again