from database import *

def edit(bot,message):
    args = message.text.split('_')
    mycursor.execute("SELECT * FROM founder WHERE username = %s", (message.from_user.username,))
    data =  mycursor.fetchall()
    if(len(data) == 1):
        mycursor.execute("UPDATE founder SET name = %s, company = %s, contact = %s, amount = %s, description = %s WHERE username = %s", (args[1], args[2], args[3], args[4], args[5],  message.from_user.username))
        mydb.commit()
        bot.send_message(message.chat.id,f'Data berhasil diubah')
    else:
        bot.send_message(message.chat.id,'Data tidak ditemukan')