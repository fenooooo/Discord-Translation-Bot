
# Discord Translation Bot

This bot translates messages to various languages using the `!translate <language_code> <message>` command. 
Built with Python, Discord.py, and Googletrans.

## Features

- Translates text to different languages
- Simple command-based usage

## Setup

1. Clone the repository.
2. Install dependencies:

   ```
   pip install discord.py googletrans==4.0.0-rc1 python-dotenv
   ```

3. Create a `.env` file and add your Discord bot token:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   ```

4. Run the bot:

   ```
   python bot.py
   ```

## Usage

Use the `!translate` command followed by the language code and the message you want to translate.

Example:

```
!translate es Hello, how are you?
```

This will translate the text to Spanish.

## Language Codes

Here is a list of common language codes you can use with the bot:

- **en**: English
- **es**: Spanish
- **fr**: French
- **de**: German
- **it**: Italian
- **pt**: Portuguese
- **zh-cn**: Chinese (Simplified)
- **zh-tw**: Chinese (Traditional)
- **ja**: Japanese
- **ko**: Korean
- **ru**: Russian
- **ar**: Arabic
- **hi**: Hindi
- **bn**: Bengali
- **he**: Hebrew
- **id**: Indonesian
- **tr**: Turkish
- **vi**: Vietnamese
- **th**: Thai
- **pl**: Polish

For a complete list of language codes, you can refer to the [Googletrans documentation](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages).

## Requirements

- Python 3.6 or higher
- discord.py
- googletrans==4.0.0-rc1
- python-dotenv

