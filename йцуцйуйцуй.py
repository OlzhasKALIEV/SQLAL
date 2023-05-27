import random
from datetime import datetime

d1 = datetime.strptime("01/01/2001", "%d/%m/%Y")
d3 = datetime.strptime("01/01/2021", "%d/%m/%Y")

d2 = datetime.strptime("01/01/2001", "%d/%m/%Y")
if (d1 <= d2 <= d3):
    print(random.randint(0, 100))

# start_dt = DT.strptime('01.01.2017', '%d.%m.%Y')
# end_dt = DT.strptime('01.01.2018', '%d.%m.%Y')
#
# for i in range(2):
#     print(get_random_date())


# spisok_surname = [
#     "Ершов",
#     "Никитин",
#     "Соболев",
#     "Рябов",
#     "Поляков",
#     "Цветков",
#     "Данилов",
#     "Жуков",
#     "Фролов",
#     "Журавлёв",
#     "Николаев"
# ]
#
# for i in range(5):
#     r = random.randint(1, len(spisok_surname) - 1)
#     print(spisok_surname[r])
