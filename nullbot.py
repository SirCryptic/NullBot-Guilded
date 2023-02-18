import guilded
import subprocess
import os
import re
import ipaddress
import socket
import whois

data = {
    "prefix": "!" # or whatever prefix you want to use
}

client = guilded.Client()

def sanitize(input_str):
    return re.sub('[^A-Za-z0-9\.\-]', '', input_str)

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user.name}!')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    args = message.content.split(" ")
    if args[0] == data['prefix'] + 'console':
        if args[1] == 'help':
            await message.channel.send("List of available commands: \n"
                "-----------------------------------------------------------------------\n"
                + data['prefix'] + "console whois - Get WHOIS Information About A Domain\n"
                + data['prefix'] + "console nmap - Detect OS & Find Open Ports On A Host\n"
                + data['prefix'] + "console nikto - Scan a web server for vulnerabilities\n"
                "-----------------------------------------------------------------------\n"
                "NullBot Beta v1.0.0 Developed By: [ SirCryptic ] - [ NullSecurityTeam ]\n")
        elif args[1] == 'nmap':
            sanitizedInput = sanitize(args[2])
            try:
                ip = ipaddress.ip_address(sanitizedInput)
                if ip.is_loopback or ip.is_link_local:
                    await message.channel.send("Scanning localhost and link-local addresses is not allowed.")
                    return
                host = ipaddress.ip_network('10.0.0.0/8')
                if ip in host:
                    await message.channel.send("Scanning addresses within the host machine's network is not allowed.")
                    return
            except ValueError:
                try:
                    ip = ipaddress.ip_address(socket.gethostbyname(sanitizedInput))
                except socket.gaierror:
                    await message.channel.send("Invalid IP address or domain name.")
                    return

            print(f"Scanning IP: {ip}")
            command = f"sudo nmap -O {ip}"
            output = subprocess.check_output(command, shell=True).decode()
            await message.channel.send(output)
        elif args[1] == 'nikto':
            sanitizedInput = sanitize(args[2])
            try:
                ip = ipaddress.ip_address(sanitizedInput)
                if ip.is_loopback or ip.is_link_local:
                    await message.channel.send("Scanning localhost and link-local addresses is not allowed.")
                    return
                host = ipaddress.ip_network('10.0.0.0/8')
                if ip in host:
                    await message.channel.send("Scanning addresses within the host machine's network is not allowed.")
                    return
            except ValueError:
                try:
                    ip = ipaddress.ip_address(socket.gethostbyname(sanitizedInput))
                except socket.gaierror:
                    await message.channel.send("Invalid IP address or domain name.")
                    return

            print(f"Scanning IP: {ip}")
            command = ["nikto", "-h", str(ip)]
            output = subprocess.check_output(command).decode()
            for chunk in [output[i:i+2000] for i in range(0, len(output), 2000)]:
                await message.channel.send(chunk)
                
        elif args[1] == 'whois':
            sanitizedInput = sanitize(args[2])
            try:
                ip = ipaddress.ip_address(sanitizedInput)
                if ip.is_loopback or ip.is_link_local:
                    await message.channel.send("Performing a whois lookup on localhost and link-local addresses is not allowed.")
                    return
                host = ipaddress.ip_network('10.0.0.0/8')
                if ip in host:
                    await message.channel.send("Performing a whois lookup on addresses within the host machine's network is not allowed.")
                    return
            except ValueError:
                try:
                    ip = ipaddress.ip_address(socket.gethostbyname(sanitizedInput))
                except socket.gaierror:
                    await message.channel.send("Invalid IP address or domain name.")
                    return
                
    command = ["whois", sanitizedInput]
    output = subprocess.check_output(command).decode()
    for chunk in [output[i:i+2000] for i in range(0, len(output), 2000)]:
        await message.channel.send(chunk)
                
client.run('you_bot_token')
