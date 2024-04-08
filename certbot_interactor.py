import subprocess
from datetime import datetime

class certInt():
    def __init__(self) -> None:
        pass

    def newCert(domains: list):
        date = datetime.today().strftime('%Y-%m-%d')
        for domain in domains:
            subprocess.run("sudo certbot certonly --dns-ovh --dns-ovh-credentials $HOME/creds.ini --dns-ovh-propagation-seconds 50 -d " + domain + " --cert-name " + domain + "-" + date
                            , timeout=70, shell=True, check=True)
            print("New cert for "+domain+" created")