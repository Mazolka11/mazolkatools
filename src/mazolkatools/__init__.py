"""
MazolkaTools — набор утилит для работы со строками, файлами и базовыми операциями.

Основные возможности:
- Обработка и анализ строк
- Работа с файловой системой
- Вспомогательные функции для повседневных задач
"""

# Метаданные библиотеки
version = "0.1.0"
author = "Mazolka11"
license = "MIT"
url = "https://github.com/Mazolka11/mazolkatools"
description = "Утилиты для Python: строки, файлы, вспомогательные функции."

# Экспорт при from mazolkatools import *
all = [
    "reverse_string",
    "count_vowels",
    "is_palindrome",
    "read_file",
    "write_file",
    "list_files",
    # Добавьте сюда другие функции, которые хотите сделать публичными
]

# Импорт ключевых функций из подмодулей
try:
    from mazolkatools.formating import (
        isinstance,
        to_kebab_case,
        isinstance,
    )
    from mazolkatools.cleaning import (
        remove_whitespace,
        remove_punctuation,
        isinstance,
    )
    from mazolkatools.analysis import (
        word_count,
        char_count,
        top_words
    )
    # Если есть другие модули, добавьте их здесь
    # from .other_module import some_function
except ImportError as e:
    raise ImportError(f"Ошибка при загрузке модулей MazolkaTools: {e}")

# Опциональное приветствие при импорте (можно убрать)
if __name__ == "__main__":
    print(f"MazolkaTools {version} загружен.")