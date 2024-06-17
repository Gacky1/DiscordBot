# from discord.ext import commands
# import discord

# DISCORD_TOKEN = "MTI1MTc4ODkyNDM0NzYxMzIwNA.G_swFi.dqP5YmMZaVTjj7z8OG-igKCtAFI1nwDrJVhnAU"

# bot = commands.Bot("!", intents=discord.Intents.all())

# @bot.event
# async def on_message(message):
#     if message.content.lower() == "c2i":
#         await message.channel.send("Today is Sunday, June 16, 2024 and here are the results:")

# if __name__ == "__main__":
#     bot.run(DISCORD_TOKEN)
# Run the bot
#bot.run('MTI1MTc4ODkyNDM0NzYxMzIwNA.G_swFi.dqP5YmMZaVTjj7z8OG-igKCtAFI1nwDrJVhnAU')
import discord
from discord.ext import commands
import asyncio
import aiohttp
import json

bot = commands.Bot("!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Yoru Shop & Exchanges"))
    print('Bot is ready')
    print(bot.user.name)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="﹕ϟ﹒﹐chat")
    if channel:
        message = await channel.send(f"Welcome to the server, {member.mention}!")
        await asyncio.sleep(40)
        await message.delete()



@bot.event
async def on_guild_channel_create(channel):
    if channel.category.name == "B4Y":
        await asyncio.sleep(3)
        await channel.send("I accept luxe mm!\n Server link: https://discord.gg/autoluxe \n If you want we can do direct without MM")

group1 = [1207080495549259776]
@bot.event
async def on_message(message):
    # Check if the bot was mentioned in the message
    if bot.user.mentioned_in(message):
        # Respond with "HI"
        await message.channel.send("HI")

    # Check if the message contains "c2i"
    if "c2i" in message.content.lower():
        # Respond with a message
        await message.channel.send("Your custom response message here")

    if message.content.lower() == "addy":
        user_id = message.author.id
        if user_id in group1:
            await message.channel.send("`ltc1q0urwvm33a2mh04nwdhanmdgh07x6ksqcv6fjty`")
        else:
            await message.channel.send("You don't have an LTC address associated with your account.")
        await message.delete()

    if message.content.lower() == "upi":
        user_id = message.author.id
        if user_id in group1:
            await message.channel.send("avasthisantivirus@fam")
        else:
            await message.channel.send("You don't have a UPI associated with your account.")
        await message.delete()

    if message.content.lower() == "qr":
        user_id = message.author.id
        if user_id in group1:
            await message.channel.send("https://media.discordapp.net/attachments/1251871027915526154/1251871903258513408/WhatsApp_Image_2024-06-16_at_15.png?ex=66702810&is=666ed690&hm=e457becda1326ee61f269a6fe743a5ce654af28445ebf8bfe04aac7cb92618bd&=&format=webp&quality=lossless&width=343&height=701")
        else:
            await message.channel.send("You don't have a UPI associated with your account.")
        await message.delete()

    if message.content.lower() == "tyn":
        await message.channel.send("Thank you for dealing with me!\n Please vouch me at <#1251170304055574679>\n **Vouch Format**\n *For purchase*: `+rep 1207080495549259776 Legit Got (product) For (price) Thank You` \n *For Exchange*: `+rep 1207080495549259776 LEGIT EXCHANGER • [Amt] LTC TO UPI Thank You`")
        await message.delete()

# Other bot commands and event handlers can be defined here
    await bot.process_commands(message)

@bot.command()
async def remind(ctx, time: int, *, task: str):
    await ctx.send(f'Reminder set for {time} minutes.')
    await asyncio.sleep(time*60)
    await ctx.send(f'{ctx.author.mention}, reminder: {task}')
    await bot.process_commands(message)

@bot.command()
async def calc(ctx, *, operation: str):
    try:
        result = eval(operation)
        if isinstance(result, (int, float)):
            await ctx.send(f"Result: {result}")
        else:
            await ctx.send("Error: Invalid operation")
    except Exception as e:
        await ctx.send(f"Error: {e}")
        await bot.process_commands(message)


@bot.command()
async def clone(ctx, target_server_id: int):
    """Clone a Discord server"""
    if ctx.author.id != 1207080495549259776:  # replace MY_ID with your Discord ID
        return await ctx.send("You do not have the permission to clone servers.")

    target_server = bot.get_guild(target_server_id)
    if target_server is None:
        return await ctx.send("Target server not found.")

    # Create a new server with the same name
    new_server = await bot.create_guild(target_server.name)

    # Set the icon of the new server
    await new_server.edit(icon=target_server.icon)

    # Clone channels
    for channel in target_server.channels:
        if channel.type == discord.ChannelType.text:
            new_channel = await new_server.create_text_channel(channel.name)
        elif channel.type == discord.ChannelType.voice:
            new_channel = await new_server.create_voice_channel(channel.name)
        elif channel.type == discord.ChannelType.category:
            new_channel = await new_server.create_category_channel(channel.name)

        # Clone channel permissions
        for permission in channel.permissions:
            await new_channel.set_permissions(permission.target, permission.permission)

    # Clone roles
    for role in target_server.roles:
        new_role = await new_server.create_role(role.name, role.color, role.hoist, role.mentionable)
        await new_role.edit(position=role.position)

        # Clone role permissions
        for permission in role.permissions:
            await new_role.set_permissions(permission.target, permission.permission)

    # Clone server settings
    await new_server.edit(banner=target_server.banner)

    await ctx.send(f"Server cloned successfully! New server ID: {new_server.id}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


bot.run('MTI1MTc4ODkyNDM0NzYxMzIwNA.G_swFi.dqP5YmMZaVTjj7z8OG-igKCtAFI1nwDrJVhnAU')
