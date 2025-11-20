from exceptions import InvalidTextError
import re


def remove_whitespace(text: str) -> str:
    """
    Удаляет лишние пробелы: в начале, конце и заменяет множественные пробелы внутри строки на одиночный.
    
    Параметры:
        text (str): входная строка для обработки.
        
    Возвращает:
        str: строка без избыточных пробелов.
        
    Исключения:
        InvalidTextError: если аргумент не является строкой.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    
    return re.sub(r'\s+', ' ', text.strip())



def remove_punctuation(text: str, keep: str = "") -> str:
    """
    Удаляет знаки пунктуации, оставляя только буквенно‑цифровые символы, пробелы и указанные в keep символы.
    
    Параметры:
        text (str): входная строка.
        keep (str): строка с символами, которые следует сохранить (по умолчанию — пустая).
        
    Возвращает:
        str: очищенная от пунктуации строка.
        
    Исключения:
        InvalidTextError: если аргумент не является строкой.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    
    # Экранируем специальные символы в keep и формируем шаблон
    escaped_keep = re.escape(keep)
    pattern = f'[^\\w\\s{escaped_keep}]'
    
    return re.sub(pattern, '', text)



def normalize_spaces(text: str) -> str:
    """
    Заменяет все пробельные символы (\t, \n, \r и др.) на обычный пробел и нормализует пробелы.
    
    Параметры:
        text (str): входная строка.
        
    Возвращает:
        str: строка с нормализованными пробелами.
        
    Исключения:
        InvalidTextError: если аргумент не является строкой.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    
    # Заменяем все пробельные символы на пробел
    normalized = re.sub(r'\s', ' ', text)
    # Убираем множественные пробелы и обрезаем края
    return re.sub(r' +', ' ', normalized).strip()


def remove_digits(text: str) -> str:
    """
    Удаляет все цифровые символы из строки.
    
    Параметры:
        text (str): входная строка.
        
    Возвращает:
        str: строка без цифр.
        
    Исключения:
        InvalidTextError: если аргумент не является строкой.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    
    return re.sub(r'\d', '', text)


def remove_special_chars(text: str, keep: str = "") -> str:
    """
    Удаляет специальные символы, оставляя буквы, цифры, пробелы и указанные в keep символы.
    
    
    Параметры:
        text (str): входная строка.
        keep (str): строка с символами, которые следует сохранить.
        
    Возвращает:
        str: строка без специальных символов.
        
    Исключения:
        InvalidTextError: если аргумент не является строкой.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    
    escaped_keep = re.escape(keep)
    pattern = f'[^a-zA-Za-яА-ЯёЁ0-9\\s{escaped_keep}]'
    return re.sub(pattern, '', text)