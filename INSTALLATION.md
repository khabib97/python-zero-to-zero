## Pre-requisites

Before you start, make sure you have the following installed and running:

- [python](https://www.python.org/downloads/): Python 3.6 or higher
- [pip](https://pip.pypa.io/en/stable/installation/): Python package manager


## How to run the project

### Easy way
1. Go to code folder
2. Run the following command, replacing `*` with the day number:
   ```bash
   python3 day_*.py
   ```
### Hard way

1. **Download the project:**
   ```bash
   git clone https://github.com/khabib97/python-zero-to-zero.git
   cd  python-zero-to-zero
   
or, download the zip file and extract it.

2. **Enable virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   It will install all the dependencies from `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the project:**
   To run a specific day's code, run the following command, replacing `*` with the day number:
   ```bash
   python3 code/day_*.py
   ```