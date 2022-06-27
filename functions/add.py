from database import *

def simpanData(data):
    mycursor.execute("INSERT INTO founder (name, username,  company ,  contact , amount ,description) VALUES (%s, %s,%s, %s, %s, %s)", data)
    mydb.commit()

# nama company contact ammount description
def add(bot,message):
    mycursor.execute("SELECT * FROM founder WHERE username = %s", (message.from_user.username,))
    data =  mycursor.fetchall()

    if(len(data) == 0):
        args = message.text.split('_')
        data = (args[1], message.from_user.username ,args[2], args[3], args[4], args[5])
        simpanData(data)
        bot.send_message(message.chat.id,f'Data berhasil ditambahkan')
    else:
        bot.send_message(message.chat.id,'Startup tidak boleh lebih dari 1')