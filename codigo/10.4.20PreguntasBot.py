#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adaptacion de Simple Bot by @Telegram

TODO:
* Teclado Si/No
* Fusion de nodos de varios arboles

"""
import logging
import os
import shutil
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import Preguntas20

v = '1.1'



update_id = None
juegos = {} # diccionarios de juegos con chat_id como clave

def main():
    """Run the bot."""
    global update_id, juego
    
    # Telegram Bot Authorization Token
    bot = telegram.Bot('1563564271:AAGUmlPaUXOWPWRLAcxdTjQy01KMQR70-nk')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    print(f'20 Preguntas Bot {v}')
    
    while True:
        try:
            updateBot(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def updateBot(bot):
    """Echo the message the user sent."""
    global update_id, juegos
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            # usuario update.message.from_user.first_name
            # texto update.message.text
            # chat_id update.message.chat_id
            
            if update.message.chat_id in juegos.keys():
                juego = juegos[update.message.chat_id]
            else: # Es nuevo
                userfile = f'nodos_{update.message.from_user.first_name}.txt'
                if not userfile in  os.listdir():
                    shutil.copyfile('nodos.txt',userfile)
                juego = Preguntas20.Juego20(userfile)
                juegos[update.message.chat_id] = juego
                print(f'Eres {update.message.from_user.first_name} desde {update.message.chat_id} ')
                # juego.dumpElementos()
            print(f'{update.message.from_user.first_name} >> {update.message.text}')
            respuesta = juego.updateEstado(update.message.text )
            str_respuesta = respuesta.replace('\n', '\n' + update.message.from_user.first_name + ' << ')
            print(f'{update.message.from_user.first_name} << {str_respuesta}')
            
            update.message.reply_text(respuesta)

if __name__ == '__main__':
    main()
