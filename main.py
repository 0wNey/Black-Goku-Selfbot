import asyncio
from art import *
from termcolor import colored
import subprocess
import discord, json, pyfiglet
from discord.ext import commands





def main():
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
		await bot.change_presence(activity=discord.Streaming(name="Black-Goku-Selfbot", url="https://twitch.tv/pewdipie"))

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
		desc="`Prefix actuel : " + p + "`\n\n/cmd\n**Liste des commandes**\n\n/fun\n**Affiche les commandes fun**\n\n/moderation\n**Affiche les commandes moderation**\n\n/raid\n**Affiche les commandes raid**\n\n/statut\n**Affiche les commandes statut**\n\n/credit\n**Donne les informations du créateur du selfbot**"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_footer(text = "Goku Selfbot | Help Panel")
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/823138692189257728/f8dc4f7e2de553ed983b75199b2bdc1e.gif")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Lancée")
			break

	@bot.command()
	async def raid(ctx):
		await ctx.message.delete()
		titre="Panel Help Raid"
		desc="\n/create\n**Crée 10 channel**\n\n/spam\n**Spam le message souhaité**\n\n/stop\n**Stop le spam**\n\n/destroy\n**Supprimme tous les channels textuels/vocaux**\n\n"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/823184119281745952/2659116c2a560652d8fca0790c88a359.gif")
		embed.set_footer(text = "Black Goku Selfbot | Raid Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Raid Lancée")
			break

	@bot.command()
	async def statut(ctx):
		await ctx.message.delete()
		titre="Panel Custom Statut"
		desc="\n/stream\n**Stream ce que l'on veut**\n\n/watch\n**Regarde ce que l'on veut**\n\n/listen\n**Ecoute ce que l'on veut**\n\n/play\n**Joue a ce que l'on veut**"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/820337285463015484/giphy.gif")
		embed.set_footer(text = "Black Goku Selfbot | Statut Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Statut Lancée")
			break

	@bot.command()
	async def fun(ctx):
		await ctx.message.delete()
		titre="Panel Help Fun"
		desc="\n/ascii \n**Ecrit le message souhaité en art ascii**\n\n/embed\n**Ecrit le message souhaité dans un embed**\n\n/pp\n**Affiche la photo de profil de l'utilisateur mentionné**"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/823184736599015474/tumblr_static_tumblr_static_8047l7nf6gsgc40o8488kooog_focused_v3.gif")
		embed.set_footer(text = "Black Goku Selfbot | Fun Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Fun Lancée")
			break

	@bot.command()
	async def moderation(ctx):
		await ctx.message.delete()
		titre="Panel Help Modération"
		desc="\n/ban\n**Ban l'utilisateur mentionné**\n\n/kick\n**Kick l'utilisateur mentionné**"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/823139826807209984/ayPj3Db.gif")
		embed.set_footer(text = "Black Goku Selfbot | Panel Modération")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Modération Lancée")
			break

	@bot.command()
	async def cmd(ctx):
		await ctx.message.delete()
		titre="Panel Help Commandes"
		desc="\n/fun\n`ascii`, `embed`, `pp`\n\n/moderation\n`ban`, `kick`\n\n/utile\n`soon`\n\n/raid\n`create`, `spam`, `stop`, `destroy`\n\n/statut\n`stream`, `watch`, `listen`, `play`\n\n/credit\n`credit`"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url = "https://cdn.discordapp.com/attachments/485011383721787415/823185119493750834/09f06f40c24fe904b9fff5e47ca75ff4983e069ar1-500-281_hq.gif")
		embed.set_footer(text = "Black Goku Selfbot | Panel Help Cmd")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Cmd Lancée")
			break

	@bot.command()
	async def credit(ctx):
		await ctx.message.delete()
		titre="Panel Crédits"
		desc="Développer : 0wNey#7599\nLangage Utilisé : Python3.9\nTry Hack Me : https://www.tryhackme.com/p/0wNey\nGithub : https://github.com/0wNey"
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/485011383721787415/823144490218422292/62280680.png")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Crédit Lancée")
			break

	@bot.command()
	async def create(ctx):
		await ctx.send("**Raid en cours d'exécution...** :gear:")
		guild = ctx.message.guild
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await guild.create_text_channel('hacked by goku-selfbot')
		await ctx.send("**Raid effectué avec succés !** :white_check_mark:")
		while True:
			print("=> Raid Lancé")
			break

	@bot.command()
	async def spam(ctx, *, arg):
		while True:
			await ctx.send(arg)


	@bot.command()
	async def stop(ctx):
		while True:
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

	@bot.command()
	async def ban(ctx, member: discord.Member, *, reason=None):
		while True:
			try:
				await member.ban(reason=reason)
				await ctx.send(":white_check_mark: **L'utilisateur a été ban avec succés !**")
				print("=> Commande Ban Lancée")
				break
			except:
				await ctx.send(":x: **Vous ne possédez pas les permissions nécessaires pour effectuer cette action**")
				print("=> Commande Ban Interrompue")
				break

			

	@bot.command()
	async def kick(ctx, member: discord.Member, *, reason=None):
		while True:
			try:
				await member.kick(reason=reason)
				await ctx.send(":white_check_mark: **L'utilisateur a été kick avec succés !**")
				print("=> Commande Kick Lancée")
				break
			except:
				await ctx.send(":x: **Vous ne possédez pas les permissions nécessaires pour effectuer cette action**")
				print("=> Commande Kick Interrompue")
				break

	@bot.command()
	async def pp(ctx, user: discord.Member,):
		await ctx.message.delete()
		titre="{0}".format(user)
		desc=""
		embed=discord.Embed(title=titre, description=desc, color=0)
		embed.set_image(url=user.avatar_url)
		await ctx.send(embed=embed)
		while True:
			print("=> Commande pp Lancée")
			break

	@bot.command()
	async def ghost(ctx):
		await ctx.send("@everyone")
		await ctx.message.delete()
		while True:
			print("=> Ghost Ping Effectué")
			break

	bot.run(t, bot=False)





if __name__ == "__main__":
	main()
