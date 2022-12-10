from database import *

def simpanData(data):
    mycursor.execute("INSERT INTO user (username, password, role) VALUES (%s, %s, %s)", data)
    mydb.commit()

def register(bot,message):
    msg = message.text.split('_')
    nama = message.from_user.username
    role = ''
    print(msg)
    try:
        if(msg[2] == "founder" or msg[2] == "investor"):
            if(msg[2] == "founder"):
                role = 1
            elif(msg[2] == "investor"):
                role = 2
            data = (nama, msg[1], role)
            simpanData(data)
            bot.send_message(message.chat.id,f'Selamat datang {nama}, anda terdaftar sebagai {msg[2]}.')
        else:
            bot.send_message(message.chat.id,'Anda hanya bisa memilih founder atau investor')
    except IndexError:
        bot.send_message(message.chat.id, 'Pastikan format penulisan sudah tertulis dengan benar')bayley
