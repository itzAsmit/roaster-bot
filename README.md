# Discord Roast Bot 🔥

A fun Discord bot that delivers pre-written roasts and integrates with Google's Gemini AI for creative responses.

## Features

- **Database Roasts**: Pre-loaded roasts for specific people that cycle through sequentially
- **AI Integration**: Tag the bot to get AI-generated responses via Google Gemini
- **Command System**: Simple prefix-based commands for quick roasts
- **Auto-notifications**: Announces when the bot comes online

## Commands

### Roast Commands
- `!ankit` - Roast Ankit
- `!abhra` - Roast Abhra
- `!biswa` - Roast Biswa
- `!gunda` - Roast Gunda
- `!asmit` - Compliment Asmit (yes, he gets special treatment 💚)

### Utility Commands
- `!roastlist` - View roast database statistics
- `!helpme` - Display all available commands

### AI Features
**Tag the bot** to activate AI mode:
- `@Bot ai [your prompt]` - Get AI-generated creative roasts
- `@Bot [name]` - Get database roasts by tagging with a name
- `@Bot [any question]` - Normal AI chat

## Setup

### Prerequisites
- Python 3.8+
- Discord Bot Token
- Google Gemini API Key

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd discord-roast-bot
```

2. **Install dependencies**
```bash
pip install discord.py google-generativeai
```

3. **Set up environment variables**

Create a `.env` file or set these environment variables:
```env
TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Run the bot**
```bash
python main.py
```

## Getting API Keys

### Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the "Bot" section
4. Click "Reset Token" to get your bot token
5. Enable "Message Content Intent" under Privileged Gateway Intents

### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and save it securely

## Configuration

### Channel IDs
Update the channel IDs in `main.py` where the bot sends startup messages:
```python
channel_ids = [
    1465758717583822993,  # Replace with your channel ID
    1465774350455279707   # Replace with your channel ID
]
```

### Adding New Roasts
Add entries to the respective data arrays:
```python
ankit_data = [
    "Your new roast here",
    # Add more roasts
]
```

### Adding New People
1. Create a new data array
2. Add to `roast_db` dictionary
3. Initialize in `roast_index`
4. Create a command function

## Project Structure

```
discord-roast-bot/
│
├── main.py              # Main bot file
├── README.md           # This file
└── .env                # Environment variables (create this)
```

## How It Works

### Serial Roast System
The bot uses an index system to cycle through roasts sequentially. Each person has their own index that increments with each roast, ensuring variety.

### AI Integration
The bot uses Google's Gemini 2.5 Flash model for AI responses. When tagged with "ai" or a general query, it sends requests to the Gemini API.

## Usage Examples

```
!ankit
> Ankit er Bichi Choto 💀

!roastlist
> 🔥 Roast Database 🔥
> • Ankit — 27 roasts
> • Abhra — 10 roasts
> ...

@Bot ai write a funny roast about programmers
> [AI-generated response]

@Bot ankit
> [Database roast about Ankit]
```

## Contributing

Feel free to add more roasts or improve the bot! Just make sure to:
- Keep roasts light-hearted (within your group's boundaries)
- Test new features before deploying
- Update the README if you add new commands

## Notes

⚠️ **Content Warning**: This bot contains explicit language and is designed for private use among friends who understand the context. Use responsibly.

## Troubleshooting

**Bot not responding:**
- Check if Message Content Intent is enabled
- Verify your bot token is correct
- Ensure the bot has proper permissions in your server

**Gemini API errors:**
- Verify your API key is valid
- Check your API quota
- Ensure you have internet connectivity

**Bot offline:**
- Check console for error messages
- Verify environment variables are set
- Ensure required packages are installed

## License

This project is for personal/educational use. Please use responsibly and ensure all participants consent to the roasting.

---

**Made with 🔥 for the homies**
