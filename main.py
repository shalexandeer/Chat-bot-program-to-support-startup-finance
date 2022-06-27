from email.policy import default
import telebot
# from functions.login import login
from functions.register import register
from database import *
from functions.add import *
from functions.edit import *
from functions.list import *


bot = telebot.TeleBot('5501089896:AAE7fa44wrhi_lWPm8i7GuzCH57TrQ6AHTA')
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,'Selamat datang di startup bot, disini anda bisa mendaftar sebagai investor atau founder.\nMasukkan atau tekan /help untuk mendapatkan informasi terkait cara penggunaan bot ')
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'berikut merupakan command yang bisa anda gunakan untuk menjalankan bot ini\n1. /register digunakan untuk mendaftar, anda bisa mendaftar dengan format: (/register _password_founder/investor), contoh /register _shalex_founder\n2. /add adalah fitur invest requirement bagi founder yang membutuhkan pendanaan untuk menambahkan data terkait kebutuhan investasi. Untuk menambahkan data invest requirement, anda bisa menggunakan format \n(/add name_username_company_contact_amount_description), \ncontoh /add sultan_shalex_PT.sisfo3_0868686_5000000_running a small business\n3. /edit merupakan fitur untuk mengedit invest requirement. Anda dapat mengganti invest requirement dengan format yang sama dengan /add\n4. /list merupakan fitur bagi investor untuk menampilkan data invest requirements dari para founder')
@bot.message_handler(commands=['register', 'add', 'edit', 'list'])
def main(message):
    args = message.text.split()
    mycursor.execute("SELECT * FROM user WHERE username = %s", (message.from_user.username,))
    data =  mycursor.fetchall()
    if(len(data) == 1):
        role = list(data[0])[2]
        match role:
            case 1:
                match args[0]:
                    case '/add':
                        add(bot,message)
                    case '/edit':
                        edit(bot,message)
                    case '/list':
                         bot.send_message(message.chat.id, 'Anda harus menjadi investor untuk melihat list invest requirements')
            case 2:
                match args[0]:
                    case '/list':
                        lists(bot,message)
            case _:
                bot.reply_to(message, "Command tidak tersedia")


    elif (len(data) == 0):
        if(args[0] == '/register'):
            register(bot,message)
        else:
            bot.send_message(message.chat.id, 'Anda belum terdaftar')


            
@bot.message_handler(func=lambda message: True)

def echo_all(message):
	bot.reply_to(message, "Perintah tidak tersedia!, silahkan cek command /help untuk mendapatkan informasi!")


bot.infinity_polling()