import subprocess

def run_command(command):
    """
    Run a shell command and return the output
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error Occurred:", e.stderr)

def sync_with_s3():
    """
    Sync the local directory with S3
    """
    sync_command = "aws s3 sync ./Desktop/domain_names s3://domaincheckeren/"
    run_command(sync_command)

def remove_local_directory():
    """
    Remove the local directory
    """
    remove_command = "rm -rf ./Desktop/domain_names/"
    run_command(remove_command)
