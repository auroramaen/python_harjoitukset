pituus = int(input('Kerro kuhan pituus senttimetreinä: \n'))
pituus_sallittu = 37 - pituus

if pituus < 37:
    print(f'Laske kuha takaisin järveen. Kuha on {pituus_sallittu}cm alimmasta sallitusta pyyntimitasta.')
else:
    print(f'Kuha on {pituus}cm')