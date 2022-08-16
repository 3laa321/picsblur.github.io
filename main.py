import requests
import pytesseract
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
from telegram.ext import Updater, CommandHandler
import carbonsh
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

####################################################

TOKEN = ('5540776676:AAHI3yCDihXiU6j5eHB3DCCHEnCtOsY0zTI')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

#############################################################

def start(update, context):
    username = update.message.chat.username
    first_name = update.message.chat.first_name
    print("started By : ", username)
    welcome = f'''
Hey,<b> {first_name}</b>

I'm <a herf="http://t.me/PicsBlur_bot\"> PicsBlur </a> 
I Can Do 

⌘  Blur A Image
Hit /help How to Use Me 

Developer : <a href=\"t.me/D_V_LAIL\">Lail</a>🧑‍💻
Made By : <a href=\"https://t.me/D_V_LAIL\"> Lail company </a> ❤️
Hit /Dev for more detalis

'''
    update.message.reply_text(reply_to_message_id=update.message.message_id, text=welcome, parse_mode='html',
                              disable_web_page_preview=True)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)





####################### Method to make blur###################


def blur(update, context):
    username = update.message.chat.username
    print("Blured By : ", username)
    context.bot.get_file(update.message.reply_to_message.photo[-1]).download(
        custom_path="./Editing/PicsBlur.png")
    blur_radious = int(context.args[0])

    if blur_radious < 100:

        messa = '''<b>
please wait....
                            </b>'''

        update.message.reply_text(
            reply_to_message_id=update.message.message_id, text=messa, parse_mode='html')

        Photo = Image.open("./Editing/PicsBlur.png")
        photo = Photo.filter(ImageFilter.GaussianBlur(radius=blur_radious))
        photo.save('./Editing/PicsBlur.png')

        caption = '<b>Blured  By <a herf=\"http://t.me/PicsBlur_bot\">PicsBlur</a></b> ❤️'
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open('./Editing/PicsBlur.png', 'rb'),
                               caption=caption, parse_mode="html")

    else:
        messa = '''
*Blur Value Must Be < 100 😇

Use /help If U don't Know How to Use Me*    '''
        update.message.reply_text(
            reply_to_message_id=update.message.message_id, text=messa, parse_mode='markdown')


blur_handeler = CommandHandler('blur', blur)
dispatcher.add_handler(blur_handeler)

###################### help #######################

def help(update, context):
    help_ = '''
*You Don't Know How to Use Me ? ok

To Blur image 🫣

replay to an image with /blur {blur value}

↬example: /blur 40


*
    '''
    update.message.reply_text(
        reply_to_message_id=update.message.message_id, text=help_, parse_mode='markdown')


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

########################  dev  #############################

def dev(update, context):
    username = update.message.chat.username
    print("Source  : ", username)
    source = '''

Developer : <a href=\"t.me/D_V_LAIL\">Lail</a>🧑‍💻
    
Made By <a href=\"https://t.me/D_V_LAIL\">Lail company</a> ❤️  


 
    '''
    update.message.reply_text(reply_to_message_id=update.message.message_id, text=source, parse_mode='html',
                              disable_web_page_preview=True)


dev_handeler = CommandHandler('dev', dev)
dispatcher.add_handler(dev_handeler)

updater.start_polling()
