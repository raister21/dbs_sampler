

def mkexf(tablename,rows):
    tblsql = str(tablename + '.sql')
    w = open(tblsql,'w')
    i = 0
    for i in rows:
        w.write('INSERT INTO ' + tablename + 'VALUES (')
        w.write()