# Nullbot-Reboot - [BETA] - Guilded Auditing Bot

NullBot Beta is a multi-purpose Guilded bot for system administrators and security enthusiasts. The bot is capable of executing commands through Guilded to perform various tasks, such as detecting the operating system and finding open ports on a host using Nmap, and scanning a web server for vulnerabilities using Nikto. Now includes a WHOIS command. This bot was developed by [SirCryptic](https://github.com/sircryptic) of [NullSecurityTeam](https://github.com/orgs/NULL-Security-Team), and is open-source under the [MIT license](https://github.com/SirCryptic/Nullbot-Guilded/blob/main/LICENSE).

- Heres a [Discord Version](https://github.com/SirCryptic/NullBot-Reboot)

# Changelog
<details>
  <summary>Click to expand!</summary>

  - Added WHOIS
  
  - Removed Role Check For Guilded Version
  </details>


# Installation Instructions

1. Install the required Python packages using pip: `pip install -r requirements.txt`
2. Create a new Guilded bot.
4. Copy the bot token and replace the value of `client.run('your_bot_token')` in `nullbot.py` with the bot token.

# Running The Bot
```
sudo python3 nullbot.py
```

## How do I use the bot?

To use the bot, you can type the following commands ...

- `!console help` - Displays the list of available functions
- `!console whois` - Get WHOIS Information About A Domain or IP
- `!console nmap [host]` - Detect OS & Find Open Ports On A Host
- `!console nikto -h [host]` - Scan a web server for vulnerabilities


 # ⚠️ Foot Notes / Q&A ⚠️

Q: Why do i have to run this as root?

A: Unfortunatly you have to run the bot as root or the nmap command doesnt function properly and prompts you on the host machine to input your password.

Q: Can anyone Scan the host machine?

A: NO! localhost/all ip ranges regarding the host machine are blocked.
