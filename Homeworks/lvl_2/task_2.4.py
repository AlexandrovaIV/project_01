# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

s = 'Hi! Hello!'

# Вариант 1
def remove_exclamation_marks(s):
    s1 = s.replace('!', '')
    print('Вариант А')
    print('Вариант 1')
    print(s1)
    return s1

remove_exclamation_marks(s)

# Вариант 2
def remove_exclamation_marks(s):
    ss = s.split('!')
    nn = ''.join(ss)
    print('Вариант 2')
    print(nn)

remove_exclamation_marks(s)




# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!':
        return s[:-1]
    else:
        return s
print('Вариант В')
print(remove_last_em('Hi!'))
print(remove_last_em('Hi!!!'))
print(remove_last_em('!Hi'))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass