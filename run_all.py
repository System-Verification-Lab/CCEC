import subprocess

# List of scripts to run
scripts = ['many_qusat_outputs_to_stim_type.py', 'qusat_time_values_from_outputs.py', 'many_check_equiv.py','plot.py']


for script in scripts:
    subprocess.run(['python3', script], check=True)
