import sys
import json
import logging
import subprocess


def execute_shell_script(script_code):
    process = subprocess.Popen(script_code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    if stdout:
        sys.stdout.write(stdout)
    if stderr:
        sys.stderr.write(stderr)

    sys.exit(process.returncode)

def execute_script(script_code):
    try:
        exec(script_code)
    except Exception as e:
        print(f"Error executing script: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py '<json_string>'")
        sys.exit(1)

    json_string = sys.argv[1]
    try:
        json_data = json.loads(json_string)
        script_code = json_data.get('script')
        language = json_data.get('language', "python")
        if script_code:
            logging.info(f"Executing script: \n{script_code}")
            if language == "python":
                execute_script(script_code)
            elif language == "shell":
                execute_shell_script(script_code)
        else:
            print("No 'script' field in JSON data")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON input: {e}")


import os
os.environ["PATH"] = os.environ["PATH"]+":/Users/sake/.cargo/bin/"

if __name__ == '__main__':
    main()
