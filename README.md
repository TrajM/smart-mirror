# Smart Mirror Project on Raspberry Pi

## Project Description:
Display information on a screen mounted behind a Two-Way mirror using Raspberry Pi and PyQt.

In this Implementation the following information are displayed:
- Date and Time
- Weather using Open Weather Map
- Next Train/Bus arrival using MVG (München Verkehrsgesellschaft) data
- Daily To-Do list using Any.do (still in development)

## Dependencies:
- pip install pyqt4 pyqt4-tools
- pip install pyowm
- pip install PyMVGLive
## Usage:
- Fix GUI windows sizes with Qt Designer
- Generate ui_mainwindow.py with make_uic.bat (change make_uic URL to correct pyuic script)
- Add OWM api key, station name and city on the main.py

## TODO: 
This implementation is getting obsolete.
Upgrade the code to PyQt5.
