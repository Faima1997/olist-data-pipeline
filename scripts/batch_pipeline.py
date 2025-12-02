import subprocess

def run_script(script_path):
    print(f"Running {script_path} ...")
    result = subprocess.run(['python3', script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running {script_path}:\n{result.stderr}")
        exit(1)

if __name__ == "__main__":
    run_script('scripts/transform_data.py')
    run_script('scripts/export_dashboard1_data.py')
    run_script('scripts/export_aggregated_data.py')

    print("Batch pipeline complete!")

