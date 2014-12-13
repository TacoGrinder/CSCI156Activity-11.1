__author__ = 'ortus'

#1
nolamusic = {'Buzzoven':['Sore', 'At a Loss'], 'Weedeater':['Hot Doughnuts Now!', 'Jason the Dragon'],
             'Down':['NOLA', 'Bustle in your Hedgerow'], 'Eyehategod':['Dopesick', 'Take as Needed for Pain'],
             'HAARP': ['The Filth', 'Husks'], 'Humble Pie': ['As Safe as Yesterday Is', 'Humble Pie']}
#2
print(nolamusic['HAARP'])
#3
print(nolamusic.get('Down'))
#4
for band in nolamusic:
    for album in nolamusic[band]:
        print(album + " was released by " + band)
#5
for band in nolamusic:
    for album in nolamusic[band]:
        print(album + " was released by " + band)
    if band == "Humble Pie":
        print("I Like Humble Pie")