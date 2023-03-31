import discord, datetime

token = 'Discord Token'

client = discord.Client(intents=discord.Intents.all(), status=discord.Status.dnd)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_member_join(member: discord.Member):
    channel: discord.TextChannel = client.get_channel(1091474901866651739)
    embed = discord.Embed(color=0x40c6ff, title='Member joined', description=f'{member.mention} joined the Server', timestamp=member.joined_at)
    embed.set_thumbnail(url=member.avatar.url)
    await member.add_roles(discord.utils.get(member.guild.roles, id=1091477913280458785), reason='Joined Server')
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member: discord.Member):
    channel: discord.TextChannel = client.get_channel(1091474901866651739)
    embed = discord.Embed(color=0x40c6ff, title='Member left', description=f'{member} left the Server', timestamp=datetime.datetime.now())
    embed.set_thumbnail(url=member.avatar.url)
    await channel.send(embed=embed)


@client.event
async def on_member_ban(guild: discord.Guild, member: discord.Member):
    channel: discord.TextChannel = client.get_channel(1091474901866651739)
    embed = discord.Embed(color=0x40c6ff, title='Member banned', description=f'{member} was banned from the Server', timestamp=datetime.datetime.now())
    embed.set_thumbnail(url=member.avatar.url)
    await channel.send(embed=embed)


# @client.event
# async def on_message(msg: discord.Message):
#     if msg.author.id == 365879961761873920 and msg.content == '!rules':
#         embed = discord.Embed(color=0x40c6ff, title=':scroll: Rules for behavior on this Discord', timestamp=datetime.datetime.now())
#         embed.set_footer(text='State', icon_url=None)
#         embed.add_field(name=':one: Be kind to others', value='You must respect all users, regardless of whether you like them. Treat others exactly as you would like to be treated.', inline=False)
#         embed.add_field(name=':two: No vulgar language', value='The use of obscene words should be kept to a minimum. Any derogatory language towards users and any kind of insult or defamation is strictly prohibited.', inline=False)
#         embed.add_field(name=':three: No spamming', value='Please do not send many small messages one after another. Do not interrupt the chat by spamming.', inline=False)
#         embed.add_field(name=':four: No pornographic / other NSFW material', value='This is a community server and not meant to share this type of material. Anyone who violates this rule will be banned immediately and without warning.', inline=False)
#         embed.add_field(name=':five: No advertising', value='We do not tolerate any advertising, be it for other bots or Discord servers.', inline=False)
#         embed.add_field(name=':six: No offensive names and/or profile pictures', value='You will be asked to change your name or picture if the moderators find it inappropriate.', inline=False)
#         embed.add_field(name=':seven: Direct and indirect threats', value='Threats to other users from DDoS, Death, DoX, abuse and other malicious threats are absolutely forbidden and not allowed.', inline=False)
#         embed.add_field(name=':eight: No recordings', value='Recordings of conversations in voice chat channels are prohibited.', inline=False)
#         embed.add_field(name=':nine: The Discord Community Guidelines and Discord Terms of Service must be followed', value='[Discord Community Guidelines](https://discord.com/guidelines)\n[Discord\'s Terms of Service](https://discord.com/terms)', inline=False)
#         await msg.delete()
#         await msg.channel.send(embed=embed)


client.run(token)
