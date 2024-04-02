import pysftp
from datetime import datetime 

class iLikeTo():
    def __init__(self, hostname, username, keyFile, port):
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.keyfile = keyFile
        self.port = port
        
        try:
            # Get the sftp connection object
            self.connection = pysftp.Connection(
                host=self.hostname,
                username=self.username,
                private_key=self.keyfile,
                port=self.port,
            )

        except Exception as err:
            raise Exception(err)
        finally:
            print(f"Connected to {self.hostname} as {self.username}.")

    def __del__(self):
        self.connection.close()

    def moveIt(self, domains: list):
        for domain in domains:
            try:
                print(
                    f"uploading to {self.hostname} as {self.username}"
                )
                date = datetime.today().strftime('%Y-%m-%d')

                # Download file from SFTP
                self.connection.put_r("/etc/letsencrypt/live/"+domain+"/privkey.pem", "certs/"+date+"privkey.pem")
                self.connection.put_r("/etc/letsencrypt/live/"+domain+"/fullchain.pem", "certs/"+date+"/fullchain.pem")
                print("upload completed")

            except Exception as err:
                raise Exception(err)
    

    
        