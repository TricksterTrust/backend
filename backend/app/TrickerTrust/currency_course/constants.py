class Result:
    CURRENCY_DESCRIPTION: str = "Возвращает список объектов с валютами."
    CURRENCY_OBJECT: dict = {
        "currencies": {"description": "Список с объектами хранящими код, значение, флаг и важность валюты",
                       "type": "Array[Object[id, value, flag, code, primary]]"}}
    EXCHANGE_DESCRIPTION: str = "Возвращает объект с переведенным значением"
    EXCHANGE_OBJECT: dict = {"value": {"description": "Объект со значением", "type": "Object[value]"}}


class Params:
    CODE_TO_DESCRIPTION: str = "Код страны из валюты которой нужно перевести значение"
    CODE_FROM_DESC: str = "Код страны в валюту которой нужно перевести значение"
    VALUE_DESCRIPTION: str = "Значение, которое нужно перевести"
    VALUE_WARNING: str = "По-умолчанию \"1\""


class Description:
    CURRENCY_DESCRIPTION: str = "Позволяет получить список всех валют"
    CURRENCY_WARNING: str = "Все валюты указаны по отношению к рублям"
    EXCHANGE_DESCRIPTION: str = "Возвращает переведенное значение из первой переданной валюты во вторую"


class Error:
    CODE_NOT_FOUND: str = "Код не найден"
    METHOD_NOT_FOUND: str = "Метод не найден"
