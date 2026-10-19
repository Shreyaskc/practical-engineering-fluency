def report(db,tenant):
    rows=db.execute('SELECT id FROM orders WHERE tenant=? AND status=?',(tenant,'open')).fetchall()
    return [(i,db.execute('SELECT amount FROM orders WHERE id=?',(i,)).fetchone()[0]) for (i,) in rows]
def optimize(db): pass
