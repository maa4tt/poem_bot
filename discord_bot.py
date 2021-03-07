from discord.ext import commands
from discord_token import TOKEN
import discord
import make_image
from make_poem import *
import markovify_poems

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Howdy Folks!')


@client.command()
async def poem(ctx):
    name = 'poem'
    image_file_name = f'{name}.png'  # what the image will be saved locally as.
    text_file_name = f'{name}.txt'  # what the txt will be saved locally as
    poem_text = poem_writer(f'{text_file_name}')  # write a poem, a second argument for length can be added
    # the default is random between 2 and 5 sentences (inclusive).
    column_wrapped_text = column_wrap(poem_text[1])
    make_image.make_card(poem_text[0], column_wrapped_text, 0, f'{image_file_name}')  # calling make image using
    # arguments for (title, text appropriately column wrapped, indent, filename)
    file = discord.File(f'{image_file_name}')
    print(poem_text)
    await ctx.send(file=file, content=f'')


# react to any message containing 'poet', currently breaks the poem command. I have no fkin clue why
# @client.event
# async def on_message(ctx):
#    if 'poet' in ctx.content:
#        emoji = '\N{EYES}'
#        await ctx.add_reaction(emoji)

client.run(TOKEN)
