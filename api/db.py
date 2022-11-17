import sqlite3
import time

db = sqlite3.connect("./data/db.db")
cr = db.cursor()

class AlarmClock:

    @classmethod
    def add(cls, name: str, time: int, sound_path: str = None):
        cr.execute("INSERT INTO clock (name, time, sound) VALUES (?,?,?)",
                [name, time, sound_path])
        db.commit()

    @classmethod
    def get_clocks(cls):
        clocks = cr.execute("SELECT name FROM clock")
        return clocks


