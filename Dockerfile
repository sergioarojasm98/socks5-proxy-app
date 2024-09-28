# Usar una imagen base de Python
FROM python:3.9-slim

# Instalar dependencias SSH
RUN apt-get update && apt-get install -y openssh-client

# Crear directorio para la app
WORKDIR /app

# Copiar el script Python y la llave SSH
COPY src/socks5_proxy.py /app/socks5_proxy.py
COPY ~/.ssh/my-aws-proxy-server-rsa-key.pem /root/.ssh/my-aws-proxy-server-rsa-key.pem

# Instalar las dependencias de Python
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Exponer el puerto 1080 para el proxy
EXPOSE 1080

# Ejecutar el script Python
CMD ["python", "/app/socks5_proxy.py"]
