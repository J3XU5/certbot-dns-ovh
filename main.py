from certbot_interactor import *
from sftp_mover import *

#domains = input("Insert domain names (comma separated) : ").split(",") # get domain names to work with
#sftp_param = input("Insert sftp parameters : hostname, username, privkey, port (comma separated) : ").split(",")

param = open("./param",'r').readlines()

domains = param[1].split(",")
for domain in domains:
    domain.rsplit("\n") #to remove \n on last domain name

sftp_param = param[2].split(",")
for sftp_parameter in sftp_param:
    sftp_parameter.rsplit("\n") #to remove \n on last param name

certInt.newCert(domains)

sftp_move = iLikeTo(sftp_param[0], sftp_param[1], sftp_param[2], sftp_param[3])
sftp_move.moveIt(domains)

exit(0)
