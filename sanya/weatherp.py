import random

plusforty = ["одевайтесь легче", "можете сходить на пляж. А нет, отмена, река пересохла.", "Кстати, а что если выйти на улицу голым? Сейчас проверим!", "жарковато, не находите?"]
plustwentyfive = ["время для летней майки!", "ну что, идёте открывать купальный сезон?", "жарковато..."]
plustwenty = ["ну вот и потеплело!", "одевайтесь легче."]
plusten = ["накиньте что нибудь", "у вас же была желетка?", "прямо как в Лондоне!", "как на счёт осеннего пальто?"]
plusfive = ["лучше одется потеплее", "накиньте что нибудь", "одевайтесь потеплее", "холодновато"]
pluszero = ["лучше надеть куртку", "наденьте шарф и шапку", "надеюсь у вас есть куртка?"]
belowzerofive = ["уже не лето, не забудь про куртку", "не превратись в сосульку!", "одевайся теплее", "у тебя же есть куртка?", "замёрзнешь!"]


def weatherrequest (num: int):
    if num <= -5:
        v = random.randrange(0, len(belowzerofive))
        return belowzerofive[v]

    if num <= 5 and num > -5:
        v = random.randrange(0, len(pluszero))
        return pluszero[v]
    
    if num >= 5 and num < 10:
        v = random.randrange(0, len(plusfive))
        return plusfive[v]

    if num >= 10 and num < 20:
        v = random.randrange(0, len(plusten))
        return plusten[v]

    if num >= 20 and num < 25:
        v = random.randrange(0, len(plustwenty))
        return plustwenty[v]

    if num >= 25 and num < 40:
        v = random.randrange(0, len(plustwentyfive))
        return plustwentyfive[v]

    if num >= 40:
        v = random.randrange(0, len(plusforty))
        return plusforty[v]

print(weatherrequest(int(input())))