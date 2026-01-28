import discord
from discord.ext import commands
import random

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
    "Background character energy."
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
    "Gunda 💗 Ankit",
    "Gunda akta Gudmarani...ewwww !!"
]

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


# COMMANDS

@bot.command()
async def ankit(ctx):
    await ctx.send(random.choice(ankit_data))

@bot.command()
async def abhra(ctx):
    await ctx.send(random.choice(abhra_data))

@bot.command()
async def biswa(ctx):
    await ctx.send(random.choice(biswa_data))

@bot.command()
async def asmit(ctx):
    await ctx.send(random.choice(asmit_data))

@bot.command()
async def gunda(ctx):
    await ctx.send(random.choice(gunda_data))

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
