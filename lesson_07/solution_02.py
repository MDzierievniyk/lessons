"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
название города и выводит на печать страну.
"""

my_dict = {
    "Belarus":"Minsk",
    "Poland":"Warshawa",
    "Ukraine":"Kiev",
    "Lithuania":"Vilnus",
}
def country_of_city(city):
    for key, value in my_dict.items():
        if value == city:
            return key

print(country_of_city("Minsk"))
print(country_of_city("Warshawa"))
print(country_of_city("Kiev"))
print(country_of_city("Vilnus"))