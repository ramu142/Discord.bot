import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('*With Hq Lifes / .help*'))
    for guild in client.guilds:
        for channel in guild.text_channels:
            if str(channel) == "general":
                await channel.send('Bot Activated..')
                print('Active in {}\n Member Count : {}'.format(guild.name, guild.member_count))
                print('Logged in as')
                print(client.user.name)
                print(client.user.id)
                print('------')




@client.command(help="Prints details of Server")
async def where_am_i(ctx):
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc = ctx.guild.description

    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    members = []
    async for member in ctx.guild.fetch_members(limit=150):
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name, str(member.status),
                                                                       str(member.joined_at)))


@client.command()
async def tell_me_about_yourself(ctx):
    text = "My name is WallE!\n I was built by Kakarot2000. At present I have limited features(find out more by typing !help)\n :)"
    await ctx.send(text)


@client.event
async def on_message(message, img_url=None, embed=None):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        print("User used .hello command")
        msg = 'Hello {0.author.mention} :smile: '.format(message)
        await message.channel.send(msg)
        print("above Message sent")

    if message.content.startswith('.hi'):
        print("User used .hi command")
        msg = 'Hi {0.author.mention} :smile: '.format(message)
        await message.channel.send(msg)
        print("above Message sent")

    if message.content.startswith(".how are you"):
        print("User used .how are you command")
        msg1 = "I am fine {0.author.mention} How about you".format(message)
        await message.channel.send(msg1)
        print("above Message sent")

    if message.content.startswith(".i am fine"):
        print("User used .i am fine command")
        msg2 = "Hoo {0.author.mention} ok".format(message)
        await message.channel.send(msg2)
        print("above Message sent")

    if message.content.startswith(".play music"):
        print("User used .play music command")
        await message.channel.send("*Sorry :cry: i can't right now . I am still in the Development Stage*")
        print("above Message sent")

    if message.content.startswith(".help"):
        print("User used .help command")
        commands = (".hi", ".hello" , ".how are you", ".i am fine" , ".points", ".point",".stock",".buy")
        await message.channel.send("These are  the commands",file=discord.File('help.png'))
        print("above Message sent")

    if message.content.startswith(".points"):
        print("User used .points command")
        pont = "Please Load Some Points {0.author.mention}".format(message)
        await message.channel.send("*Points* = 0 ")
        await message.channel.send(":pleading_face:")
        await message.channel.send(pont)
        print("above Message sent")

    if message.content.startswith(".point"):
        print("User used .point command")
        pont = "Please Load Some Points {0.author.mention}".format(message)
        await message.channel.send("*Points* = 0 ")
        await message.channel.send(":pleading_face:")
        await message.channel.send(pont)
        print("above Message sent")

    if message.content.startswith(".stock"):
        print("User used .stock command")
        await message.channel.send("Stock   Hqlifes =  2359 ", file=discord.File('hq.png'))
        await message.channel.send("Feal Free to Use .buy Command")
        print("above Message sent")

    if message.content.startswith(".buy"):
        print("User used .buy command")
        await message.channel.send("The Buy Command is Temporarily Disabled")
        await message.channel.send("See You Again :wave:")
        print("above Message sent")
    if message.content == '.owner':
        owner = ("*꧁⎝࿐WHITE DEVIL࿐⎠꧂#6471*")
        await message.channel.send(owner)



client.run("NjQxNTg1MTQ1NjkzOTk1MDA4.XcKgug.cdzq5EEhV9xF8Px7gsWsdGiN4Xc")
