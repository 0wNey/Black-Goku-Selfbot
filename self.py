import asyncio
from art import *
from termcolor import colored
import subprocess
import discord, json, pyfiglet
from discord.ext import commands





def self():
	subprocess.call('cls', shell=True)
	print(colored(text2art("Goku'Selfbot"), 'blue'))

	with open('./config.json') as f:
		config = json.load(f)

	t = config.get('token')
	p = config.get('prefix')

	Bot = discord.client
	bot = commands.Bot(Description="Test", command_prefix=p, self_bot=True)
	bot.remove_command('help')

	@bot.event
	async def on_ready():
		print("-"*60)
		print("=> Je suis connecté en tant que", bot.user)
		print("-"*60)

	@bot.command()
	async def ascii(ctx, *, args):
		await ctx.message.delete()
		text = pyfiglet.figlet_format(args)
		await ctx.send(f'```{text}```')


	@bot.command()
	async def embed(ctx, title, *, description):
		await ctx.message.delete()
		embed=discord.Embed(title=title, description=description)
		await ctx.send(embed=embed)

	@bot.command()
	async def help(ctx):
		await ctx.message.delete()
		titre="Panel Help"
		desc="\n/cmd\n**Liste des commandes**\n\n/fun\n**Affiche les commandes fun**\n\n/backup\n**Affiche les commandes backups**\n\n/moderation\n**Affiche les commandes moderation**\n\n/utile\n**Affiche les commandes info**\n\n/hack\n**Affiche les commandes hack**\n\n/statut\n**Affiche les commandes statut**"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_footer(text = "Goku Selfbot | Help Panel")
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/820338071199154187/208599.gif")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Lancée")
			break

	@bot.command()
	async def hack(ctx):
		await ctx.message.delete()
		titre="Panel Help Raid"
		desc="\n/raid\n**Crée 10 channel**\n\n/spam\n**Spam le message souhaité**\n\n/destroy\n**Supprimme tous les channels textuels/vocaux**\n\n"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/820337652431716432/1531319356_mastered_ultra_instinct_goku_gif.gif")
		embed.set_footer(text = "Goku Selfbot | Raid Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Hack Lancée")
			break

	@bot.command()
	async def statut(ctx):
		await ctx.message.delete()
		titre="Panel Custom Statut"
		desc="\n/stream\n**Stream ce que l'on veut**\n\n/watch\n**Regarde ce que l'on veut**\n\n/listening\n**Ecoute ce que l'on veut**\n\n/play\n**Joue a ce que l'on veut**"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/820337285463015484/giphy.gif")
		embed.set_footer(text = "Goku Selfbot | Statut Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Statut Lancée")
			break

	@bot.command()
	async def raid(ctx):
		await ctx.send("**Raid en cours d'exécution...** :gear:")
		guild = ctx.message.guild
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await guild.create_text_channel('hacked by orion-corp')
		await ctx.send("**Raid effectué avec succés !** :white_check_mark:")
		while True:
			print("=> Raid Lancé")
			break

	@bot.command()
	async def spam(ctx, *, arg):
		while spam:
			await ctx.send(arg)


	@bot.command()
	async def stop(ctx):
		while stop:
			spam = False

	@bot.command()
	async def stream(ctx, *, arg):
		await ctx.send("**Changement de statut...** :gear:")
		await bot.change_presence(activity=discord.Streaming(name=arg, url="https://twitch.tv/pewdipie"))
		await ctx.send("**Changement effectué avec succés !** :white_check_mark:")
		while True:
			print("=> Statut Changé")
			break

	@bot.command()
	async def play(ctx, *, arg):
		await ctx.send("**Changement de statut...** :gear:")
		await bot.change_presence(activity=discord.Game(name=arg))
		await ctx.send("**Changement effectué avec succés !** :white_check_mark:")
		while True:
			print("=> Statut Changé")
			break

	@bot.command()
	async def listen(ctx, *, arg):
		await ctx.send("**Changement de statut...** :gear:")
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg))
		await ctx.send("**Changement effectué avec succés !** :white_check_mark:")
		while True:
			print("=> Statut Changé")
			break

	@bot.command()
	async def watch(ctx, *, arg):
		await ctx.send("**Changement de statut...** :gear:")
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg))
		await ctx.send("**Changement effectué avec succés !** :white_check_mark:")
		while True:
			print("=> Statut Changé")
			break


	@bot.command()
	async def destroy(ctx):
		for c in ctx.guild.channels:
			await c.delete()



	bot.run(t, bot=False)





if __name__ == "__main__":
	self()