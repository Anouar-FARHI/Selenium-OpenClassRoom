from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Class.logger import Logger

logger = Logger()

class ClosePopUp :
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def close_pop_up(self):
        try:
            print(f"Clicking button: {By.CSS_SELECTOR} {'body > div.sc-dIouRR.kMwfeN.sc-kgflAQ.jQCwPs.MuiDialog-root.MuiModal-root > div.sc-fLlhyt.jDOnlw.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.sc-lbOyJj.iOFAkR > div:nth-child(1) > button > svg > path'}")
            logger.log("access_OpenClassRoom", f"Clicking button: {By.CSS_SELECTOR} {'body > div.sc-dIouRR.kMwfeN.sc-kgflAQ.jQCwPs.MuiDialog-root.MuiModal-root > div.sc-fLlhyt.jDOnlw.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.sc-lbOyJj.iOFAkR > div:nth-child(1) > button > svg > path'}")
            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.sc-dIouRR.kMwfeN.sc-kgflAQ.jQCwPs.MuiDialog-root.MuiModal-root > div.sc-fLlhyt.jDOnlw.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.sc-lbOyJj.iOFAkR > div:nth-child(1) > button > svg > path')))
            button.click()
            logger.log("log-openclassrooms", f"Pop up bien fermé !")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur pour fermer le pop-up: {e}")