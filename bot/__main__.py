"""Bot entry point. Run with: python -m bot"""

import os
import asyncio
import logging
from discord.ext import commands
import discord
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=">>", intents=intents)

# MongoDB setup
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/fight-john")
mongo_client = None
db = None


@bot.event
async def on_ready():
    """Called when bot successfully logs in."""
    logger.info(f"Bot logged in as {bot.user}")
    logger.info(f"Connected to {len(bot.guilds)} guild(s)")


@bot.command(name="new")
async def new_game(ctx):
    """Start a new battle royale game."""
    await ctx.send("🎮 Starting a new battle royale! Use `>>join` to join the game.")


@bot.command(name="join")
async def join_game(ctx):
    """Join an active battle royale game."""
    await ctx.send(f"{ctx.author.mention} has joined the battle!")


@bot.command(name="status")
async def game_status(ctx):
    """Check the current game status."""
    await ctx.send("📊 Game Status: No active games.")


@bot.command(name="commands")
async def list_commands(ctx):
    """Show available commands."""
    embed = discord.Embed(title="Fight-John Commands", color=discord.Color.blue())
    embed.add_field(name=">>new", value="Start a new battle royale", inline=False)
    embed.add_field(name=">>join", value="Join an active game", inline=False)
    embed.add_field(name=">>status", value="Check game status", inline=False)
    await ctx.send(embed=embed)


async def setup_mongo():
    """Initialize MongoDB connection."""
    global mongo_client, db
    try:
        mongo_client = AsyncIOMotorClient(MONGODB_URI)
        db = mongo_client["fight-john"]
        # Test connection
        await db.command("ping")
        logger.info("✅ MongoDB connected successfully")
    except Exception as e:
        logger.error(f"❌ Failed to connect to MongoDB: {e}")


async def main():
    """Main bot runner."""
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN environment variable is required")

    # Setup MongoDB
    await setup_mongo()

    # Start bot
    async with bot:
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())

