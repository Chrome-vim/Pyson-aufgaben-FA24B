eingabe = int(input("Gebebn sie ein Gesamtbetrag ein: "))
if eingabe > 10:
    rabatt = (eingabe * 10)/100
    discounterpreis = int(eingabe-rabatt)
    print("Discounterpreis",discounterpreis)
else:
   print(eingabe)