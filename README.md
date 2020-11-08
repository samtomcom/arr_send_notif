# \*arr Send Notification

A "fork" of https://github.com/samtomcom/arr_post_process (can't fork my own repo : /)

A sample notification script for Sonarr/Radarr.  

## Usage

## Requirements

* Sonarr/Radarr installed
* Python 3.6+ installed and added to your system PATH

## Installation

1. Clone the repository

    git clone https://github.com/samtomcom/arr_send_notif.git

2. Run `python -m pip install -r requirements.txt` to install plyer
3. Edit `execute.bat` to the correct location.
4. Naviage to Sonarr/Radarr [Settings > Connect > + > Custom Script](https://i.imgur.com/UOhYbNf.png), fill in the Path variable to `your\install\path\execute.bat`
5. Test and save

