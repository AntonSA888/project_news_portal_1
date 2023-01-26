from django import template

censor = template.Library()


def lower(text):
    # Проверяем, что все буквы в слове, начиная со второй, прописные.
    if text[1:] != text[1:].lower():
        return False
    else:
        return True


def change_word(text):
    # Заменяем буквы в слове, начиная со второй, на '*'.
    word = text[0]
    for i in text:
        if i.isalpha():
            word += '*'
        else:
            word += i
    return word


def censor1(string):
    # Обрабатываем входящую строку и выводим новую с цензурой.
    if isinstance(string, str):
        split_ = string.split()
        list_ = []
        for i in split_:
            if not lower(i):
                list_.append(change_word(i))
            else:
                list_.append(i)
    return ' '.join(list_)


@censor.filter()
def mycenzor(value): # К этому названию нужно обращаться из шаблонов
    return {value}



