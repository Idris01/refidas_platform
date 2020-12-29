import os
from pathlib import Path
from django.test import TestCase Client

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



# Create your tests here
def file_uri(file):
    return Path(os.path.abspath(file)).as_uri()

