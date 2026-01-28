import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ROAST DATABASE
ankit_data = [
    "Ankit er Bichi Choto 💀",
    "Ankit Madarchod.",
    "Panchod Bill sala tor maire chudi 👄",
    "Ek number er khanki r chele sala ☠️",
    "Saddy ke Soda ii chudbe.",
    "Saddy 💗 Soda.",
    "Jolpori r Nati.",
    "Magibaj saala.",
    "Panchod er Gud e Murgi r Dim 😘",
    "Panchod er Gud e Powerbank Dhukiye De 🔥",
    "Ankit er Pussy, sobcheye juicy 🫦💦",
    "Bhor Pone 5 ta obdi Panchod er Bou ke Chudbo 🤣",
    "Saala tor maa ke tel muri diye chudbo, sala tor bhai jhal muri hoye berobe 🤣🤣",
    "Panchod er pod, Tel chara chod.",
    "Mukhe diye pan, maro ankit er gan(d)",
    "Bara Panchod gare arshola guje die LAL HIT spray kore debo...",
    "10 ta back chure marbo bara Microsoft ☠️",
    "Background character energy.",
    "Train e Bichi kata Ankit 💦",
    "Handle Choda Ankit💦",
    "Royal Stag choda Ankit 💦💦",
    "Ankit er fata , gudmarani r beta 💦",
    "Highway r rendimagi Ankit 💦",
    "AOT r bessa magi Ankit💦",
    "Malgari r bichi Ankit er guddee💦",
    "Saala toke Bally te giye chude asbo 😝",
    "Nakazz chudi Ankit 💦"
]

abhra_data = [
    "Abhra thinks he cooked… but Digha cooked harder.",
    "Abhra loading confidence without skills.",
    "Bro speaks before thinking — every time.",
    "Abhra running on Sristi's cum.",
    "Even Google can’t find Abhra’s choto nunu.",
    "Digha r mone e gota Boys Hostel, but pussy te khali Abhradip 🫦",
    "Abhra Loves Sristi. But Sristi loves Subham.",
    "Kire Gandu Threesome korbi naki re Sristi & Digha r sathe 😘",
    "Chut is soo large, AOT r moto 10 ta college dhuke jabe ☠️",
    "Khenki to bhai achis tui 🥴"
]

biswa_data = [
    "Biswa talks like he knows everything — knows nothing.",
    "Biswa’s ideas sound better in his head.",
    "Confidence sponsored by nothing.",
    "Biswa r rani ke bara amrai chude debo 😘",
    "Sala Baccha choda mal 🤣",
    "Bar bar deke lab nei Biswa pedophile ii thakbe.",
    "Panchod chess e toke chude debe 💦",
    "Byapti choda sala 👄",
    "Sala Byapti r kalo Pussy chata mal 👅",
    "Byapti r pussy fatano holo?? Saaaaallaaa Byaptichoda 🤣🤣",
    "Sala Byaptaranjan 💀"
]

asmit_data = [
    "Asmit saala valo maal ache.",
    "Asmit is that calm guy everyone trusts.",
    "Always supportive, always solid — that’s Asmit.",
    "One of those people who makes the group better.",
    "Asmit = green flag energy fr 💚",
    "Asmit deserves respect 🫡",
    "W human detected.",
    "Good vibes only — Asmit edition.",
    "Rare personality unlocked.",
    "Solid guy fr.",
    "Asmit ke niye doubt kore lab nei, chele valo 😘"
]

gunda_data = [
    "Gunda r morche pora Pussy ☠️",
    "Khemti Magi Saali.",
    "Garer Cheda sala kutta ke khoyano uchit ☠️",
    "Khanki Magi r guder baal.",
    "Chutmaarani Rendi 🥀",
    "Generational Rendi 😒",
    "Khanki Chudi Saalaa 🙄",
    "Gunda r garer cheday rocket guje mahakash e pathie debo khankir meye akta 🙄",
    "Gunda 💗 Ankit",
    "Besaaa Magii Gunda 👅",
    "Gunda Rendi khana 🖕",
    "Silencer dhokano Gunda magi 💀",
    "Road e ghose jaoa Gunda pussy 🖕",
    "Arnab er bichi dhokano mal Gunda 💀",
    "Phedaa khaoa Gunda 🖕",
    "Bablachudi Gunda 🖕",
    "Choto bichi ar jhulonto duudhh wala Gunda 💀",
    "Handle dkhokano Gunda 💀",
    "Gunda r poder futo, pahar r guhoo 🖕",
    "Jolonto chudir meye Gunda 🖕",
    "Nataka chudi Gunda 💀",
    "Baba choda Gunda 🖕",
    "Mountain Dew, Gunda ma ki chut 🖕",
    "Scooty choda Gunda 💀",
    "Sobai kore guun guun, Gunda r pussy te agun 👅",
    "Gunda akta Gudmarani...ewwww !!"
]

# ROAST INDEX
roast_index = {
    "ankit": 0,
    "abhra": 0,
    "biswa": 0,
    "asmit": 0,
    "gunda": 0
}

# ROAST LIST DATABASE
roast_db = {
    "Ankit": ankit_data,
    "Abhra": abhra_data,
    "Biswa": biswa_data,
    "Asmit": asmit_data,
    "Gunda": gunda_data
}

# EVENTS
@bot.event
async def on_ready():
    print("Bot is online 🔥")

    channel_ids = [
        1465758717583822993,
        1465774350455279707
    ]

    for channel_id in channel_ids:
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(
                "🟢 **Bot is Updated just now.**\nYou may continue your bakchodi 👾"
            )

# SERIAL FUNCTION
def get_next(name, data):
    i = roast_index[name]
    msg = data[i]
    roast_index[name] = (i + 1) % len(data)
    return msg

# COMMANDS
@bot.command()
async def ankit(ctx):
    await ctx.send(get_next("ankit", ankit_data))

@bot.command()
async def abhra(ctx):
    await ctx.send(get_next("abhra", abhra_data))

@bot.command()
async def biswa(ctx):
    await ctx.send(get_next("biswa", biswa_data))

@bot.command()
async def asmit(ctx):
    await ctx.send(get_next("asmit", asmit_data))

@bot.command()
async def gunda(ctx):
    await ctx.send(get_next("gunda", gunda_data))


@bot.command()
async def roastlist(ctx):
    msg = "🔥 **Roast Database** 🔥\n\n"

    for name, roasts in roast_db.items():
        msg += f"• {name} — {len(roasts)} roasts\n"

    await ctx.send(msg)

@bot.command()
async def list(ctx):
    msg = (
        "📘 **Bot Commands** 📘\n\n"
        "• `!ankit` — Roast Ankit\n"
        "• `!abhra` — Roast Abhra\n"
        "• `!biswa` — Roast Biswa\n"
        "• `!gunda` — Roast Gunda\n"
        "• `!asmit` — Roast Asmit\n\n"
        "**Utility:**\n"
        "• `!roastlist` — Show roast database\n\n"
        "Type commands with `!` prefix.\n"
        "Use responsibly 😌🔥"
    )

    await ctx.send(msg)


# RUN BOT
bot.run("MTQ2NjA0MjA4ODg3NjQxMjk0OQ.GsLIRx.2tpsDZnpRAZWGzSZCessieJnrluEKKcmA5_qw4")


