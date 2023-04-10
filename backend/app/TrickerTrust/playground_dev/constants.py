class Result:
    RETRIEVE_DESCRIPTION: str = "Возвращает словарь, в котором params_type выводит всё, что принимает\\выдает эндпоинт, paths содержит все методы и URL для обращения"
    RETRIEVE_OBJECT: dict = {"params_type": {"description": "Список из всех элементов", "type": "Array[Dict[]]"},
                             "paths": {"description": "Все методы и эндпоинты", "type": "Array[Dict[]]"}}
    LIST_DESCRIPTION: str = "После успешного выполнения возвращает объект, содержащий словарь с категориями и списками методов"
    LIST_OBJECT: list = ["Object[str: Array[str]}"]


class Params:
    RETRIEVE_DESCRIPTION: str = "Нужный метод для выдачи информации"


class Description:
    RETRIEVE_DESCRIPTION: str = "Возвращает всю доступную информацию о переданном методе"
    LIST_DESCRIPTION: str = "Возвращает словарь содержащий все методы и их категории"


class Error:
    METHOD_NOT_FOUND: str = "Метод не найден"
