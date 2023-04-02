class Param:
    QUERY = "query"
    BODY = "body"
    PARAM = "param"


class Types:
    STRING = "string"


class Result:
    RETRIEVE_DESCRIPTION: str = "Возвращает словарь, в котором params_type выводит всё, что принимает\\выдает эндпоинт, paths содержит все методы и URL для обращения"
    LIST_DESCRIPTION: str = "После успешного выполнения возвращает объект, содержащий словарь с категориями и списками методов"


class Params:
    RETRIEVE_DESCRIPTION: str = "Нужный метод для выдачи информации"
    RETRIEVE_WARNING: str = "Без этой фигни ничего работать не будет!"


class Description:
    RETRIEVE_DESCRIPTION: str = "Возвращает всю доступную информацию о переданном методе"
    RETRIEVE_WARNING: str = "Денис, это временный текст, потом надо убрать"
    LIST_DESCRIPTION: str = "Возвращает словарь содержащий все методы и их категории"
    LIST_WARNING: str = "Ничего передавать не нужно! Денис, это временный текст, потом надо убрать"


class Error:
    METHOD_NOT_FOUND: str = "Метод не найден"
