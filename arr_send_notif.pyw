import os
from plyer import notification

SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
ENV_FILE = f"{SCRIPT_DIR}\\ARR_ENV.txt"
SONARR_ICO = "C:\\ProgramData\\NzbDrone\\bin\\UI\\Content\\Images\\favicon.ico"
RADARR_ICO = "C:\\ProgramData\\Radarr\\bin\\UI\\Content\\Images\\favicon\\favicon.ico"

envs = {}

def getEnv(env):
    if env in envs:
        return envs[env]
    else:
        return False

# Checking all potentiall environment variables
with open(ENV_FILE, 'r') as f:
    for line in f:
        env = line.rstrip()
        if env in os.environ:
            envs[env] = os.environ[env]

    # No environment variables were found
    # Either the script was run manually as a test (ie Not ran by *arr)
    #  or, something went wrong : )
    if len(envs) == 0:
        raise Exception('No *arr Environment variables were found.')

if "RADARR_EVENTTYPE" in envs:
    ico = RADARR_ICO
    title = "Radarr"

    eventtype = envs['RADARR_EVENTTYPE']
    if eventtype == "Rename":
        mes = f"A file for {envs['RADARR_MOVIE_TITLE']} has been Renamed."
    elif eventtype == "Grab":
        mes = f"A file for {envs['RADARR_MOVIE_TITLE']} has been Grabbed."
    elif eventtype == "Download" and envs['RADARR_ISUPGRADE'] != "True":
        mes = f"A file for {envs['RADARR_MOVIE_TITLE']} has been Downloaded."
    elif eventtype == "Download" and envs['RADARR_ISUPGRADE'] == "True":
        mes = f"A file for {envs['RADARR_MOVIE_TITLE']} has been Upgraded."
    else:
        raise Exception('Something went wrong lol')

elif "SONARR_EVENTTYPE" in envs:
    ico = SONARR_ICO
    title = "Sonarr"

    eventtype = envs['SONARR_EVENTTYPE']
    if eventtype == "Rename":
        mes = f"Some files for {envs['SONARR_SERIES_TITLE']} have been Renamed."
    elif eventtype == "Grab":
        mes = f"{envs['SONARR_RELEASE_EPISODECOUNT']} files for {envs['SONARR_SERIES_TITLE']} have been Grabbed."
    elif eventtype == "Download" and envs['RADARR_ISUPGRADE'] != "True":
        mes = f"{envs['SONARR_EPISODEFILE_EPISODECOUNT']} files for {envs['SONARR_SERIES_TITLE']} have been Downloaded."
    elif eventtype == "Download" and envs['RADARR_ISUPGRADE'] == "True":
        mes = f"{envs['SONARR_EPISODEFILE_EPISODECOUNT']} files for {envs['SONARR_SERIES_TITLE']} have been Upgraded."
    else:
        raise Exception('Something went wrong lol')

	
notification.notify(title=title, 
    message=mes,
    app_icon=ico)
