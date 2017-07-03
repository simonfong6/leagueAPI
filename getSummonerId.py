#getSummonerId.py

import sys
import LOL

args = sys.argv
summonerName = args[1]

api_key = "RGAPI-57a858b4-a696-40d2-8dad-d09a530eb83e"
api = LOL.LeagueAPI(region=LOL.NA, api_key=api_key)
summoner = api.summoner_v3(getType="name", summonerName=summonerName)
print summoner
print summoner["id"]
