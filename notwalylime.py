import pymongo

# name of dataset: Rick and Morty
# hyperlink: api.tvmaze.com/singleseasrch/shows?q=rick-&-morty&embed=episodes
# we download the data from the website into a file called "s". Then we read this data and convert it into a json dictionary. Finally we use the "episode" section of the data and put it into the database.

connection = pymongo.MongoClient("149.89.150.100")
db = connection.notwalylime
collection = db.rick_and_morty

def find_episode(e):
    ret = []
    all = collection.find( {"number":e} )
    for each in all:
        ret.append(each)
    return ret

def find_season(s):
    ret = []
    all = collection.find( {"season":s} )
    for each in all:
        ret.append(each)
    return ret

def find_season_episode(s, e):
    all = collection.find( {"season":s}, {"number":e} )
    for each in all:
        if each['number'] == e:
            return collection.find_one( {"_id": each['_id']} )
    
def find_name(n):
    return collection.find( {"name":n} )
    
print "================================================"
print "This are the test cases for find_episode(1)"
temp = find_episode(1)
for each in temp:
    print each
    print "   "

print "================================================"
print "This are the test cases for find_season(1)"
temp = find_season(1)
for each in temp:
    print each
    print "   "

print "================================================"
print "This are the test cases for find_season_episode()"
i = 1
while i < 4:
    print find_season_episode(1,i)
    print "    "
    i = i + 1
    
print "================================================"
print "This are the test cases for find_name(n)"
temp = find_name("Pilot")
for each in temp:
    print each
    print "   "
