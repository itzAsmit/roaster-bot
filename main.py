import discord
from discord.ext import commands
import os
import google.generativeai as genai
import random

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

text_model = genai.GenerativeModel("gemini-2.5-flash")

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
    "Even Google can't find Abhra's choto nunu.",
    "Digha r mone e gota Boys Hostel, but pussy te khali Abhradip 🫦",
    "Abhra Loves Sristi. But Sristi loves Subham.",
    "Kire Gandu Threesome korbi naki re Sristi & Digha r sathe 😘",
    "Chut is soo large, AOT r moto 10 ta college dhuke jabe ☠️",
    "Khenki to bhai achis tui 🥴"
]

biswa_data = [
    "Biswa talks like he knows everything — knows nothing.",
    "Biswa's ideas sound better in his head.",
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
    "Always supportive, always solid — that's Asmit.",
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

# COLOR SCHEMES FOR EACH PERSON
colors = {
    "Ankit": discord.Color.red(),
    "Abhra": discord.Color.blue(),
    "Biswa": discord.Color.purple(),
    "Asmit": discord.Color.green(),
    "Gunda": discord.Color.orange()
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
            embed = discord.Embed(
                title="🟢 Bot Online",
                description="Bot is Updated just now.\nYou may continue your bakchodi 👾",
                color=discord.Color.green()
            )
            embed.set_footer(text="Type !helpme for commands")
            await channel.send(embed=embed)

# SERIAL FUNCTION
def get_next(name, data):
    i = roast_index[name]
    msg = data[i]
    roast_index[name] = (i + 1) % len(data)
    return msg

# COMMANDS
@bot.command()
async def ankit(ctx):
    roast = get_next("ankit", ankit_data)
    embed = discord.Embed(
        title="🔥 Roasting Ankit",
        description=roast,
        color=colors["Ankit"]
    )
    embed.set_footer(text=f"Roast #{roast_index['ankit']} | Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def abhra(ctx):
    roast = get_next("abhra", abhra_data)
    embed = discord.Embed(
        title="🔥 Roasting Abhra",
        description=roast,
        color=colors["Abhra"]
    )
    embed.set_footer(text=f"Roast #{roast_index['abhra']} | Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def biswa(ctx):
    roast = get_next("biswa", biswa_data)
    embed = discord.Embed(
        title="🔥 Roasting Biswa",
        description=roast,
        color=colors["Biswa"]
    )
    embed.set_footer(text=f"Roast #{roast_index['biswa']} | Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def asmit(ctx):
    roast = get_next("asmit", asmit_data)
    embed = discord.Embed(
        title="✨ Praising Asmit",
        description=roast,
        color=colors["Asmit"]
    )
    embed.set_footer(text=f"Compliment #{roast_index['asmit']} | Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def gunda(ctx):
    roast = get_next("gunda", gunda_data)
    embed = discord.Embed(
        title="🔥 Roasting Gunda",
        description=roast,
        color=colors["Gunda"]
    )
    embed.set_footer(text=f"Roast #{roast_index['gunda']} | Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

# ROAST LIST
@bot.command()
async def roastlist(ctx):
    embed = discord.Embed(
        title="🔥 Roast Database 🔥",
        description="Here's the complete roast arsenal:",
        color=discord.Color.gold()
    )
    
    for name, roasts in roast_db.items():
        embed.add_field(
            name=f"{name}",
            value=f"📊 **{len(roasts)}** roasts available",
            inline=True
        )
    
    embed.set_footer(text="Use !helpme to see commands")
    await ctx.send(embed=embed)

# HELP LIST
@bot.command()
async def helpme(ctx):
    embed = discord.Embed(
        title="📘 Bot Commands Guide",
        description="Your complete guide to roasting and AI interactions",
        color=discord.Color.purple()
    )
    
    # Roast Commands
    roast_commands = (
        "`!ankit` - Roast Ankit\n"
        "`!abhra` - Roast Abhra\n"
        "`!biswa` - Roast Biswa\n"
        "`!gunda` - Roast Gunda\n"
        "`!asmit` - Praise Asmit"
    )
    embed.add_field(
        name="🔥 Roast Commands",
        value=roast_commands,
        inline=False
    )
    
    # Utility Commands
    utility = "`!roastlist` - View roast database stats"
    embed.add_field(
        name="⚙️ Utility",
        value=utility,
        inline=False
    )
    
    # AI Commands
    ai_info = (
        "**Tag the bot** to interact with AI:\n"
        "• `@bot <message>` - Normal AI chat\n"
        "• `@bot ai <prompt>` - Creative AI mode\n"
        "• `@bot <name>` - Get database roast"
    )
    embed.add_field(
        name="🤖 AI Features",
        value=ai_info,
        inline=False
    )
    
    # Tips
    tips = (
        "• Commands need `!` prefix\n"
        "• Tag bot for AI responses\n"
        "• Use responsibly 😌🔥"
    )
    embed.add_field(
        name="💡 Tips",
        value=tips,
        inline=False
    )
    
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    
    await ctx.send(embed=embed)

# TAG HANDLER
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(f"<@{bot.user.id}>"):
        raw = message.content.replace(f"<@{bot.user.id}>", "").strip()
        content = raw.lower()

        # AI MODE (keyword: ai)
        if content.startswith("ai"):
            prompt = raw[2:].strip()

            try:
                async with message.channel.typing():
                    response = text_model.generate_content(prompt)
                
                embed = discord.Embed(
                    title="🤖 AI Creative Mode",
                    description=response.text[:4000],
                    color=discord.Color.from_rgb(138, 43, 226)
                )
                embed.set_footer(text=f"Requested by {message.author.name}")
                await message.channel.send(embed=embed)
            except Exception as e:
                print(e)
                error_embed = discord.Embed(
                    title="⚠️ Error",
                    description="Gemini API error occurred.",
                    color=discord.Color.red()
                )
                await message.channel.send(embed=error_embed)

            await bot.process_commands(message)
            return

        # DATABASE ROAST MODE
        for name, data in roast_db.items():
            if name.lower() in content:
                roast = get_next(name.lower(), data)
                
                embed = discord.Embed(
                    title=f"🔥 Roasting {name}",
                    description=roast,
                    color=colors[name]
                )
                embed.set_footer(text=f"Triggered by {message.author.name}")
                await message.channel.send(embed=embed)
                await bot.process_commands(message)
                return

        # NORMAL AI CHAT
        if raw:
            try:
                async with message.channel.typing():
                    response = text_model.generate_content(raw)
                
                embed = discord.Embed(
                    title="💬 AI Response",
                    description=response.text[:4000],
                    color=discord.Color.blurple()
                )
                embed.set_footer(text=f"Asked by {message.author.name}")
                await message.channel.send(embed=embed)
            except Exception as e:
                print(e)
                error_embed = discord.Embed(
                    title="⚠️ Error",
                    description="Gemini API error occurred.",
                    color=discord.Color.red()
                )
                await message.channel.send(embed=error_embed)

    await bot.process_commands(message)

# RUN BOT
bot.run(os.getenv("TOKEN"))

