class Song:
    def __init__(self, singer, songname):
        self.singer = singer
        self.songname = songname

s1 = Song('ABBA', 'Mamma Mia')
s2 = Song('Crazy Frog', 'Axel F')
s3 = Song('Madonna', 'Vogue')
s4 = Song('Britney Spears', 'Toxic')
s5 = Song('Darude', 'Sandstorm')
s6 = Song('singer1', 'song1')

class Playlist:
    def __init__(self):
        self.munlista = []

    def lisaa(self, biisi):
        self.munlista.append(biisi)

playlist = Playlist()
playlist.lisaa(s1)
print(playlist.munlista)
for item in playlist:
    print(item.singer)

#l1 = [s1, s2, s3]
#for item in l1:
#    print(item.singer)