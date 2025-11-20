from exceptions import InvalidTextError
from collections import Counter
import re

def word_count(text: str) -> int:
    """
    Подсчитывает количество слов в тексте.
    
    Параметры:
        text (str): входная строка для анализа.
        
    Возвращает:
        int: количество слов в строке.
        
    Исключения:
        InvalidTextError: если передан не строковый аргумент.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    # Нормализуем пробелы и разбиваем на слова
    words = re.findall(r'\b\w+\b', text.strip())
    return len(words)



def char_count(text: str, ignore_spaces: bool = False) -> int:
    """
    Подсчитывает количество символов в тексте.
    
    Параметры:
        text (str): входная строка для анализа.
        ignore_spaces (bool): если True, пробелы не учитываются в подсчёте.
        
    Возвращает:
        int: количество символов (с учётом или без учёта пробелов).
        
    Исключения:
        InvalidTextError: если передан не строковый аргумент.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    if ignore_spaces:
        # Удаляем все пробелы (включая табуляции, переносы)
        cleaned_text = re.sub(r'\s', '', text)
        return len(cleaned_text)
    else:
        return len(text)



def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """
    Возвращает список самых частых слов в тексте.
    
    Параметры:
        text (str): входная строка для анализа.
        n (int): количество возвращаемых самых частых слов (по умолчанию 3).
        
    Возвращает:
        list[tuple[str, int]]: список кортежей (слово, частота), отсортированный 
        по убыванию частоты. Если слов меньше, чем n, возвращает все.
        
    Исключения:
        InvalidTextError: если передан не строковый аргумент.
        ValueError: если n < 1.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")
    
    if n < 1:
        raise ValueError("Параметр n должен быть >= 1")
    
    # Очищаем текст: оставляем только слова, переводим в нижний регистр
    words = re.findall(r'\b[a-zA-Za-яА-ЯёЁ]+\b', text.lower())
    
    # Считаем частоту слов
    word_counter = Counter(words)
    
    # Возвращаем топ-n слов
    return word_counter.most_common(n)