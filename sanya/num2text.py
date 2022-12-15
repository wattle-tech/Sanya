#Перевод int, на русский язык


__all__=("NumConvert")
class NumConvert:
    def __positive_numbers(self, num: int):
        d = { 0 : 'ноль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
            6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять', 10 : 'десять',
            11 : 'одиннадцать', 12 : 'двеннадцать', 13 : 'тринадцать', 14 : 'четырнадцать',
            15 : 'пятнадцать', 16 : 'шестнадцать', 17 : 'семнадцать', 18 : 'восемнадцать',
            19 : 'девятнадцать', 20 : 'двадцать',
            30 : 'тридцать', 40 : 'сорок', 50 : 'пятьдесят', 60 : 'шестьдесят',
            70 : 'семьдесят', 80 : 'восемьдесят', 90 : 'девяносто' }
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert(0 <= num)

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0: return d[num]
            else: return d[num // 10 * 10] + '-' + d[num % 10]

        if (num < k):
            if num % 100 == 0: return d[num // 100] + ' сто'
            else: return d[num // 100] + ' сто ' + self.positive_numbers(num % 100)

        if (num < m):
            if num % k == 0: return self.positive_numbers(num // k) + ' тысяча'
            else: return self.positive_numbers(num // k) + ' тысяча, ' + self.positive_numbers(num % k)

        if (num < b):
            if (num % m) == 0: return self.positive_numbers(num // m) + ' миллион'
            else: return self.positive_numbers(num // m) + ' миллион, ' + self.positive_numbers(num % m)

        if (num < t):
            if (num % b) == 0: return self.positive_numbers(num // b) + ' миллиард'
            else: return self.positive_numbers(num // b) + ' миллиард, ' + self.positive_numbers(num % b)

        if (num % t == 0): return self.positive_numbers(num // t) + ' трилион'
        else: 
            return self.positive_numbers(num // t) + ' трилион, ' + self.positive_numbers(num % t)
    
    def negative_number(self, num: int):
        if num > 0:
            return str(self.__positive_numbers(num))
        if num < 0:
            comb = "минус " + str(self.__positive_numbers(num))
            return comb
