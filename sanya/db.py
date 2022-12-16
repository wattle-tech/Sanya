import sqlite3
import time
import playsound
import json


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
        clocks = cr.execute("SELECT * FROM clock") #получаем все данные из столбца name
        return clocks
    
    @classmethod
    def delete(cls, time):
        cr.execute("DELETE FROM clock WHERE time <= ?", [time])
        return db.commit()
    
    @classmethod
    def start(cls):
        # for playing ph_intr.mp3 file
        playsound.playsound('./data/sounds/clock.mp3')


class Timer:

    @classmethod
    def add(cls, time: int):
        cr.execute("INSERT INTO timer (time) VALUES (?)",[time]) #Добавляем в бд данные
        db.commit()

    @classmethod
    def get_clocks(cls):
        clocks = cr.execute("SELECT * FROM timer") #получаем все данные из столбца name
        return clocks
    
    @classmethod
    def delete(cls, time):
        cr.execute("DELETE FROM timer WHERE time <= ?", [time])
        return db.commit()
    
    @classmethod
    def start(cls):
        # for playing ph_intr.mp3 file
        playsound.playsound('./data/sounds/timer.mp3')

        

class Data:
    @classmethod
    def get(cls):
        with open(f'data/user.json', 'r') as f:
            file = json.load(f)
        return file
        

        

