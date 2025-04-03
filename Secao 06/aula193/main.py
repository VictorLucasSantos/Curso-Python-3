from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
EDGEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "msedgedriver.exe"


def make_egde_browser(*options):
    edge_options = webdriver.EdgeOptions()

    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    egde_service = Service(executable_path=str(EDGEDRIVER_EXEC))

    browser = webdriver.Edge(service=egde_service, options=edge_options)

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    options = ()
    browser = make_egde_browser()
    browser.get("https://www.google.com.br")
    sleep(2)
    # Procurando input procurando o elemento com name "q", aguardando ele aparecer
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    sleep(1)
    # Digitar no elemento
    search_input.send_keys("Hello World")
    search_input.send_keys(Keys.ENTER)

    # sleep(1)
    # results = browser.find_element(By.ID, "search")
    # links = results.browser.find_element(By.TAG_NAME, "a")

    sleep(1)
    # links[0].click()
    sleep(TIME_TO_WAIT)
