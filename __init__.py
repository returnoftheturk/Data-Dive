import urllib

i=1
htmltext = urllib.urlopen("http://fantasy.premierleague.com/web/api/elements/" + str(i) + "/")

myfile = open("player_history.txt", "w")
myfile.close()
#   urllib.urlopen("http://fantasy.premierleague.com/web/api/elements/" + str(i) + "/")
 #   json.load(htlmtext)
print

#for i in range(1,1000):
 #   urllib.urlopen("http://fantasy.premierleague.com/web/api/elements/" + str(i) + "/")
 #   json.load(htlmtext)