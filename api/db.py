import sqlite3
import time
import playsound


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
    
    @classmethod
    def delete(cls, time):
        cr.execute("DELETE FROM clock WHERE time <= ?", [time])
        return db.commit()
    
    @classmethod
    def start(cls):
        # for playing ph_intr.mp3 file
        playsound.playsound('./data/sounds/ph_intr.mp3')
        


