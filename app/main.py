import telebot
from app.xbot import TrendBot
from env import Env
import json

from app.func import get_country_by_code, get_countries, escape_markdown_v2


API_TOKEN = Env.TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    welcome_message = (
        "Merhaba! Bu bot Twitter'daki popüler hashtag'leri getirir. "
        "/hashtags `--country <code>` komutunu kullanarak belirli bir ülkedeki popüler hashtag'leri görebilirsiniz.\n"
        "Varsayılan ülke kodu: `tr` \n"
        "Ülke kodlarını görmek için: /countries komutunu çalıştırın"
    )
    welcome_message = escape_markdown_v2(welcome_message)

    bot.reply_to(
        message,
        welcome_message,
        parse_mode="MarkdownV2",
    )


@bot.message_handler(commands=["hashtags"])
def send_hashtags(message):
    try:

        country_code = "tr"
        command_part = "tr"

        if "--country" in message.text:
            parts = message.text.split("--country")
            print("parts: ", parts)

            if len(parts) > 1:
                command_part = parts[0].strip()
                country_code = parts[1].strip().split()[0].lower().replace(" ", "")

        print("country_code: ", country_code, command_part)

        country = get_country_by_code(country_code)
        print("country_code: ", country)

        if country is None:
            bot.reply_to(
                message,
                escape_markdown_v2(
                    f"Geçersiz ülke kodu: `{country_code}`. Lütfen geçerli bir ülke kodu girin."
                ),
                parse_mode="MarkdownV2",
            )
            return

        start_message = bot.reply_to(
            message,
            escape_markdown_v2("Hashtag'ler getiriliyor..."),
        )

        # Verileri al
        tbot = TrendBot(country_code)
        hashtags = tbot.run()

        bot.delete_message(message.chat.id, start_message.message_id)

        if hashtags:
            response = "*Şu anda trend olan hashtag'ler:*\n"
            response += f"*Tamamlanma Süresi:* {tbot.tamamlanma_suresi:.2f} saniye\n"
            response += "\n".join([f"`{hashtag}`" for hashtag in hashtags])
            response = escape_markdown_v2(response)
        else:
            response = "Üzgünüm, şu anda trend olan hashtag'leri alamıyorum."
            response = escape_markdown_v2(response)

    except Exception as e:
        print("hello.....".replace(".", "\\."))
        response = f"Bir hata oluştu: {e}"
        response = escape_markdown_v2(response)

    bot.reply_to(message, response, parse_mode="MarkdownV2")


@bot.message_handler(commands=["countries"])
def send_countries(message):
    try:
        countries = get_countries()

        with open("countries.json", "w", encoding="utf-8") as f:
            json.dump(countries, f, ensure_ascii=False, indent=4)

        with open("countries.json", "rb") as f:
            bot.send_document(message.chat.id, f)

    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {e}")
