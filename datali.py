import random

spisok_name = [
    "Вавила",
    "Вадим",
    "Валентин",
    "Валерий",
    "Валерьян",
    "Варлам",
    "Варсонофий",
    "Семён",
    "Серафим",
    "Сергей",
    "Созон",
    "Софрон",
    "Спиридон",
    "Станислав",
    "Степан"
]

spisok_surname = [
    "Ларионов",
    "Федосеев",
    "Зимин",
    "Пахомов",
    "Шубин",
    "Игнатов",
    "Филатов",
    "Крюков",
    "Рогов",
    "Кулаков",
    "Терентьев",
    "Артемьев",
    "Гурьев",
    "Зиновьев",
    "Гришин"
]

number = random.randint(0, len(spisok_name) - 1)


def surname():
    spisok = []
    while len(spisok) != number:
        for i in range(len(spisok_surname)):
            t = random.randint(0, len(spisok_surname) - 1)
            if spisok_surname[t] not in spisok:
                spisok.append(spisok_surname[t])
        return spisok


def name():
    spisok = []
    while len(spisok) != number:
        for i in range(len(spisok_name)):
            t = random.randint(0, len(spisok_name) - 1)
            if spisok_name[t] not in spisok:
                spisok.append(spisok_name[t])
        return spisok


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
    "г.Новокузнецк": [
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
    spisok = []
    tt = random.choice(list(adresa_employee))
    while len(spisok) != number:
        for i in adresa_employee[tt]:
            adres = tt + ', ' + i
            if adres not in spisok:
                spisok.append(adres)
            tt = random.choice(list(adresa_employee))
        return spisok

