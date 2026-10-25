def total(galleons, sickles, knuts):
    print(galleons*sickles,knuts)
coins = [100, 40, 23]
total(*coins) # unpack the list coins into seperate values
#like total(100,40,23)