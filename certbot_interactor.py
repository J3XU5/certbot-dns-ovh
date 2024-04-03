import subprocess

class certInt():
    def __init__(self) -> None:
        pass

    def newCert(domains: list):
        for domain in domains:
            subprocess.run(["sudo", "certbot" , "certonly", "--dns-ovh", 
                            "--dns-ovh-credentials $HOME/creds.ini", 
                            "--dns-ovh-propagation-seconds 60", 
                            "-d " + domain] 
                            , timeout=70)
            print("New cert for "+domain+" created")