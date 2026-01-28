# 🔥 Roaster Bot

A fun Discord bot built using **Python** and **discord.py** that sends **serial (non-random) roasts** and **positive messages** through simple commands.

> ⚠️ This bot is created strictly for entertainment purposes.

---

## ✨ Features

- 🔁 Serial roast system (not random)
- 🎯 Separate roast list for each command
- 💚 Positive-only command section
- 🧠 Clean and beginner-friendly code
- 🔐 Secure token handling using environment variables
- ☁️ Ready for Railway deployment
- ⚡ Lightweight & fast

---

## 🤖 Commands

| Command | Description |
|-------|-------------|
| `!ankit` | Sends serial roast for Ankit |
| `!abhra` | Sends serial roast for Abhra |
| `!biswa` | Sends serial roast for Biswa |
| `!gunda` | Sends serial roast for Gunda |
| `!asmit` | Sends positive messages |

Each command sends messages **in order** and loops automatically after the last message.

---

## 🧠 How Serial Mode Works

Instead of random selection, the bot uses an index-based system:

- First command → first message  
- Second command → second message  
- After last message → starts again  

This avoids repetition and keeps responses organized.

---

## 🛠️ Tech Stack

- Python 3.10+
- discord.py
- Railway (recommended for hosting)

---

## 📂 Project Structure

```
roaster-bot/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/roaster-bot.git
cd roaster-bot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Create Discord Bot

1. Go to Discord Developer Portal  
2. Create a new application  
3. Add a bot  
4. Enable **Message Content Intent**  
5. Copy the bot token  

---

### 4️⃣ Set Environment Variable (IMPORTANT)

Do **not** place the token in code.

```
TOKEN=your_discord_bot_token
```

For Railway:
- Open project
- Go to **Variables**
- Add `TOKEN`

---

### 5️⃣ Run Locally

```bash
python main.py
```

If successful:
```
Bot is online 🔥
```

---

## ☁️ Railway Deployment

1. Push code to GitHub  
2. Create a Railway project  
3. Deploy from GitHub repository  
4. Add environment variable:

```
TOKEN = your_discord_bot_token
```

5. Start command:
```
python main.py
```

Bot will run **24/7**.

---

## 🔐 Security Notes

- ❌ Never hardcode your Discord token
- ✅ Always use environment variables
- 🔄 Reset token immediately if exposed

---

## 📌 Disclaimer

This bot is intended only for friendly and fun usage.  
Do not use it for harassment or harmful behavior.

---

## 👨‍💻 Author

Built with Python & chaos 🔥  
Maintained by **Rishi**
