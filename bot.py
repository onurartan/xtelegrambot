from app.main import bot
import logging

if __name__ == '__main__':
    """
    Start Bot Bro
    """
    logging.basicConfig(level=logging.INFO)    
    bot.polling()