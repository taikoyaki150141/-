import discord
from discord import app_commands
import random

intents = discord.Intents.default()

# Discordクライアントを作成します。
client = discord.Client(intents=intents)

# コマンドツリーを作成します。
tree = app_commands.CommandTree(client)


# 起動イベントを定義します。
@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()  # スラッシュコマンドを同期


# 乱数生成のコマンドを定義します。
@tree.command(name="roll", description="指定された範囲内の乱数を生成します。")
async def generate_random_number_command(interaction: discord.Interaction, max_number: int):
    generated_number = random.randint(1, max_number)
    await interaction.response.send_message(f"{generated_number}")


# コイントスのコマンドを定義します。
@tree.command(name="coin", description="コイントスを行います。")
async def coin_toss_command(interaction: discord.Interaction):
    result = random.choice(["表", "裏"])
    await interaction.response.send_message(f"{result}")


# Discordボットクライアントを実行します。
client.run("MTE5Nzk0NjQ4NDgyNjU5MTM2Mw.Gf5ea0.8zDTmtdII68rrrwWheQnsz5ECkb8q1NV1g0raU")
