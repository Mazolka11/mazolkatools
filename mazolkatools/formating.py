from exceptions import InvalidTextError
import re


def to_snake_case(text: str) -> str:
    """
    Преобразует строку в формат snake_case (нижний регистр, слова разделены подчёркиваниями).
    
    Параметры:
        text (str): входная строка для преобразования.
        
    Возвращает:
        str: строка в формате snake_case.
        
    Исключения:
        InvalidTextError: если передан не строковый аргумент.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")

    # Убираем знаки пунктуации и лишние пробелы
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    # Разбиваем на слова, приводим к нижнему регистру и соединяем подчёркиваниями
    words = cleaned_text.lower().split()
    snake_case = '_'.join(words)

    return snake_case


def to_kebab_case(text: str) -> str:
    """
    Преобразует строку в формат kebab-case (нижний регистр, слова разделены дефисами).
    
    Параметры:
        text (str): входная строка для преобразования.
        
    Возвращает:
        str: строка в формате kebab-case.
        
    Исключения:
        InvalidTextError: если передан не строковый аргумент.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")

    # Убираем знаки пунктуации и лишние пробелы
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    # Разбиваем на слова, приводим к нижнему регистру и соединяем дефисами
    words = cleaned_text.lower().split()
    kebab_case = '-'.join(words)

    return kebab_case


def capitalize_sentences(text: str) -> str:
    """
    Делает первую букву каждого предложения заглавной.
    Предложения определяются по знакам препинания: точка, восклицательный или вопросительный знак.
    
    Параметры:
        text (str): входная строка для преобразования.
        
    Возвращает:
        str: строка с заглавными первыми буквами в каждом предложении.
        
    Исключения:
        InvalidTextError: если передан не строковый аргумент.
    """
    if not isinstance(text, str):
        raise InvalidTextError(f"Ожидалась строка, получено {type(text).__name__}")

    if not text:
        return text

    # Разбиваем текст на предложения по знакам препинания
    sentences = re.split(r'([.!?])', text)
    result = []

    for i in range(0, len(sentences) - 1, 2):
        sentence = sentences[i].strip()
        punctuation = sentences[i + 1]

        if sentence:  # Если предложение не пустое
            capitalized_sentence = sentence[0].upper() + sentence[1:]
            result.append(capitalized_sentence + punctuation)
        else:
            result.append(punctuation)

    # Обрабатываем последнее предложение, если оно есть
    if len(sentences) % 2 == 1 and sentences[-1].strip():
        last_sentence = sentences[-1].strip()
        result.append(last_sentence[0].upper() + last_sentence[1:])

    return ''.join(result)