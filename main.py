import asyncio
import subprocess
import discord, json, pyfiglet
from discord.ext import commands





def main():
	subprocess.call('cls', shell=True)
	print("""
██╗   ██╗ ██████╗██╗  ██╗██╗██╗  ██╗ █████╗     ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██║   ██║██╔════╝██║  ██║██║██║  ██║██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██║   ██║██║     ███████║██║███████║███████║    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
██║   ██║██║     ██╔══██║██║██╔══██║██╔══██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
╚██████╔╝╚██████╗██║  ██║██║██║  ██║██║  ██║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
 ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                                                                                                          
""")

	with open('./config.json') as f:
		config = json.load(f)

	t = config.get('token')
	p = config.get('prefix')

	Bot = discord.client
	bot = commands.Bot(Description="Test", command_prefix=p, self_bot=True)
	bot.remove_command('help')
	user = bot.get_user
	
	
	@bot.event
	async def on_ready():
		print("-"*60)
		print("=> Je suis connecté !")
		print("-"*60)
		print("=> Username : ", bot.user)
		print("-"*60)
		print("=> ID : ", bot.user.id)
		print("-"*60)
		print("=> Prefix : ", p)
		print("-"*60)
		print("\n=> Logs De Commandes : \n")
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
		desc="`Prefix actuel : " + p + "`\n\n/cmd\n**Liste des commandes**\n\n/fun\n**Affiche les commandes fun**\n\n/moderation\n**Affiche les commandes moderation**\n\n/raid\n**Affiche les commandes raid**\n\n/statut\n**Affiche les commandes statut**\n\n/credit\n**Donne les informations du créateur du selfbot**"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
		embed.set_footer(text = "⛩️ | Uchiha Project | Help Panel")
		embed.set_image(url = "https://i.pinimg.com/originals/a9/ee/de/a9eede5023a456a29a5eaa6a44a1f838.gif")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Lancée")
			break

	@bot.command()
	async def raid(ctx):
		await ctx.message.delete()
		titre="Panel Help Raid"
		desc="`Prefix actuel : " + p + "`\n\n/create\n**Crée 10 channel**\n\n/spam\n**Spam le message souhaité**\n\n/stop\n**Stop le spam**\n\n/destroy\n**Supprimme tous les channels textuels/vocaux**\n\n"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
		embed.set_image(url = "https://i.pinimg.com/originals/a9/ee/de/a9eede5023a456a29a5eaa6a44a1f838.gif")
		embed.set_footer(text = "⛩️ | Uchiha Project | Raid Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Raid Lancée")
			break

	@bot.command()
	async def statut(ctx):
		await ctx.message.delete()
		titre="Panel Custom Statut"
		desc="`Prefix actuel : " + p + "`\n\n/stream\n**Stream ce que l'on veut**\n\n/watch\n**Regarde ce que l'on veut**\n\n/listen\n**Ecoute ce que l'on veut**\n\n/play\n**Joue a ce que l'on veut**"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
		embed.set_image(url = "https://i.pinimg.com/originals/a9/ee/de/a9eede5023a456a29a5eaa6a44a1f838.gif")
		embed.set_footer(text = "⛩️ | Uchiha Project | Statut Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Statut Lancée")
			break

	@bot.command()
	async def fun(ctx):
		await ctx.message.delete()
		titre="Panel Help Fun"
		desc="`Prefix actuel : " + p + "`\n\n/ascii \n**Ecrit le message souhaité en art ascii**\n\n/embed\n**Ecrit le message souhaité dans un embed**\n\n/pp\n**Affiche la photo de profil de l'utilisateur mentionné**"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
		embed.set_image(url = "https://i.pinimg.com/originals/a9/ee/de/a9eede5023a456a29a5eaa6a44a1f838.gif")
		embed.set_footer(text = "⛩️ | Uchiha Project | Fun Panel")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Fun Lancée")
			break

	@bot.command()
	async def moderation(ctx):
		await ctx.message.delete()
		titre="Panel Help Modération"
		desc="`Prefix actuel : " + p + "`\n\n/ban\n**Ban l'utilisateur mentionné**\n\n/kick\n**Kick l'utilisateur mentionné**\n\n/clear\n**Clear 15 messages**"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
		embed.set_image(url = "https://i.pinimg.com/originals/a9/ee/de/a9eede5023a456a29a5eaa6a44a1f838.gif")
		embed.set_footer(text = "⛩️ | Uchiha Project | Panel Modération")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Modération Lancée")
			break

	@bot.command()
	async def cmd(ctx):
		await ctx.message.delete()
		titre="Panel Help Commandes"
		desc="`Prefix actuel : " + p + "`\n\n/fun\n`ascii`, `embed`, `pp`\n\n/moderation\n`ban`, `kick`\n\n/utile\n`soon`\n\n/raid\n`create`, `spam`, `stop`, `destroy`\n\n/statut\n`stream`, `watch`, `listen`, `play`\n\n/credit\n`credit`"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
		embed.set_image(url = "https://i.pinimg.com/originals/a9/ee/de/a9eede5023a456a29a5eaa6a44a1f838.gif")
		embed.set_footer(text = "⛩️ | Uchiha Project | Panel Help Cmd")
		await ctx.send(embed=embed)
		while True:
			print("=> Commande Help Cmd Lancée")
			break

	@bot.command()
	async def credit(ctx):
		await ctx.message.delete()
		titre="Panel Crédits"
		desc="Développer : 0wNey#7599\nLangage Utilisé : Python3.9\nTry Hack Me : https://www.tryhackme.com/p/0wNey\nGithub : https://github.com/0wNey"
		embed=discord.Embed(title=titre, description=desc, color=10038562)
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
	async def clear(ctx, amount=15): 
		while True:
			try:
				await ctx.channel.purge(limit=amount)
				await ctx.send("**Commande Clear Effectuée Avec Succés** :white_check_mark:")
				print("=> Commande Clear Lancée")
				break
			
			except:
				await ctx.send("**Vous ne possédez pas les permissions nécessaires pour effectuer cette action** :x:")
				print("=> Commande Clear Interrompue")
				break

	bot.run(t, bot=False)





if __name__ == "__main__":
	main()
