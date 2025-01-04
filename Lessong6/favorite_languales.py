"""
Опрос. Возьмите за основу код программы favorite_languales.py из подраздела 
"Словарь с однотипными объектами" данной главы. 

1. Создайте список людей, которые должны учавствовать в опросе по поводу 
любимого языка программирования. Добавте имена, которые уже существуют в с
писке, и имена, которых еще нет.

2. Переберите список людей, которые должны учавствовать в опросе. Если они уже 
прошли его, то выведите сообщение с благодарностью за участие. Если ещё не проходили,
то выведите сообщение с предложением принять участвие. 

"""

# Словарь с любимыми языками программирования
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Список людей для опроса
survey_list = ['jen', 'alex', 'sarah', 'maria', 'phil', 'john']

# Перебор списка людей
for person in survey_list:
    if person in favorite_languages:
        print(f"Спасибо, {person.title()}, за участие в опросе!")
    else:
        print(f"{person.title()}, приглашаем вас принять участие в опросе о любимом языке программирования!")

print("\n")