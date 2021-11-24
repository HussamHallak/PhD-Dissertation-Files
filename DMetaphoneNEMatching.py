import fuzzy
import csv
import itertools
from fuzzywuzzy import fuzz

nes = [line.strip() for line in open("nes.txt", 'r')]

fieldnames = ['NE1', 'NE2', 'Output']

fuzzy_dmeta_results_csv = open('fuzzy_dmeta_results.csv', 'w', newline='')
fuzzy_dmeta_writer = csv.DictWriter(fuzzy_dmeta_results_csv, fieldnames=fieldnames)
fuzzy_dmeta_writer.writeheader()

def fuzzy_dmeta_isEqual(ne1, ne2):
	dmeta = fuzzy.DMetaphone()
	if dmeta(ne1)[0] == dmeta(ne2)[0] or dmeta(ne1)[0] == dmeta(ne2)[1] or dmeta(ne1)[1] == dmeta(ne2)[0]:
		return 1
	else:
		return 0
			
for ne1, ne2 in itertools.combinations(nes, 2):
	if ne1 != ne2:
		fuzzy_dmeta_writer.writerow({'NE1': ne1, 'NE2': ne2, 'Output': fuzzy_dmeta_isEqual(ne1, ne2)})

fuzzy_dmeta_results_csv.close()

'''
print("dmeta")
dmeta = fuzzy.DMetaphone()
print(dmeta('Amin'))
print(dmeta('Joumana'))
'''

