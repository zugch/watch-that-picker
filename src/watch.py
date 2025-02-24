import requests
from bs4 import BeautifulSoup
import logging
import os
import hashlib
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# URL und Element-Selektor aus Umgebungsvariablen
URL = os.getenv("SCRAPE_URL", "https://example.com")
ELEMENT_SELECTOR = os.getenv("ELEMENT_SELECTOR", "h1")
CRON_EXPRESSION = os.getenv("CRON_EXPRESSION", "*/5 * * * *")  # Default: alle 5 Minuten

scheduler = BlockingScheduler()

def watch_that():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        element = soup.select_one(ELEMENT_SELECTOR)
        
        if element:
            logging.info(f"Gefundenes Element ({ELEMENT_SELECTOR}): {element}")
            logging.info(f"Text des Resultats: ({ELEMENT_SELECTOR}): {element.text.strip()}")
            logging.info(f"Hash des Resultats: {hashlib.sha256(element.encode()).hexdigest()}")
        else:
            logging.warning(f"Kein Element mit dem Selektor '{ELEMENT_SELECTOR}' gefunden.")
    except requests.RequestException as e:
        logging.error(f"Fehler beim Abrufen der URL: {e}")

# Job mit CronTrigger hinzufügen
scheduler.add_job(watch_that, CronTrigger.from_crontab(CRON_EXPRESSION))

if __name__ == "__main__":
    logging.info(f"Starte Scheduler mit Cron-Ausdruck: {CRON_EXPRESSION}")
    scheduler.start()
