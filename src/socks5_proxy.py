import paramiko
from sshtunnel import SSHTunnelForwarder
import os

# Configuración de conexión SSH
SSH_HOST = '<placeholder>'
SSH_PORT = 22
SSH_USER = '<placeholder>'
SSH_KEY_PATH = os.path.expanduser('~/.ssh/key.pem')

# Configuración del Proxy SOCKS5
LOCAL_PORT = 1080

def start_socks5_proxy():
    # Crear el cliente SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Conectar usando la clave privada
    ssh_client.connect(
        hostname=SSH_HOST,
        port=SSH_PORT,
        username=SSH_USER,
        key_filename=SSH_KEY_PATH
    )

    # Configurar el túnel SOCKS5
    with SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_username=SSH_USER,
        ssh_pkey=SSH_KEY_PATH,
        remote_bind_address=('127.0.0.1', 22),
        local_bind_address=('127.0.0.1', LOCAL_PORT),
        set_keepalive=30.0
    ) as tunnel:
        print(f"SOCKS5 proxy iniciado en 127.0.0.1:{LOCAL_PORT}")
        tunnel.start()
        tunnel.join()

if __name__ == "__main__":
    start_socks5_proxy()
