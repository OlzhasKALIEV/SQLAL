import random

adresa_employee = {
    "г.Москва": [
        "Адмирала Лазарева, улица",
        "Адмирала Макарова, улица",
        "Адмирала Руднева, улица",
        "Железногорская 1-я, улица",
    ],
    "г.Омск": [
        "Авангардная улица",
        "Улица Авиагородок",
        "Авиационная улица",
        "Авиационный переулок"
    ],
    "г.Новокузнецк":[
        "Плунжерная улица",
        "Улица Победы",
        "Погрузочная улица",
        "Подольская улица",
        "Речная улица",
        "Ровный переулок",
        "Улица Розы Люксембург",
        "Российская улица",
        "Ростовская улица"
    ]
}


def city():
    tt = random.choice(list(adresa_employee))
    for i in adresa_employee[tt]:
        adres = tt + ', ' + i
        return f'{adres}'


t = city()
print(t)
