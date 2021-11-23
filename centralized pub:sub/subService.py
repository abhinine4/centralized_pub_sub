import sqlite3

class SubService:

    def subscribe(sid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT sid FROM subscriber WHERE sid = ? AND eid = ?", (sid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET subscription = 1 WHERE sid = ? AND eid = ?", (sid, eid))
        else:
            c.execute("INSERT INTO subscriber VALUES(?,?,?,?)", (sid, eid, 1, 0))
        conn.commit()
        conn.close()
        return

    def unsubscribe(sid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT sid FROM subscriber WHERE sid = ? AND eid = ?", (sid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET subscription = 0 WHERE sid = ? AND eid = ?", (sid, eid))
        else:
            c.execute("INSERT INTO subscriber VALUES(?,?,?,?)", (sid, eid, 0, 0))
        conn.commit()
        conn.close()
        return

    def viewNotification(sid,eid):
        message = 'No new updates !'
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT * FROM subscriber WHERE sid = ? AND subscription = 1 AND notification = 1", (sid,))
        val = c.fetchall()
        if val:
            message = "You have new updates !"
        c.execute("UPDATE subscriber SET notification = 0 WHERE sid = ? AND eid = ?", (sid, eid))
        conn.commit()
        conn.close()
        return message

    def view(sid,eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT * FROM subscriber WHERE sid = ? AND eid = ? AND subscription = 1", (sid,eid,))
        val = c.fetchone()
        if val is None:
            updates = 'Not subscribed !'
        else:
            c.execute("SELECT eventData FROM eventBroker WHERE eid = ?", str(eid))
            updates = c.fetchone()
            updates = updates[0]
            conn.commit()
            conn.close()
        return updates
