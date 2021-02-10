import os
import subprocess

def heal(script_name, py_error_path):
    print('Beginning to heal')

    run_cmd = f'python {script_name} > {py_error_path}'
    run_cmd = run_cmd.split()
    subprocess.run(run_cmd, capture_output=True, text = True)

    with open(py_error_path, 'r') as py_error:
        error_message = py_error.readlines()[-1]
    error_name = os.path.split(py_error_path)[-1]
    error_detail = error_message.split(':')[-1].strip()
    # print(f'Last line of {error_name} : {error_detail}')

    dep_message = 'ModuleNotFoundError'
    dep_message_detail = ' No module named '
    pkg_install_cmd = 'pip install '
    if error_message.startswith(dep_message):
        error_message = error_message.split(':')[-1]
        miss_pkg = error_message.split(dep_message_detail)[-1].replace('\n', '').strip()[1:-1]
        print('Packages missing are :', miss_pkg)
        print('Installing missing package...')
        pkg_install_cmd = (pkg_install_cmd + miss_pkg).split()
        subprocess.run(pkg_install_cmd)
        # print('Cleaning temp files...')
        # os.remove(py_error_path)
    else:
        return 0
