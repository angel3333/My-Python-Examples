import os
import subprocess
import sys

# Helper function to run shell commands
def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: Command '{command}' failed with exit code {result.returncode}")
        print(result.stdout)
        print(result.stderr)
        sys.exit(result.returncode)
    return result.stdout

# Static Code Analysis (using Bandit)
def run_bandit(path):
    print("Running Bandit for static code analysis...")
    run_command(f"bandit -r {path}")

# Dependency Checking (using Safety)
def run_safety():
    print("Running Safety for dependency checking...")
    run_command("safety check --full-report")

# Secret Scanning (using TruffleHog)
def run_trufflehog(path):
    print("Running TruffleHog for secret scanning...")
    run_command(f"trufflehog {path}")

# Infrastructure as Code Scanning (using Terraform and Snyk)
def run_terraform_scan(path):
    print("Running Snyk for Terraform IaC scanning...")
    run_command(f"snyk iac test {path}")

# Code Coverage and Linting (using Pylint)
def run_pylint(path):
    print("Running Pylint for code linting...")
    run_command(f"pylint {path}")

# Main function to orchestrate the DevSecOps pipeline
def main():
    project_path = os.getcwd()

    # Static Analysis
    run_bandit(project_path)
    
    # Dependency Checking
    run_safety()
    
    # Secret Scanning
    run_trufflehog(project_path)
    
    # Terraform IaC Scanning
    terraform_path = os.path.join(project_path, 'terraform')
    if os.path.exists(terraform_path):
        run_terraform_scan(terraform_path)
    
    # Linting
    run_pylint(project_path)

    print("DevSecOps pipeline completed successfully!")

if __name__ == "__main__":
    main()
