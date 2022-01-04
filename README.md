#  rxposter

Python script for cross posting to multiple subreddits.

***Prerequisites**:* make sure you download and install chrome driver for the chrome version you have installed on your system (https://chromedriver.chromium.org/downloads). It's important that the versions match!

  

 - Setup the virtual environment by running: `python3 -m venv env` 
 - Active the virtual environment by running: `source env/bin/activate` 
 - Install the requirements: `pip install -r requirements.txt` 
 - Open the `config.py` file and add comma delimited values for `SUBS` (these are subreddits
   for x-posting) Example: `SUB="Business_Ideas,gadgets,funny"` 
   Run the script: `python nreddit.py`
