# Python Environment Setup Script

This repository contains a utility script (`env_setup.py`) to automatically manage the Python environment for a data science projects.

## How It Works

The script reads a list of required Python libraries from `data_science_libs.txt` and performs the following actions for each library:

1.  **Checks** if the library is installed.
2.  **Installs** the library if it is missing.
3.  **Updates** the library if it is installed but not on the latest version.
4.  **Skips** the library if it is already installed and up-to-date.

## Usage

1.  Ensure you have Python and pip installed.
2.  Run the script from your terminal:
    ```bash
    python env_setup.py
    ```

The script will handle the rest, ensuring your environment is synchronized with the project's requirements.

### Managing Libraries

To add, remove, or change a library version, simply edit the `data_science_libs.txt` file. The script ignores lines starting with `##` (headers) and any text after a `#` (comments).
