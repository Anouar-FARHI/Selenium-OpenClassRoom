from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Class.logger import Logger

logger = Logger()

class CookieHandler:
    def __init__(self, driver):
        self.driver = driver
        
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="truste-consent-button"]'))
            ).click()
            logger.log("log-openclassrooms", "Les cookies ont bien été acceptés")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors de l'acceptation des cookies : {e}")
            
    def decline_cookies(self):
        try:
            decline_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="truste-consent-required"]'))
            )
            decline_button.click()
            logger.log("log-openclassrooms", "Les cookies ont bien été refusés")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors du refus des cookies : {e}")
