#import os
#import paramiko

from paramiko import SSHClient
from scp import SCPClient

def newLocal(server, localpath, remotepath):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(server)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(localpath, remotepath)
        #scp.get('test2.txt')

def localTest(server, username, password, localpath, remotepath):
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()

def mytest():
    server='10.75.20.75'
    localpath='testLLL.txt'
    remotepath='Downloads'
    username='lava'
    password='lava'
    #localTest(server, username, password, localpath, remotepath)
    newLocal(server, localpath, remotepath)

mytest()    
