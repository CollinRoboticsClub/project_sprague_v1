# Project Sprague

## Overview

This is for Collin Robotics Club's Project Sprague V1.

It is a Raspberry Pi based robot.

### Setup

1. When using this on the Pi, make sure to clone the latest version of the code from the repo.
2. pip install -r requirements.txt (Make sure to update requirements.txt every time you install a module by pip freeze > requirements.txt)

### Running the Code

To run the code, run `python3 src/main.py` in the project directory.

To run the code on boot, add the following to the end of the file `/etc/rc.local`:

 cd /home/pi/ProjectSpragueV1 && source venv/bin/activate && python3 main.py
