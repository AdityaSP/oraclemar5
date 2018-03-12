import paramiko
import time

def open_ssh_conn(ip):
    username = 'vagrant'
    password = 'vagrant'
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
    session.connect(ip, username=username, password=password)
    connection = session.invoke_shell()
    output = connection.recv(65535)
    connection.send("free\n")
    time.sleep(1)
    output = connection.recv(65535)
    return output
    fh.write(output)
    session.close()

# Calling the SSH function
ips = ["192.168.33.10", "192.168.33.11"]
fh = open('log.txt', 'wt')
for ip in ips:
    output = open_ssh_conn(ip)
    fh.write(output)
fh.close()