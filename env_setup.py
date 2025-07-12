import pkg_resources
import subprocess
import sys
import re

# Load and clean package names from file
with open("data_science_libs.txt", "r") as f:
    lines = f.readlines()

packages = [re.sub(r'#.*', '', line).strip() for line in lines if line.strip() and not line.startswith("#")]

# Get currently installed packages and versions
installed_pkgs = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

# Iterate through the list
for pkg_name in packages:
    normalized_name = pkg_name.lower().replace("_", "-")

    print(f"\n🔍 Checking: {pkg_name}...")

    if normalized_name in installed_pkgs:
        # Check for updates
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", pkg_name, "--dry-run"],
            capture_output=True,
            text=True
        )

        if "Requirement already satisfied" in result.stdout:
            print(f"⏭️ Already up-to-date: {pkg_name}")
        else:
            print(f"🔄 Updating: {pkg_name}")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", pkg_name])
    else:
        print(f"📦 Installing: {pkg_name}")
        subprocess.run([sys.executable, "-m", "pip", "install", pkg_name])