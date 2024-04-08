import paramiko
import socket
from datetime import datetime 
import os

class iLikeTo():
    def __init__(self, hostname, username, keyFile, port):
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.keyfile = keyFile
        self.port = port

        try:
            # Create socket
            sock = socket.create_connection((hostname,port))
            # Get the sftp connection object
            param_transport = paramiko.Transport(sock)
            param_connect = param_transport.connect(
                username=self.username,
                pkey=paramiko.RSAKey.from_private_key_file(self.keyfile)
            )
            param_channel = param_transport.open_channel("session")
            param_channel.invoke_subsystem("sftp")

            self.connection = paramiko.SFTPClient(param_channel)


        except Exception as err:
            raise Exception(err)

    def __del__(self):
        if self.connect != None:
            self.connection.close()

    def moveIt(self, domains: list):
        for domain in domains:
            try:
                print(
                    f"uploading to {self.hostname} as {self.username}"
                )
                date = datetime.today().strftime('%Y-%m-%d')

                # Download file from SFTP
                self.connection.mkdir("certs/"+date+"/")
                self.connection.put("/etc/letsencrypt/live/"+domain+"-"+date+"/privkey.pem", "certs/"+date+"/")
                self.connection.put("/etc/letsencrypt/live/"+domain+"-"+date+"/fullchain.pem", "certs/"+date+"/")
                print("upload completed")

            except Exception as err:
                raise Exception(err)
    

    
        