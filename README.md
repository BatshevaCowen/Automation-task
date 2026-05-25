Entry Point Website Testing
Using Selenium and the PYTEST Library
The installation of the plugins is in the requirements file.
The installation of the extensions is in the extensions.JSON file 
and versions in the requirements fil

## Prerequisites
- Python 3.12+
- uv
- Chrome
- EntryPoint account

# Installation and Setup
Follow these steps to set up the project locally on your machine:

# Clone the Repository
Clone this repository to your local machine:
```bash
git clone [https://github.com/BatshevaCowen/Automation-task.git](https://github.com/BatshevaCowen/Automation-task.git)
cd Automation-task
# Setup and Configuration

To run the tests, you need to set up your environment variables for authentication:

1. Create a .env file in the root directory.
2. Add your LeetCode credentials into the .env file like this:
   ENTRYPOINT_USERNAME=your_username_here
   ENTRYPOINT_PASSWORD=your_password_here

# Create the environment
seting -> python select interpeter -> .vene

# Install all the required packages in requirements file
pip install -r requirements.txt

# run all tests in the terminal
python -m pytest

# Entry Point Automation Tests

This project runs Selenium tests for EntryPoint login and LeetCode progress.