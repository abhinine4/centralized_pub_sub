import requests
import sqlite3
import json


class Events:

    def eventService(eid):
        if eid == 1:
            headers = {
                'Accept': 'text/plain',
            }
            response = requests.get("https://icanhazdadjoke.com/", headers=headers)
            update = response.text
            conn = sqlite3.connect('pubsub.db')
            c = conn.cursor()
            c.execute("UPDATE eventBroker set eventData = ? WHERE eid = ?", (update, 1))
            conn.commit()
            conn.close()
        elif eid == 2:
            headers = {
                'Accept': 'text/plain',
            }
            response = requests.get("https://api.adviceslip.com/advice", headers=headers)
            jj = json.loads(response.text)
            update = jj['slip']['advice']
            conn = sqlite3.connect('pubsub.db')
            c = conn.cursor()
            c.execute("UPDATE eventBroker set eventData = ? WHERE eid = ?", (update, 2))
            conn.commit()
            conn.close()
        elif eid == 3:
            headers = {
                'Accept': 'text/plain',
            }
            response = requests.get("https://zenquotes.io/api/random", headers=headers)
            jj = json.loads(response.text)
            update = jj[0]['q']
            conn = sqlite3.connect('pubsub.db')
            c = conn.cursor()
            c.execute("UPDATE eventBroker set eventData = ? WHERE eid = ?", (update, 3))
            conn.commit()
            conn.close()
        return
