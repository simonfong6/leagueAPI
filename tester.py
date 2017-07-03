#tester.py

import LOL

class Tester:
	testKey = "RGAPI-57a858b4-a696-40d2-8dad-d09a530eb83e"

	#Faker	
	SUMMONERNAME = "Hide on bush"
	SUMMONERID = "4460427"
	ACCOUNTID = "34440481"

	#Katarina
	CHAMPIONID = "55"

	#Boots of Speed
	ITEMID = "1001"

	#Thunderlord's Decree
	MASTERYID = "6363"

	#Greater Quintessence of Attack Damage
	RUNEID = "5335"

	#Flash
	SUMMONERSPELLID = "4"

	TOURNAMENTCODE = ""
	MATCHID = ""
	ACCOUNTID = ""

	def __init__(self):
		self.api = LOL.LeagueAPI(api_key=self.testKey, region=LOL.KR)

	def test_lol_static_data_v3(self):
		apis = {"allChampions": "/lol/static-data/v3/champions",
			"champion": "/lol/static-data/v3/champions/{}".format(None),
			"allItems": "/lol/static-data/v3/items",
			"item": "/lol/static-data/v3/items/{}".format(None),
			"language_strings": "/lol/static-data/v3/language-strings",
			"laguages": "/lol/static-data/v3/languages",
			"maps": "/lol/static-data/v3/maps",
			"allMasteries": "/lol/static-data/v3/masteries",
			"mastery": "/lol/static-data/v3/masteries/{}".format(None),
			"profile_icons": "/lol/static-data/v3/profile-icons",
			"realms": "/lol/static-data/v3/realms",
			"allRunes": "/lol/static-data/v3/runes",
			"rune": "/lol/static-data/v3/runes/{}".format(None),
			"allSumSpells": "/lol/static-data/v3/summoner-spells",
			"sumSpell": "/lol/static-data/v3/summoner-spells/{}".format(None),
			"versions": "/lol/static-data/v3/versions"}
		for key in apis:
			print self.api.lol_static_data_v3(getType=key, championId=self.CHAMPIONID, itemId=self.ITEMID, masteryId=self.MASTERYID, runeId=self.RUNEID, sumSpellId=self.SUMMONERSPELLID)

	def test_match_v3(self):
		apis = {"byTournament": "/lol/match/v3/matches/by-tournament-code/{}/ids",
			"matchById": "/lol/match/v3/matches/{}",
			"matchByIdAndTournament": "/lol/match/v3/matches/{}/by-tournament-code/{}".format(matchId, tournamentCode),
			"allMatchList": "/lol/match/v3/matchlists/by-account/{}",
			"matchListRecent": "/lol/match/v3/matchlists/by-account/{}/recent",
			"matchTimeline": "/lol/match/v3/timelines/by-match/{}"}
		for key in apis:
			json = self.api.match_v3(getType=key, tournamentCode=TOURNAMENTCODE, matchId=MATCHID, accountId=ACCOUNTID)
			print json

def main():
	tester = Tester()
	tester.test_lol_static_data_v3()

if(__name__ == "__main__"):
	main()
