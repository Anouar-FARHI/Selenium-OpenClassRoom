# Utiliser l'image officiel de Python
FROM python:3.8-slim

# Installer les dépendances Python nécessaires
RUN pip install selenium

# Installe wget, gnupg2 et unzip
RUN apt-get update && apt-get install -y wget gnupg2 unzip

# Installer chrome et ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg2 \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
  && apt-get update && apt-get install -y google-chrome-stable \
  && wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
  && rm chromedriver_linux64.zip

#   Définir le répertoire de travail dans le conteneur docker
WORKDIR /app

# Copier les fichiers du projet dans le répertoire de travail que l'on vien de créer
COPY . .

# Expose le port 3000
EXPOSE 3000

#Lancer les teste de l'application
CMD ["sh","-c","python main.py"]