import os
import subprocess

script_dir = os.path.dirname(__file__)

script_abs_path = os.path.join(script_dir + '/shell_script.sh')

subprocess.call(['sh', script_abs_path])
