import requests


https = "https://"
riotApi = ".api.riotgames.com"

BR = "br1"
EUNE = "eun1"
EUW = "euw1"
JP = "jp1"
KR = "kr"
LAN = "la1"
LAS = "la2"
NA = "na1"
OCE = "oc1"
TR = "tr1"
RU = "ru"
PBE = "pbe1"

class LeagueAPI:
	def __init__(self, api_key, region=NA):
		self.api_key = api_key
		self.host = https + region + riotApi

	def request(self, getType, apis, data=None):
		if(getType not in apis):
			raise InputError("{" + getType + "} is not a valid getType!")
		api = apis[getType]	
		url = self.host + api
		payload = {"api_key": self.api_key}
		r = None
		if(data == None):
			r = requests.get(url, params=payload)
		else:
			r = requests.post(url, params=payload, data=data)
		return r.json()
		
	def champion_mastery_v3(self, getType="all", summonerId=None, championId=None):
		apis = {"all": "/lol/champion-mastery/v3/champion-masteries/by-summoner/{}".format(summonerId),
			"champion": "/lol/champion-mastery/v3/champion-masteries/by-summoner/{}/by-champion/{}".format(summonerId, championId),
			"score": "/lol/champion-mastery/v3/scores/by-summoner/{}".format(summonerId)}
		return self.request(getType=getType, apis=apis)

	def champion_v3(self, getType=None, championId=None):
		apis = {"all": "/lol/platform/v3/champions",
			"champion": "/lol/platform/v3/champions/{}".format(championId)}
		return self.request(getType=getType, apis=apis)

	def league_v3(self, getType=None, queue=None, summonerId=None):
		apis = {"challenger": "/lol/league/v3/challengerleagues/by-queue/{}".format(queue),
			"leagues": "/lol/league/v3/leagues/by-summoner/{}".format(summonerId),
			"master": "/lol/league/v3/masterleagues/by-queue/{}".format(queue),
			"position": "/lol/league/v3/positions/by-summoner/{}".format(summonerId)}
		return self.request(getType=getType, apis=apis)

	def lol_static_data_v3(self, getType=None, championId=None, itemId=None, masteryId=None, runeId=None, sumSpellId=None):
		apis = {"allChampions": "/lol/static-data/v3/champions",
			"champion": "/lol/static-data/v3/champions/{}".format(championId),
			"allItems": "/lol/static-data/v3/items",
			"item": "/lol/static-data/v3/items/{}".format(itemId),
			"language_strings": "/lol/static-data/v3/language-strings",
			"laguages": "/lol/static-data/v3/languages",
			"maps": "/lol/static-data/v3/maps",
			"allMasteries": "/lol/static-data/v3/masteries",
			"mastery": "/lol/static-data/v3/masteries/{}".format(masteryId),
			"profile_icons": "/lol/static-data/v3/profile-icons",
			"realms": "/lol/static-data/v3/realms",
			"allRunes": "/lol/static-data/v3/runes",
			"rune": "/lol/static-data/v3/runes/{}".format(runeId),
			"allSumSpells": "/lol/static-data/v3/summoner-spells",
			"sumSpell": "/lol/static-data/v3/summoner-spells/{}".format(sumSpellId),
			"versions": "/lol/static-data/v3/versions"}
		return self.request(getType=getType, apis=apis)

	def lol_status_v3(self, getType="shard"):
		apis = {"shard": "/lol/status/v3/shard-data"}
		return self.request(getType=getType, apis=apis)

	def masteries_v3(self, getType="masteryPages", summonerId=None):
		apis = {"masteryPages": "/lol/platform/v3/masteries/by-summoner/{}".format(summonerId)}
		return self.request(getType=getType, apis=apis)

	def match_v3(self, getType="", tournamentCode=None, matchId=None, accountId=None):
		apis = {"byTournament": "/lol/match/v3/matches/by-tournament-code/{}/ids".format(tournamentCode),
			"matchById": "/lol/match/v3/matches/{}".format(matchId),
			"matchByIdAndTournament": "/lol/match/v3/matches/{}/by-tournament-code/{}".format(matchId, tournamentCode),
			"allMatchList": "/lol/match/v3/matchlists/by-account/{}".format(accountId),
			"matchListRecent": "/lol/match/v3/matchlists/by-account/{}/recent".format(accountId),
			"matchTimeline": "/lol/match/v3/timelines/by-match/{}".format(matchId)}
		return self.request(getType=getType, apis=apis)

	def runes_v3(self, getType=None, summonerId=None):
		apis = {"runes": "/lol/platform/v3/runes/by-summoner/{}".format(summonerId)}
		return self.request(getType=getType, apis=apis)

	def spectator_v3(self, getType=None, summonerId=None):
		apis = {"active_game": "/lol/spectator/v3/active-games/by-summoner/{}".format(summonerId),
			"featured_games": "/lol/spectator/v3/featured-games"}
		return self.request(getType=getType, apis=apis)

	def summoner_v3(self, getType="name", accountId=None, summonerName=None, summonerId=None):
		apis = {"account": "/lol/summoner/v3/summoners/by-account/{}".format(accountId),
			"name": "/lol/summoner/v3/summoners/by-name/{}".format(summonerName),
			"summonerId": "/lol/summoner/v3/summoners/{}".format(summonerId)}
		return self.request(getType=getType, apis=apis)

	#TODO
	def tournament_stub_v3(self, getType=None, tournamentCode=None, data=None):
		"""
		Creates and reads mock tournament codes, providers, and tournaments.

		Parameters
		----------
		getType : str
			Selects which api to use.
		tournamentCode : str
			Tournament identifier number.
		data : dict
			Data required for POST requests.

		Returns
		-------
		dict
			JSON data for the specified API.
		"""
		apis = {"mockCode": "/lol/tournament-stub/v3/codes",
			"mockLobbyEvents": "/lol/tournament-stub/v3/lobby-events/by-code/{}".format(tournamentCode),
			"mockProvider": "/lol/tournament-stub/v3/providers",
			"mockTournament": "/lol/tournament-stub/v3/tournaments"}
		return self.request(getType=getType, apis=apis, data=data)

	def tournament_v3(self, getType=None, tournamentCode=None, data=None):
		apis = {"createCode": "/lol/tournament/v3/codes",
			"updateCode": "/lol/tournament/v3/codes/{}".format(tournamentCode),
			"codeDTO": "/lol/tournament/v3/codes/{}".format(tournamentCode),
			"lobbyEvents": "/lol/tournament/v3/lobby-events/by-code/{}".format(tournamentCode),
			"createProvider": "/lol/tournament/v3/providers",
			"createTournament": "/lol/tournament/v3/tournaments"}
		return self.request(getType=getType, apis=apis, data=data)

class InputError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def main():
	pass

if(__name__ == "__main__"):
	main()


