from pathlib import Path

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#CAMINHO PARA RAIZ DO PROJETO
ROOT_FOLDER = Path(__file__).parent
#CAMINHO PARA A PASTA ONDE O CHROMEDRIVER ESTA
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

chrome_browser = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_service = Service()
