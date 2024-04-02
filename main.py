from certbot_interactor import *
from sftp_mover import *

domains = input("Insert domain names (comma separated) : ").split(",") # get domain names to work with
sftp_param = input("Insert sftp parameters : hostname, username, privkey,  port (comma separated) : ").split(",")

certInt.newCert(domains)

sftp_move = iLikeTo("hugoravard.fr", "cert_delivery", "/home/"+sftp_param[1]+"/.ssh/id_rsa", 50004)
sftp_move.moveIt(domains)

del sftp_move
