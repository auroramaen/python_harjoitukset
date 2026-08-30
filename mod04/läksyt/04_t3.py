# .lower() muuttaa käyttäjän vastauksen isoiksi kirjaimiksi
sukupuoli = input('Ilmoita sukupuoli (nainen, mies): \n').lower()
hg = int(input('Ilmoita hemoglobiiniarvo: \n'))

if (sukupuoli == 'nainen') and (117 <= hg <= 175):
    print(f'Hemoglobiiniarvo {hg} g/l on normaali.')
elif (sukupuoli == 'nainen') and hg < 117:
    print(f'Hemoglobiiniarvo {hg} g/l on alhainen')
elif (sukupuoli == 'nainen') and hg > 175:
    print(f'Hemoglobiiniarvo {hg} g/l on korkea.')
elif (sukupuoli == 'mies') and (134 <= hg <= 195):
    print(f'Hemoglobiiniarvo {hg} g/l on normaali.')
elif (sukupuoli == 'mies') and hg < 134:
    print(f'Hemoglobiiniarvo {hg} g/l on alhainen.')
elif (sukupuoli == 'mies') and hg > 195:
    print(f'Hemoglobiiniarvo {hg} g/l on korkea.')
    