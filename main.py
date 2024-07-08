import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Récupère les variables d'environnement pour le Selenium Hub
selenium_hub_host = os.getenv('SELENIUM_HUB_HOST', 'selenium')
selenium_hub_port = os.getenv('SELENIUM_HUB_PORT', '4444')

# Configure les options de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Exécute Chrome en mode headless (sans interface graphique)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialise le WebDriver pour se connecter au Selenium Grid
driver = webdriver.Remote(
    command_executor=f'http://{selenium_hub_host}:{selenium_hub_port}/wd/hub',
    options=chrome_options
)

# Ouvre la page contenant le composant
driver.get('http://app:3000')  # Utilise le port 3000 pour l'URL de l'application

# Trouve le bouton par son texte
button = driver.find_element(By.XPATH, "//button[text()='Click Me']")

# Vérifie la couleur du bouton
assert button.value_of_css_property('background-color') == 'rgba(0, 0, 255, 1)', "Le bouton n'est pas bleu"

# Vérifie la taille du bouton
assert button.value_of_css_property('font-size') == '16px', "La taille de la police n'est pas correcte"
assert button.value_of_css_property('padding') == '10px 20px', "Le padding n'est pas correct"

# Redimensionne la fenêtre pour tester la responsivité
driver.set_window_size(500, 800)
button = driver.find_element(By.XPATH, "//button[text()='Click Me']")

# Vérifie la taille responsive du bouton
assert button.value_of_css_property('font-size') == '14px', "La taille de la police responsive n'est pas correcte"
assert button.value_of_css_property('padding') == '8px 16px', "Le padding responsive n'est pas correct"

# Ferme le WebDriver
driver.quit()
