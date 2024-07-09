import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Class.logger import Logger  # Assurez-vous que l'importation est correcte
from Class.cookies import CookieHandler

logger = Logger()


# Récupère les variables d'environnement pour le Selenium Hub
selenium_hub_host = os.getenv('SELENIUM_HUB_HOST', 'selenium')
selenium_hub_port = os.getenv('SELENIUM_HUB_PORT', '4444')

# Configure les options de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Exécute Chrome en mode headless (sans interface graphique)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--verbose")
chrome_options.add_argument("--log-level=0")

# Fonction pour vérifier la disponibilité du Selenium Grid
def wait_for_selenium_grid(host, port, timeout=60):
    url = f'http://{host}:{port}/wd/hub/status'
    for _ in range(timeout):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logger.log("access-selenium", "Selenium Grid est prêt.")
                print("Selenium Grid est prêt.")
                return True
        except requests.ConnectionError as e:
            # logger.log("error-selenium", f"Erreur de connexion selenium :{e}" )
            pass
        logger.log("log-selenium", "En attente de Selenium Grid...")
        print("En attente de Selenium Grid...")
        time.sleep(1)
    logger.log("error-selenium", "Selenium Grid n'est pas prêt après plusieurs tentatives")
    raise Exception("Selenium Grid n'est pas prêt après plusieurs tentatives")

# Vérifie que le Selenium Grid est prêt
wait_for_selenium_grid(selenium_hub_host, selenium_hub_port)

# Initialiser le WebDriver pour se connecter au Selenium Grid
for attempt in range(10):
    try:
        driver = webdriver.Remote(
            command_executor=f'http://{selenium_hub_host}:{selenium_hub_port}/wd/hub',
            options=chrome_options
        )
        logger.log("access-selenium", "Connexion au Selenium Grid réussie.")
        print("Connexion au Selenium Grid réussie.")
        break
    except Exception as e:
        logger.log("error-selenium", f"Tentative {attempt + 1}: Selenium Grid n'est pas prêt, attente... Erreur: {e}")
        print(f"Tentative {attempt + 1}: Selenium Grid n'est pas prêt, attente... Erreur: {e}")
        time.sleep(5)
else:
    logger.log("error-selenium", "Selenium Grid n'est pas prêt après plusieurs tentatives")
    raise Exception("Selenium Grid n'est pas prêt après plusieurs tentatives")

# Ouvre la page d'accueil de openclassrooms
try:
    driver.get('https://openclassrooms.com/fr/')
    logger.log("access-openclassrooms", "Félicitations ! L'accès à l'URL a été réussi.")
    print("Félicitations ! L'accès à l'URL a été réussi.")
except Exception as e:
    logger.log("error-openclassrooms", f"Erreur lors de l'accès à l'URL: {e}")
    print("Erreur lors de l'accès à l'URL:", e)
    driver.quit()
    raise

# Attendre que les éléments se chargent
time.sleep(2)
cookies = CookieHandler(driver)
cookies.decline_cookies()

# Ferme le WebDriver
logger.log("access-selenium", "Fermeture du WebDriver.")
logger.log("success", "Fermeture du WebDriver.")
driver.quit()
