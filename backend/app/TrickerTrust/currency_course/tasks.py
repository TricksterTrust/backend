import datetime

import requests
from celery import shared_task
from xml_to_dict import XMLtoDict

from currency_course.models import Currency

parser = XMLtoDict()
primary = {"USD": 7, "EUR": 6, "JPY": 5, "CNY": 4, "GBP": 3, "KZT": 2}
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
    now = datetime.datetime.now()
    currencies_insert = [Currency(**{"code": currency["CharCode"],
                                     "value": round(
                                         float(currency["Value"].replace(",", ".")) / int(currency["Nominal"]), 2),
                                     "flag": flags[currency["CharCode"]],
                                     "primary": primary.get(currency["CharCode"], 0),
                                     "updated_at": now})
                         for currency in currencies["ValCurs"]["Valute"]]
    currencies_insert.append(Currency(code="RUB", value=1.00, flag="🇷🇺", primary=8, updated_at=now))
    return currencies_insert


@shared_task
def update_course():
    currencies = get_currencies_list()
    Currency.objects.bulk_create(currencies, update_conflicts=True, unique_fields=["code"],
                                 update_fields=["value", "updated_at"])
