class TextToolsError(Exception):
    """Базовое исключение библиотеки texttools."""
    pass

class InvalidTextError(TextToolsError):
    """Исключение, если в функцию передано не строковое значение."""
    pass