import random
menu = '''
Maak een keuze uit het menu
Typ 1 om de contacten te zien
Typ 2 om een contact toe te voegen
Typ 3 om een contact te verwijderen
Typ 4 om een contact aan te passen
'''

def print_menu():
	print(menu)

def contact_aanpassen(contacten):
	print(contacten)
	welk_contact_aanpassen = input("Welk contact wil je aanpassen? ")
	if welk_contact_aanpassen in contacten:
		nieuwe_waarde = input("Welke nieuwe waarde wil je dit contact geven? ")
		contacten_update = {welk_contact_aanpassen: nieuwe_waarde}
		weet_je_zeker_aanpassen = input("Weet je het zeker dat je de waarde van dit contact wil veranderen ja of nee ")
		if weet_je_zeker_aanpassen == "ja":
			contacten.update(contacten_update)
			print(contacten)
		elif weet_je_zeker_aanpassen == "nee":
			print("oke")

	else:
		opnieuw = input("Dat is niet mogelijk wil je het opnieuw proberen ja of nee. ")
		if opnieuw == "ja":
			contact_aanpassen(contacten)
		elif opnieuw == "nee":
			print("oke")

def contact_toevoegen(contacten):
	print(contacten)
	contact_naam_toevoegen = input("Voer de naam van het contact dat je wil toevoegen. ")
	contact_waarde_toevoegen = input("Voer een telefoon nummer of iets wat bij het contact hoort. ")

	if contact_naam_toevoegen in contacten:
		naam_bestaat_al = input("Dit contact bestaat al druk x om een ander contact toe te voegen of druk y om door te gaan. ")
		if naam_bestaat_al == "x":
			contact_toevoegen(contacten)
		elif naam_bestaat_al == "y":
			print("Hallo")
	else:
		dic_contacten_toevoegen = {contact_naam_toevoegen: contact_waarde_toevoegen}
		print(dic_contacten_toevoegen)
		weet_je_het_zeker = input("Weet je zeker dat je dit contact wil toevoegen ja of nee? ")
		if weet_je_het_zeker == "ja":
			contacten.update(dic_contacten_toevoegen)
			contacten_zien_of_niet = input("Het contact is toegevoegt aan de contacten typ y om de contacten te bekijken of druk x om door te gaan. ")
			if contacten_zien_of_niet == "y":
				print(contacten)
			elif contacten_zien_of_niet == "x":
				print("oke")
		elif weet_je_het_zeker == "nee":
			print("Oke dan niet")
		else:
			print("Dat is niet mogelijk")

def contact_verwijderen(contacten):
	print(contacten)
	contact_naam_verwijderen = input("Welk contact wilt u verwijderen ")
	if contact_naam_verwijderen in contacten:
		weetje_zeker_verwijderen = input("Weet je zeker dat je het contact wilt verwijderen ja of nee ")
		if weetje_zeker_verwijderen == "ja":
			del contacten[contact_naam_verwijderen]
			print(contacten)
		elif weetje_zeker_verwijderen == "nee":
			print("Oke dan niet ")
		else:
				print("Dat is niet mogelijk ")
	else:
		niet_mogelijk_verwijderen = input("dat is niet mogelijk wil je het opnieuw proberen ja of nee. ")
		if niet_mogelijk_verwijderen == "ja":
			contact_verwijderen(contacten)
		elif niet_mogelijk_verwijderen == "nee":
			print("oke ")

def input_gebruiker():
	print_menu()
	return input()

def runner_code(contacten):
	menu_keuze = input_gebruiker()
	if menu_keuze == "1":
		for key, value in contacten.items():
			print(key, value)
	elif menu_keuze == "2":
		contact_toevoegen(contacten)
	elif menu_keuze == "3":
		contact_verwijderen(contacten)
	elif menu_keuze == "4":
		contact_aanpassen(contacten)
	else:
		print("Dat is niet mogelijk ")

	wil_je_doorgaan = input("Druk x om te stoppen of druk y om doortegaan ")
	if wil_je_doorgaan == "x":
		print("doei")
	else:
		print("Nog een keer ")
		runner_code(contacten)

contacten = {"Maurits": "waarde", "Marijn": "waarde"}
runner_code(contacten)
