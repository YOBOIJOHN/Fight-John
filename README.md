# Fight-John

A Discord battle-royale bot with persistent game data and image generation. Supports both slash commands (`/new`, `/join`, etc.) and prefix commands (`>>`).

## Features

- **Battle Royale Gameplay**: Classic game mode with multiple players
- **Persistent Data**: MongoDB integration for storing game state
- **Image Generation**: Pillow-based image rendering for game displays
- **Flexible Commands**: Both slash commands and prefix commands supported
- **Always-On**: Runs as a background service on Railway

## Tech Stack

- **Python 3.12** — Core runtime
- **discord.py** — Discord bot framework
- **Motor/MongoDB** — Async MongoDB driver for persistent storage
- **aiohttp** — Async HTTP client for image downloads
- **Pillow** — Image generation and manipulation

## Prerequisites

Before deploying, you need:

1. **Discord Bot Token**
   - Create an application on [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a bot user and copy the token
   - Enable required intents (Message Content Intent, etc.)
   - Invite the bot to your server with appropriate permissions

2. **MongoDB Instance**
   - Use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (free tier available)
   - Or use Railway's built-in MongoDB add-on
   - Get your connection URI (format: `mongodb+srv://user:pass@cluster.mongodb.net/dbname`)

## Local Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOBOIJOHN/Fight-John.git
   cd Fight-John
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (use `.env.example` as a template):
   ```bash
   cp .env.example .env
   ```

5. Update `.env` with your Discord token and MongoDB URI:
   ```
   DISCORD_TOKEN=your_token_here
   MONGODB_URI=your_mongodb_uri_here
   ```

6. Run the bot:
   ```bash
   python -m bot
   ```

## Deployment on Railway

### Step 1: Connect Repository to Railway

1. Go to [Railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `YOBOIJOHN/Fight-John`
5. Railway will automatically detect the Dockerfile

### Step 2: Add Environment Variables

1. In the Railway dashboard, go to your project
2. Click on the service
3. Go to the "Variables" tab
4. Add the following:

   | Variable | Value |
   |----------|-------|
   | `DISCORD_TOKEN` | Your Discord bot token |
   | `MONGODB_URI` | Your MongoDB connection URI |

### Step 3: Add MongoDB (if not using external Atlas)

1. In Railway, click "Add a service"
2. Select "Add from Marketplace" → "MongoDB"
3. Railway will create a MongoDB instance and auto-populate `MONGODB_URI`
4. Or, use MongoDB Atlas and manually set `MONGODB_URI`

### Step 4: Deploy

1. Railway will automatically build and deploy when you push to `main`
2. The bot starts with the command: `python -m bot`
3. View logs in the Railway dashboard to confirm the bot is running

### Step 5: Verify Deployment

- Check Railway logs for startup messages
- Test the bot in Discord with `/new` or `>>help`
- Confirm data is persisting in MongoDB

## Commands

### Slash Commands
- `/new` — Start a new battle royale
- `/join` — Join an active game
- `/status` — Check game status
- (More commands as implemented)

### Prefix Commands
- `>>new` — Start a new battle royale
- `>>join` — Join an active game
- `>>status` — Check game status
- `>>help` — List all commands
- (More commands as implemented)

## Troubleshooting

### Bot Not Responding

- Verify `DISCORD_TOKEN` is correct and the bot is invited to the server
- Check Railway logs for errors
- Ensure the bot has permission to see channels and messages

### Database Connection Issues

- Verify `MONGODB_URI` is correct
- Check MongoDB Atlas/Railway MongoDB is running
- Ensure IP whitelist allows Railway's egress IPs (Atlas: add `0.0.0.0/0`)

### Image Generation Errors

- Verify Pillow is installed: `pip install Pillow`
- Check that image URLs are accessible
- Review logs for specific Pillow/aiohttp errors

## License

(Add your license here)

## Support

For issues or questions, open a GitHub issue or contact the maintainer.
