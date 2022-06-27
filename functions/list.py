from database import *

def lists(bot,message):
    try:
        mycursor.execute("SELECT * FROM founder")
        myresult = mycursor.fetchall() 
        print(myresult)
        for name,username,company,contact,amount,description in myresult:
            bot.send_message(message.chat.id, 
                """
    Name: {}\n
    Company: {}\n
    Contact: {}\n
    Ammount: {}\n
    Description: {}
    """.format(name,company,contact,amount,description))
    except:
        bot.send_message(message.chat.id, "Tidak ada data")

