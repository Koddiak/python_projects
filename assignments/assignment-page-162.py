import sqlite3

conn = sqlite3.connect('myDb.db')
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files( \
                 file_id INTEGER PRIMARY KEY AUTOINCREMENT, \
                 file_txt_type TEXT \
                 )')
    conn.commit()
    
    for x in fileList:
        if x.endswith('.txt'):
            cur.execute('INSERT INTO tbl_files(file_txt_type) VALUES (?)', (x,))
            conn.commit()
    
    cur.execute('SELECT file_txt_type FROM tbl_files')
    txtFiles = cur.fetchall()
    print('All .txt files currently in the directory: \n')
    i = 1
    for file in txtFiles:
        msg = 'File {}: {}'.format(i, file[0])
        print(msg)
        i += 1
conn.close()
