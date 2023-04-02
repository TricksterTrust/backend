import datetime

import requests
from celery import shared_task
from xml_to_dict import XMLtoDict

from currency_course.models import Currency

parser = XMLtoDict()
primary = {"USD": 10, "EUR": 9, "JPY": 7, "CNY": 5, "GBP": 8, "KZT": 6}
flags = {"AUD": "🇦🇺", "AZN": "🇦🇿", "GBP": "🇬🇧",
         "AMD": "🇦🇲", "BYN": "🇧🇾", "BGN": "🇧🇬",
         "BRL": "🇧🇷", "HUF": "🇭🇺", "VND": "🇻🇳",
         "HKD": "🇭🇰", "GEL": "🇬🇪", "DKK": "🇩🇰",
         "AED": "🇦🇪", "USD": "🇺🇸", "EUR": "🇪🇺",
         "EGP": "🇪🇬", "INR": "🇮🇳", "IDR": "🇮🇩",
         "KZT": "🇰🇿", "CAD": "🇨🇦", "QAR": "🇶🇦",
         "KGS": "🇰🇬", "CNY": "🇨🇳", "MDL": "🇲🇩",
         "NZD": "🇳🇿", "NOK": "🇳🇴", "PLN": "🇵🇱",
         "RON": "🇷🇴", "XDR": "🏳", "SGD": "🇸🇬",
         "TJS": "🇹🇯", "THB": "🇹🇭", "TRY": "🇹🇷",
         "TMT": "🇹🇲", "UZS": "🇺🇿", "UAH": "🇺🇦",
         "CZK": "🇨🇿", "SEK": "🇸🇪", "CHF": "🇨🇭",
         "RSD": "🇷🇸", "ZAR": "🇿🇦", "KRW": "🇰🇷",
         "JPY": "🇯🇵"}


def get_currencies_list():
    data = requests.get("https://www.cbr.ru/scripts/XML_daily.asp").text
    currencies = parser.parse(data)
    currencies_insert = [Currency(**{"code": currency["CharCode"],
                                     "value": round(
                                         float(currency["Value"].replace(",", ".")) / int(currency["Nominal"]), 2),
                                     "flag": flags[currency["CharCode"]],
                                     "primary": primary.get(currency["CharCode"], 0),
                                     "updated_at": datetime.datetime.now()})
                         for currency in currencies["ValCurs"]["Valute"]]
    return currencies_insert


@shared_task
def update_course():
    currencies = get_currencies_list()
    Currency.objects.bulk_create(currencies, update_conflicts=True, unique_fields=["code"], update_fields=["value", "updated_at"])
