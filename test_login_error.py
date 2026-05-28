from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:5500/login.html")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.ID, "correo").send_keys("linaportela2002@gmail.com")

driver.find_element(By.ID, "contrasena").send_keys("incorrecta")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

# CAPTURAR ALERTA
alerta = driver.switch_to.alert

print("Mensaje alerta:", alerta.text)

alerta.accept()

time.sleep(2)

# Nombre automático con fecha y hora
nombre_archivo = f"CP-004_Login_Error_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S.png')}.png"

ruta = fr"C:\Users\porte\OneDrive\Pictures\Screenshots 1\{nombre_archivo}"

# Screenshot evidencia
driver.save_screenshot(ruta)

print(f"Captura guardada en: {ruta}")

driver.quit()