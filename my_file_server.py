import paramiko
import os
from paramiko import SSHClient
from scp import SCPClient

ip = '103.125.216.210'
username = 'Administrator'
password = 'Qn0KShci5Q14'

ssh = paramiko.SSHClient()  #ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port=22, username=username, password=password)

ftp = ssh.open_sftp()
ftp.chdir(r"C:\Users\Administrator\loader\data\2023-03-11\Binance")
fileList = ftp.listdir()
file_name = fileList[0]
currentDir = ftp.getcwd()
path_dir = currentDir[1:]
print(path_dir)

with SCPClient(ssh.get_transport()) as scp:
    scp.put(file_name, recursive=True, remote_path=path_dir)
    # scp.get('..btcusdt@trade.csv', recursive=True)

ssh.close()
