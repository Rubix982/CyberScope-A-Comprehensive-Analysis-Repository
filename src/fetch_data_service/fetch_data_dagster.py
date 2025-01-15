import os
import subprocess

import dagster

from constants import FETCH_DATA_BIN_PATH

from dagster import op, job

# Define the solid as an operation
@op
def run_rust_script(context):
    # Path to the compiled Rust script (using the custom target directory)
    rust_script_path = FETCH_DATA_BIN_PATH

    # Ensure the file exists
    if not os.path.exists(FETCH_DATA_BIN_PATH):
        raise FileNotFoundError(f"Rust script not found at {rust_script_path}")

    # Run the Rust script as a subprocess
    result = subprocess.run([str(rust_script_path)], capture_output=True, text=True)

    # Log the output and error if any
    context.log.info(f"Rust script output: {result.stdout}")
    if result.stderr:
        context.log.error(f"Rust script error: {result.stderr}")

    return result.stdout


@job
def rust_job():
    run_rust_script()


def main():
    result = dagster.execute_job(rust_job, instance=dagster.DagsterInstance.ephemeral())
    if result.success:
        print("Pipeline executed successfully!")
    else:
        print("Pipeline failed!")


if __name__ == "__main__":
    main()
