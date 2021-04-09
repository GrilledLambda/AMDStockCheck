import discord, time , requests
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from bs4 import BeautifulSoup
import lxml
from BotConfigurations import TOKEN, GUILD, linkFile, refreshDelay, debug
#----------------------------

client = discord.Client() 

#-------------------------MAIN BOT CLASS--------------------------
class CheckStock:

    #checks if product link is in stock
    def checkAval(self, url, title=False):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, features="lxml")
       
        try:
            stock = soup.select("p.product-out-of-stock")[-1].get_text()
        except:
            stock = "Couldn't determine availability."
        
        if title:
            try:
                title = soup.select(".product-page-description >  h2")[-1].get_text()
            except:
                title = "Couldn't get product title"
            result = [title, stock]
            return result
        else:
            return stock

    #checks stock of link. If in stock it sends a discord message.
    def checkMe(self,url):
    
        embed=discord.Embed(title="**__IN STOCK ALERT__**", color=0xff0000) #an alerting red >:[
        stock = self.checkAval(url, True)
        if debug:
            print("stock:", stock)
        elif "Out of stock" not in stock[1]:
            embed.add_field(name=stock[0], value=f"**{stock[1]}**", inline=False)
            embed.add_field(name="Source:", value=f"**{url}**", inline=False)
            return  embed
        else:
            return False    

newBot = CheckStock()

#loops through .txt file and checks stock
def startBot():
    while True:
        with open(linkFile) as linkReader:
                for link in linkReader:
                    if debug:
                        print("current link:", link, "\n Checking Link...")
                    time.sleep(refreshDelay)
                    status = newBot.checkMe(link.replace("\n", ""))
                    if status == True:
                        channel = client.get_channel(GUILD)
                        channel.send("@everyone", embed=status)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f"{client.user} successfully connected to: {guild.name}")
    return startBot()

if __name__ == "__main__":
    client.run(TOKEN)
    
