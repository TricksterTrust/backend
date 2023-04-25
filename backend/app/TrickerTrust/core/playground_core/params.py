from typing import Any, Union


class Param:
    QUERY = "query"
    BODY = "body"
    PARAM = "param"


class Types:
    BOOL = "boolean"
    FLOAT = "float"
    STR = "string"
    INT = "integer"
    DATETIME = "datetime"


def required(name: str,
             name_type: str,
             param_type: str = "query",
             description: str = "",
             warning_description: str = "") -> dict:
    return {"name": name,
            "type": "required",
            "param_type": param_type,
            "description": description,
            "name_type": name_type,
            "warning_description": warning_description}


def optional(name: str,
             name_type: str,
             default: Any = None,
             param_type: str = "query",
             description: str = "",
             warning_description: str = "") -> dict:
    return {"name": name,
            "default": default,
            "type": "optional",
            "param_type": param_type,
            "description": description,
            "name_type": name_type,
            "warning_description": warning_description}


def description(text: str = "", warning_text: str = "") -> dict:
    return {"type": "description",
            "text": text,
            "warning_text": warning_text}


def error(code: int, description: str) -> dict:
    return {"type": "error",
            "code": code,
            "description": description}


def result(description: str = "", objects: Union[dict, list, None, str] = None, code: int = 200) -> dict:
    return {"type": "result",
            "description": description,
            "objects": str(objects),
            "code": code}
