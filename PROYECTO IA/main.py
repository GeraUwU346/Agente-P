import os, random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.client(intents=intents)




@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    frase_cada_cierto_tiempo.start()
    

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_image_url():    
    url = 'https://random.photo/api/random'
    res = requests.get(url)
    data = res.json()
    return data['image']

#1
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
#2
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
#3
def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']
#4
def get_pokemon_image_url():    
    url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    res = requests.get(url)
    data = res.json()
    return data['sprites']['front_default']
#5
def get_tokio_image_url():    
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url)
    data = res.json()
    return data['data'][0]['attributes']['posterImage']['tiny']


phrases = [
   "Unta una mezcla de cal y agua en tus plantas. Te lo agradecerán",
   "Usa rocas pequeñas, algodon, arena y tela para crear un filtro de agua!",
   "Recolecta el agua de fugas o goteras!",
   "La basura organica es un muy buen fertilizante",
   "la mejor hora de regar las plantas es en la mañana",
   "Realizar una pequeña huerta casera es una de las mejores cosas que puedes hacer",
   "Si juntas ajo, vinagre y agua crearás un insecticida muy efectivo"   ]

CHANNEL_ID = 1199170804504608780

@bot.command.loop(minutes=60)

async def frase_cada_cierto_tiempo():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        frase = random.choice(phrases)
        await channel.send(phrases)
            
async def fotos(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_image_url()
    await ctx.send(image_url)


    
#1
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
#2
@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
#3
@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando fox, 
    el programa llama a la función get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)
#4
@bot.command('pokemon')
async def pokemon(ctx):
    '''Una vez que llamamos al comando pokemon, 
    el programa llama a la función get_pokemon_image_url'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)
#5
@bot.command('tokio')
async def tokio(ctx):
    '''Una vez que llamamos al comando tokio, 
    el programa llama a la función get_tokoi_image_url'''
    image_url = get_tokio_image_url()
    await ctx.send(image_url)
    

    
    

bot.run("MTE5OTE2OTk3OTUxMDE3Nzg0NA.GWaTXY._dW_Uur6ivntgGMQq6QMvI4BRpKaw_SAi7FAxw")








