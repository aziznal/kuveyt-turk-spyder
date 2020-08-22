from BankSpyder import BankSpyder
from bs4 import BeautifulSoup

from CustomExceptions import *

class KuveytSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_rates_list(self):

        top_container = self.page_soup.find('div', {'class': 'finans-portali'})
        rates_container = top_container.find('div', {'class': 'container'})
        rates = rates_container.find('div', {'class': 'row'})

        rates_list = rates.findChildren(name='div', recursive=False)

        return rates_list

    @staticmethod
    def _get_currency_name(container: BeautifulSoup):

        raw_name_ = container.find(name='h2', recursive=False).text
        currency_name = raw_name_.split(' ')[0]
        return currency_name

    @staticmethod
    def _format_raw_values(raw_values: BeautifulSoup):
    
        clean_values = []

        # REFACTOR
        for value in raw_values:
            
            separator = ';'

            dirty_rate = value.find('p').getText(separator=separator)
            clean_rate = dirty_rate.split(separator)[0]

            clean_rate = clean_rate.strip().replace(',', '.')

            clean_values.append(float(clean_rate)) 

        return clean_values

    def _get_bank_rates(self, container: BeautifulSoup):
        
        raw_values = container.findChildren('div', {'class': 'cellbox insidebox'})

        values = self._format_raw_values(raw_values)

        bank_buys = min(values)
        bank_sells = max(values)

        return bank_buys, bank_sells

    def _extract_values(self, rates_list):

        for value in rates_list:
            top_container = value.find('div', {'class': 'box-borderless'})
            currency_name = self._get_currency_name(top_container)

            value_container = value.find('div', {'class': 'alphabox'})
            bank_buys, bank_sells = self._get_bank_rates(value_container)

            yield currency_name, bank_buys, bank_sells

    def _get_usd(self, extracted_values):
        for value in extracted_values:
            if value[0] == 'USD':
                return value

        raise CurrencyNotFoundException("Couldn't find the currency USD")

    def get_single_reading(self):

        rates_list = self._get_rates_list()

        extracted_values = self._extract_values(rates_list)

        usd_value = self._get_usd(extracted_values)

        return usd_value