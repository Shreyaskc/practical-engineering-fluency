def report(db,tenant):
    return db.execute('SELECT id,amount FROM orders WHERE tenant=? AND status=? ORDER BY id',(tenant,'open')).fetchall()
def optimize(db):
    db.execute('CREATE INDEX IF NOT EXISTS orders_tenant_status ON orders(tenant,status)')
