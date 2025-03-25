# pulire numero di tel da caratteri estranei
# i caratteri ammessi in entrata  sono: + 0123456789
# in uscita senza gli spazi e in caso
# del pref int 0039 diventa +39
def pulisci_numero(numero):
        risultato="+"
        parti_da=0      
        if numero[0:2]=="00":
                parti_da=2
        elif numero[0]=="+":
                parti_da=1
        else:
                raise Exception("errore")
        for x in numero[parti_da:]:
                if x!=" ":
                        risultato +=x
        return risultato
