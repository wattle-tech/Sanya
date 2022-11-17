import sqlite3
import time

db = sqlite3.connect("./data/db.db")
cr = db.cursor()

class AlarmClock: #создаём класс

    @classmethod
    def add(cls, name: str, time: int, sound_path: str = None):
        cr.execute("INSERT INTO clock (name, time, sound) VALUES (?,?,?)", #в таюлицу clock добавляем name, time, sound
                [name, time, sound_path]) #Добавляем в бд данные
        db.commit()

    @classmethod
    def get_clocks(cls):
        clocks = cr.execute("SELECT name FROM clock") #получаем все данные из столбца name
        return clocks 


