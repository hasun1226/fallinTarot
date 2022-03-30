import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!")
client = discord.Client(intents=intents)

embedS = discord.Embed(title="☆공지사항☆", description="", color=0xFFFFFF)
embedS.set_thumbnail(url="http://drive.google.com/uc?export=download&id=17q0DCBUJrJanmjNNR3ujul5YxVcNkDny")
embedS.add_field(name="안녕하세요, 폴인타로입니다", value="단톡방과 마찬가지로 서로 다른 분들이 많이 모인 곳이니 " + \
                "모두를 존중해주시기 바라며, 상대방을 비난하거나 욕설을 하는 등, " + \
                "디스코드 내 불화나 분란 조장의 기미가 발견 될 시 단톡방과 디스코드 모두에서 추방합니다.\n" + \
                "모두와 함께 타로를 공부하고 어느 누구도 공부할 기회로부터 소외되지 않도록 다음 규칙들을 준수해주시기 바랍니다.", inline=False)
embedS.add_field(name="타로 리딩",
                value="디스코드 내에서 리딩을 하실 때, 단톡방에도 잊지말고 카드 사진을 올려주세요!\n" + \
                "본인의 리딩은 올리지 않아도 되나, 배열법과 질문까지 단톡방에 알려주시고 디스코드에서 리딩을 진행하고 있음을 " + \
                "알 수 있게 디스코드에서 누구누구와 리딩하고 있는지도 알려주세요.\n" + \
                "예시는 우측의 사진을 참고해주세요.", inline=False)
embedS.add_field(name="각 방의 용도",
                value="이야기방 : 자유롭게 리딩을 하면서 일상 대화를 주고 받을 수 있는 방\n" + \
                "진실의 방 : 민감한 주제나 개인적인 이야기를 나눌 수 있는 방\n" + \
                "공부방 : 기존에 약속 된 시간에 진행하는 공부를 하는 방", inline=False)
embedS.set_footer(text="디스코드도 좋지만 단톡방도 관심 많이 가져주세요~ 한 달 30톡 못 채우시면 숙제가 있어요!",
                 icon_url="https://us.123rf.com/450wm/zo3listic/zo3listic1905/zo3listic190500090/125123133-%EB%8A%90%EB%82%8C%ED%91%9C-%EC%9C%84%ED%97%98-%EA%B8%B0%ED%98%B8%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%A3%BC%EC%9D%98-%ED%91%9C%EC%8B%9C-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%9C%84%ED%97%98-%EA%B2%BD%EA%B3%A0-%EC%A3%BC%EC%9D%98-%ED%91%9C%EC%8B%9C.jpg?ver=6")

@bot.event
async def on_ready():
    print('Loggend in Bot: ', bot.user.name)
    print('Bot id: ', bot.user.id)
    print('connection was succesful!')
    print('https://discord.com/oauth2/authorize?client_id=958753736346443848&permissions=8&scope=bot')

@bot.command(aliases=['공지사항', '공'])
async def Announcement(ctx):
    await ctx.send(embed=embedS)
    
@client.event
async def on_member_join(member):
    channel = client.get_channel('936620125006725123')
    await channel.send(embed=embedS) # channel에 보내기
    await member.send('welcome !')

bot.run('OTU4NzUzNzM2MzQ2NDQzODQ4.YkR6_w.KaBAnYbqU18-LHMsHogX3JWUPyE')

# Invite link: https://discord.com/oauth2/authorize?client_id=958753736346443848&permissions=8&scope=bot