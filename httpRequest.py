import requests
import pprint
import json
import datetime

host = "https://na1.api.riotgames.com"
apiLol = "/api/lol"
region = "na"
version = "1.3"
api = "/game/by-summoner"
summonerId = "69921165"
options = "recent"

url = host + apiLol + "/" + region + "/v" + version + api + "/" + summonerId + "/" + options

payload = {"api_key": "RGAPI-57a858b4-a696-40d2-8dad-d09a530eb83e"}

r = requests.get(url, params=payload)

jsonData = r.json()

print r.url
print ""
print "{}\t\t\t{}\t{}\t{}".format("Date", "Kills", "Deaths", "Assists")

totalKills, totalDeaths, totalAssists = 0, 0, 0
for game in jsonData["games"]:
	print game["gameId"]
	timestamp = game["createDate"]
	secs = timestamp/1000
	date = datetime.datetime.fromtimestamp(secs).strftime("%Y-%m-%d %H:%M:%S")
	stats = game["stats"]
	kills = stats["championsKilled"]
	if "numDeaths" in stats:
		deaths = stats["numDeaths"]
	else:
		deaths = 0
	assists = stats["assists"]
	totalKills += kills
	totalDeaths += deaths
	totalAssists += assists
	print "{}\t{}\t{}\t{}".format(date, kills, deaths, assists)

print "{}\t\t\t{}\t{}\t{}".format("Totals:", totalKills, totalDeaths, totalAssists)

