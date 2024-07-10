from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Class.openclassrooms import OpenClassRoomsActions
from Class.logger import Logger

logger = Logger()

class OpenClassRoomsLogin(OpenClassRoomsActions):
    def __init__(self, driver, username, password):
        super().__init__(driver)
        self.username = username
        self.password  = password
        self.wait = WebDriverWait(driver, 10)

    def login(self):
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#header > div > div > div.sc-fnykZs.ceLBks.MuiBox-root > button')))
            login_button.click()

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-header-menu"]/a[2]')))
            login_button.click()
            
            email_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.sc-iFwKgL.sc-iJkHyd.ghOkCd.fwkEBX.MuiInputBase-input.MuiOutlinedInput-input')))
            email_field.send_keys(self.username)
            email_field.send_keys(Keys.ENTER)
            
            password_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.sc-iFwKgL.sc-iJkHyd.ghOkCd.ettpfn.MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedEnd')))
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.ENTER) 
            
            logger.log("log-openclassrooms", f"Vous êtes maintenant connecter avec le compte {self.username}")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors de la connexion sur OpenClassrooms : {e}")
