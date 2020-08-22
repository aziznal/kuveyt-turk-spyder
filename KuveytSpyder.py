from BankSpyder import BankSpyder
from bs4 import BeautifulSoup


class KuveytSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_rates_list(self):

        top_container = self.page_soup.find('div', {'class': 'finans-portali'})
        rates_container = top_container.find('div', {'class': 'container'})
        rates = rates_container.find('div', {'class': 'row'})

        rates_list = rates.findChildren(name='div', recursive=False)

        return rates_list

    def _extract_values(self, rates_list):
        pass

    def _get_usd(self, extracted_values):
        pass

    def get_single_reading(self):

        rates_list = self._get_rates_list()

        print("Got rates list!")
        print(f"Found {len(rates_list)} elements")

        extracted_values = self._extract_values(rates_list)

        usd_value = self._get_usd(extracted_values)

        return usd_value