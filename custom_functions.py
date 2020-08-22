from KuveytSpyder import KuveytSpyder
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def make_spyder():

    url = "https://www.kuveytturk.com.tr/finans-portali/"

    options = FirefoxOptions()
    options.headless = False

    spyder = KuveytSpyder(url=url, options=options)

    return spyder