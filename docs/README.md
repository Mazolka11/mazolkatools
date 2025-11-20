# mazolkatools

Библиотека для быстрой обработки текстовых данных: очистка, форматирование и базовая аналитика строк.

## Что делает библиотека

mazolkatools предоставляет набор инструментов для:
- очистки текста (удаление лишних пробелов, пунктуации, нормализация разделителей);
- форматирования (преобразование в snake_case, kebab-case, капитализация предложений);
- аналитики (подсчёт слов/символов, поиск самых частых слов).

## Примеры использования

```python
from texttools.cleaning import remove_whitespace, remove_punctuation
from texttools.formatting import to_snake_case, capitalize_sentences
from texttools.analysis import word_count, top_words

# Очистка текста
clean = remove_whitespace("  Hello,   world!  ")
clean = remove_punctuation(clean, keep="!")
print(clean)  # "Hello world!"

# Форматирование
snake = to_snake_case("User Name")
print(snake)  # "user_name"

capitalized = capitalize_sentences("hello. how are you?")
print(capitalized)  # "Hello. How are you?"

# Аналитика
words = word_count("One two three")
print(words)  # 3

top = top_words("apple banana apple cherry", n=2)
print(top)  # [("apple", 2), ("banana", 1)]