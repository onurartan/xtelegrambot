# Twitter Populer Hashtag Telegram Bot

![GitHub release (latest by date)](https://img.shields.io/github/v/release/onurartan/xtelegrambot)
![GitHub issues](https://img.shields.io/github/issues/onurartan/xtelegrambot)
![GitHub license](https://img.shields.io/github/license/onurartan/xtelegrambot)
![Github starts](https://img.shields.io/gitea/stars/onurartan/xtelegrambot)

This project is a Telegram bot that allows you to retrieve popular hashtags from Twitter. It is developed in Python using the Selenium and Telebot libraries.

## Features

- **Popular Hashtags:** Retrieve the most popular hashtags on Twitter.
- **Country-Based Filtering:** View popular hashtags in specific countries.
- **JSON Country Information:** Obtain country codes and related information in JSON format.
- **Easy to Use:** Access information quickly and easily via Telegram commands.

## Getting Started

Follow these steps to get the bot up and running on your local machine.

### Requirements

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- [Telebot](https://pytba.readthedocs.io/en/latest/install.html)

### Kurulum

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/onurartan/xtelegrambot.git
   cd xtelegrambot
   ```

2. **Install Requirements:**

   ```bash
    pip install -r requirements.txt
   ```

3. **Start the Bot:**

   ```bash
   python bot.py
   ```


## Usage

You can use the following commands with the bot:

- **/start**: Starts the bot and sends a welcome message.
- **/hashtags**: Lists the most popular hashtags.
- **/hashtags --country <ülke kodu>**: : Lists popular hashtags for a specific country.
- **/countries**: Sends a JSON file with country codes and information.


## Example Usage


- **All Popular Hashtags:**

  ```text
  /hashtags
  ```

- **Popular Hashtags in Turkey:**

  ```text
   /hashtags --country tr
  ```

- **Country Codes:**

  ```text
  /countries
  ```


<!-- ## Test Bot
You can test the bot on Telegram using [@xpopuler_bot](https://t.me/xpopuler_bot). -->


## Contact

For more information about this project, you can contact me via [LinkedIn](https://linkedin.com/in/onurartan) or [GitHub](https://github.com/onurartan).


## Support

support the project, [star the repository](https://github.com/onurartan/xtelegrambot).

---

© 2024 Onur Artan. All rights reserved.

