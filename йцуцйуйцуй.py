import random
from datetime import datetime as DT
from datetime import timedelta


def get_random_date():
    delta = DT.strptime('01.01.2018', '%d.%m.%Y') - DT.strptime('01.01.2017', '%d.%m.%Y')
    return DT.strptime('01.01.2017', '%d.%m.%Y') + timedelta(random.randint(0, delta.days))


start_dt = DT.strptime('01.01.2017', '%d.%m.%Y')
end_dt = DT.strptime('01.01.2018', '%d.%m.%Y')

for _ in range(2):
    print(get_random_date())




spisok_surname = [
    "Ершов",
    "Никитин",
    "Соболев",
    "Рябов",
    "Поляков",
    "Цветков",
    "Данилов",
    "Жуков",
    "Фролов",
    "Журавлёв",
    "Николаев"
]

for i in range(5):
    r = random.randint(1, len(spisok_surname)-1)
    print(spisok_surname[r])
