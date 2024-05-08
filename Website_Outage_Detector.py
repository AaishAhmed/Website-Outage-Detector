from bs4 import BeautifulSoup
import requests

#Getting input from user
page = input("Which website would you like to check? Enter 'Help' for a list of options: ")

page = page.lower()

#Help case: Multiple pages of websites, ends when website name is given
if page == "help":
    print("List of avaliable websites: Page 1 of 18. Type page number to go to page, or name of website to exit. ")
    print("000webhost, 15Five, 2k,\n8x8, Acanac, Access,\nAccor Hotels, Adobe Connect, ADP,\nAeroplan, Air Canada, Air Miles,\nAirbnb, Akamai, Alaska Airlines,\nAlibaba Cloud, AliExpress, Allegiant Air,\nAllianz, Allstream, Altima Telecom,\nAmazon, Amazon Alexa, Amazon Music,\nAmazon Prime Video")
    entry = input("Enter a page number or website name: ")

    while entry.isdigit():

        entry = int(entry)

        print()

        if 1 <= entry <= 18:

            if entry == 1:
                print("Page 1:")
                print("000webhost, 15Five, 2k,\n8x8, Acanac, Access,\nAccor Hotels, Adobe Connect, ADP,\nAeroplan, Air Canada, Air Miles,\nAirbnb, Akamai, Alaska Airlines,\nAlibaba Cloud, AliExpress, Allegiant Air,\nAllianz, Allstream, Altima Telecom,\nAmazon, Amazon Alexa, Amazon Music,\nAmazon Prime Video")
                entry = input("Enter a page number or website name: ")

            elif entry == 2:
                print("Page 2:")
                print("Ancestry, Anthem, Anydesk,\nApex Legends, App Store, Apple HomeKit,\nApple Music, Apple Pay, Apple Store,\nApple TV+, AppValley, Aptum Technologies,\nArcheAge, Archive of Our Own, ARK: Survival Evolved,\nAsana, Assassin's Creed, ATCO,\nAthena Security Inc, Banco Popular Dominicano, Bandwidth,\nBattlefield, BC Hydro, Beanfield,\nbeIN, Bell Aliant, Bell Canada,\nBell MTS, Best Buy Canada, Bet365")
                entry = input("Enter a page number or website name: ")

            elif entry == 3:
                print("Page 3:")
                print("Binance, Bing, BitChute,\nBlack Desert Online, Blackboard, Blizzard Battle.net,\nBlogger, BMO, BNN Bloomberg,\nBooking.com, Boom Beach, Box,\nBrama Telecom, Brawl Stars, Brawlhalla,\nBritish Airways, Broadridge Financial Solutions, Bumble,\nCall of Duty, Can Com Internet Inc, Candy Crush,\nCanva, Canvas by Instructure, Capital One,\nCareerShift, Carry Telecom, CBC,\nCenturylink, Chatr, Chuffed")
                entry = input("Enter a page number or website name: ")

            elif entry == 4:
                print("Page 4:")
                print("CIBC, CIK Telecom, CIRA Canadian Shield DNS,\nCisco Webex Teams, Clash of Clans, Clash Royale,\nClickFunnels, ClickUp, Cloudflare,\nCloudli, CNN, Coextro,\nCogeco, Cogent, Coinbase,\nColbaNet, CommStream, Comwave,\nCostco, Counter-Strike, Coursera,\nCrackle, Craigslist, Crave TV,\nCronoMagic, Crunchyroll, Dailymotion,\nDairy Queen, Dank Memer, Dark Souls")
                entry = input("Enter a page number or website name: ")

            elif entry == 5:
                print("Page 5:")
                print("Datto, Day One, DayZ,\nDazn, Dead By Daylight, Delta Air Lines,\nDesire2Learn, Desjardins, Destiny,\nDiablo, Discord, discovery+,\nDisney+, Distributel, DocHub,\nDoorDash, Dota 2, Dropbox,\nDuckduckgo, Duo, Duolingo,\nEA, EA Sports UFC, Eastlink,\neBay, Ebox, Ecobee,\nedX, Elite: Dangerous, ENMAX")
                entry = input("Enter a page number or website name: ")

            elif entry == 6:
                print("Page 6:")
                print("EPCOR, Epic Games Store, Equitable Bank,\nEscape from Tarkov, Etoro, Etsy,\nEVE Online, EVE Valkyrie, Execulink,\nExpedia, ExploreLearning, Facebook,\nFacebook Messenger, Facetime, Fall Guys,\nFallout, Fanfiction, FedEx,\nFidelity, Fido, Fifa,\nFigma, Final Fantasy, Fitbit,\nFive9, FiveM, Fizz,\nFlickr, Flightradar24, Flock")
                entry = input("Enter a page number or website name: ")

            elif entry == 7:
                print("Page 7:")
                print("For Honor, Fortnite, Forza,\nFox News, Freedom Mobile, Friday the 13th The Game,\nFundly, FundRazr, Fundserv,\nFunimation, Fur Affinity, Gab,\nGame of War, Garmin, Garmin Connect,\nGears of War, Gems Telecom, Genshin Impact,\nGfycat, Ghost Recon, GitHub,\nGmail, Go Daddy, GO Transit,\nGoFundMe, GOG.com, goodreads,\nGoogle, Google Ad Manager, Google Calendar")
                entry = input("Enter a page number or website name: ")

            elif entry == 8:
                print("Page 8:")
                print("Google Cloud, Google Drive, Google Duo,\nGoogle Hangouts, Google Maps, Google Meet,\nGoogle Nest, Google Play, GoToConnect,\nGoToMeeting, Grammarly, Gran Turismo,\nGrindr, GTA 5, Guild Wars 2,\nHalo, Halo Infinite, Hay Day,\nHayu, Hearthstone, Helldivers 2,\nHiBid, Hinge, Hipchat,\nHive Social, Honeywell, Hootsuite,\nHosting24, HostPapa, HSBC")
                entry = input("Enter a page number or website name: ")

            elif entry == 9:
                print("Page 9:")
                print("Hubspot, Hue, HughesNet,\nHulu, Hunt: showdown, IBM Cloud,\niCloud, IKEA, iMessage,\nImgur, IMVU, Indeed,\nIndiegogo, Ingress, Instacart,\nInstagram, Interac, Interactive Brokers,\nIQcent, itslearning, iTunes,\nJackbox, JetBlue Airways, Jira,\nJuno, Keap, Keeper,\nKick, Kickstarter, Kijiji")
                entry = input("Enter a page number or website name: ")

            elif entry == 10:
                print("Page 10:")
                print("Kik, Klarna, Knockout City,\nKOHO, Koodo, Kraken,\nlast.fm, LastPass, League of Legends,\nLightspeed, Line, LinkedIn,\nLost Ark, Madden, Mail.com,\nMailbox, Mastodon, McDonalds app,\nMCSNet, Media Temple, MEGA,\nMetro Loop, MeWe, Microsoft 365,\nMicrosoft Azure, Microsoft Store, Microsoft Teams,\nMilanote, Minecraft, Mitel")
                entry = input("Enter a page number or website name: ")

            elif entry == 11:
                print("Page 11:")
                print("MLB The Show, MLB TV, Moneris,\nMonopoly Go!, Monster Hunter, Montréal Metro,\nMordhau, My Fitness Pal, National Bank of Canada,\nNBA 2k, Need for Speed, Netatmo,\nNetflix, NetZero, Neverwinter,\nNew World, NFL Network, Nintendo eShop,\nNintendo Network, Nintendo Switch Online, No Man's Sky,\nNorthernTel, Northwestel, OkCupid,\nOkta, Omegle, Onelogin,\nOnStar, OpenAI, OpenDNS")
                entry = input("Enter a page number or website name: ")

            elif entry == 12:
                print("Page 12:")
                print("Opsgenie, Oricom Internet, Origin,\nOverwatch 2, OVHcloud, Paladins,\nParamount+, Path of Exile, Patreon,\nPAYDAY 2, Paypal, PC Optimum,\nPeloton, Phasmophobia, Photobucket,\nPinterest, Piper, Planetside2,\nPlaystation Network, PlentyOfFish, Plex,\nPokémon Go, Pokerstars, Poki,\nPrezi, Primus, Printify,\nProcore, Proofpoint, PUBG Battlegrounds")
                entry = input("Enter a page number or website name: ")

            elif entry == 13:
                print("Page 13:")
                print("Public Mobile, Qlik, Qtrade Direct Investing,\nQuad9, Questrade, Quickbooks Online,\nQuizup, Rabb.it, RadarScope,\nRainbow Six, Razer, RBC,\nRealtor.ca, Rec Room, Red Dead Redemption,\nReddit, Redfin, Resy,\nReturnal, Ring, RingCentral,\nRoblox, Rocket League, Rogers,\nRoll20, Rumble, RuneScape,\nSage, Salesforce, Sarahah")
                entry = input("Enter a page number or website name: ")

            elif entry == 14:
                print("Page 14:")
                print("Sasktel, Scotiabank, Sea of Thieves,\nSecond Life, ServiceNow, Shaw,\nShopify, Shoplazza, Signal,\nSimplii, Siri, SiriusXM,\nSkipTheDishes, Skype, Skype for Business,\nSlack, Slideshare, Smartsheet,\nSmite, Snapchat, Sonos,\nSoundcloud, Sourceforge, Speedtest,\nSplunk, Spotify, Square,\nSquarespace, Stack Overflow, Star Trek Online: House Divided")
                entry = input("Enter a page number or website name: ")

            elif entry == 15:
                print("Page 15:")
                print("Star Wars Battlefront, Starbucks, Starlink,\nStart Communications, Startpage, Steam,\nSteep, Storm Internet, Strava,\nStumble Guys, SugarDaddyMeet, Summoners War,\nTangerine, Tango, Tbaytel,\nTD Ameritrade, TD Canada Trust, TeamViewer,\nTekSavvy, Télébec, Telegram,\nTelnet, Telus, Tencent Cloud,\nTeraGo, Tesla, The Division,\nThe Elder Scrolls Online, The Huffington Post, The Simpsons Tapped out")
                entry = input("Enter a page number or website name: ")

            elif entry == 16:
                print("Page 16:")
                print("The Sims 4, The Weather Channel, Thingiverse,\nThinkific, Ticketmaster, TikTok,\nTinder, Tingleflow, Tip Transparency,\nTitanfall, Toronto Stock Exchange, Toronto Transit Commission,\nTrakt, Translink, Trello,\nTrove, Trustpilot, Tumblr,\nTuneIn, TunnelBear, TurboTax,\nTurkish Airlines, Tutanota, Tweakbox,\nTwitch, Uber, Uber Eats,\nUbisoft Connect, Udemy, UFC")
                entry = input("Enter a page number or website name: ")

            elif entry == 17:
                print("Page 17:")
                print("Ulule, United Airlines, UpdraftPlus,\nUPS, Valorant, Vancity,\nVD Wireless Tech Inc, Velcom, Venmo,\nViber, Vidéotron, Viki,\nVimeo, Virgin Mobile, Visa,\nVMedia, Vonage, VPN Unlimited,\nVRChat, Walmart Canada, War Thunder,\nWarface, Warframe, Wattpad,\nWaveapps, Wayfair, Waze,\nWebex, Webtoon, Weightwatchers")
                entry = input("Enter a page number or website name: ")

            elif entry == 18:
                print("Page 18:")
                print("Wemo, Western Union, WestJet,\nWeTransfer, Whatsapp, WhatsApp Business,\nWhisper, Wikipedia, Wish,\nWisp, Wix, Wordpress.com,\nWorld of Tanks, World of Warcraft, World of Warships,\nWWE Network, Wyze, X (Twitter),\nXbox Live, Xoom, Xplornet,\nYahoo, Yahoo Mail, Yak,\nYelp, Youtube, Youtube Music,\nYubo, Z1 Battle Royale, ZoHo,\nZoom, Zwift, Zynga")
                entry = input("Enter a page number or website name: ")
        
        else:
            print("Please enter a valid page number between 1 and 18.")
        
    else:
        #Two different cases, websites with spaces may be replaced with dashes or no spaces
        page1 = entry.lower()
        page2 = entry.lower()

        page1 = page1.replace(" ", "-")
        page2 = page2.replace(" ", "")

else:
    page1 = page.replace(" ", "-")
    page2 = page.replace(" ", "")

print()


#Storing site name, getting website, checking if valid
#Using downdetector.ca for information
site1 = "https://downdetector.ca/status/" + page1 + "/"
website1 = requests.get(site1)

site2 = "https://downdetector.ca/status/" + page2 + "/"
website2 = requests.get(site2)


#Checking if website is valid or not
while (website1.status_code != 200) and (website2.status_code != 200) :
    page = input("Error finding website name. Please try again: ")
    page1 = page.lower()
    page2 = page.lower()

    page1 = page.replace(" ", "-")
    page2 = page.replace(" ", "")

    site1 = "https://downdetector.ca/status/" + page1 + "/"
    site2 = "https://downdetector.ca/status/" + page2 + "/"

    website1 = requests.get(site1)
    website2 = requests.get(site2)

    print()


if website1.status_code != 200:
    website = site2
else:
    website = site1


#Beginning webscraping of downdetector.ca
website = requests.get(website).text

bs = BeautifulSoup(website, 'lxml')

status = bs.find('div', class_= 'h2 entry-title').text

#Checking if problems or not
if "possible problems" in status.strip():
    print("There are multiple users reporting issues accessing this website/service.")
    print("There is likely an issue at", page)

else:
    print("This website/service is running smoothly for most users!")
    print("If there is an issue it is likely on your side. Try checking your internet connection or on a different device")





