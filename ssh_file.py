import paramiko
import os
from paramiko import SSHClient
from scp import SCPClient

ip = 'ip'
username = 'username'
password = 'password'

ssh = paramiko.SSHClient()  #ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port=22, username=username, password=password)

_stdin, _stdout, _stderr = ssh.exec_command(r"cd C:\Users\OMATCH\Administrator\loader\data\2023-02-26\Binance")
for i in _stdout.read():
    print(i)
print(_stdout.read())
print(_stderr.read().decode())


with SCPClient(ssh.get_transport()) as scp:
    scp.put('btcusdt@trade.csv', recursive=True, remote_path=r'\loader\data\2023-02-26\Binance')
    scp.get('btcusdt@trade.csv', recursive=True)

ssh.close()
