#Ohjelma kysyy kaverien nimet
#Niin kauan kun vastaat, nimet kerätään.
#Kun vastaat välilyönnillä, ohjelma loppuu.
#Ja ohjelma tulostaa nimet

kaverilista = []
while True:
    nimi = input('Anna kaverisi nimi: ')
    if nimi == ' ':
        break
    elif len(nimi) > 5:
        kaverilista.append(nimi)
 
print(f'Tässä lista sun kavereistasi {kaverilista}')
