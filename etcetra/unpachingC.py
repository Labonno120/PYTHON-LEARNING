def total(galleons, sickles, knuts):
    print(galleons*sickles,knuts)
coins = {
    "galleons" : 100,
    "sickles" : 40,
    "knuts" :25
}
total(**coins) # unpack the dictionary coins into seperate values
#like total(galleons=100,sickles = 40,knuts=23)