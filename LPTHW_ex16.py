from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." #La finalita' di ^C penso sia quella di abortire il programma
print "If you do want that, hit RETURN." #La finalita' dell'invio a capo e' solo quella di andare avanti. Penso un qualsiasi input dato a linea di comando sortisca lo stesso effetto.

raw_input("?") #Lo scopo di tale comando e' solo quello di o abortire il programma o passare oltre. Per questo non e' necessario salvare l'input ricevuto da linea di comando.

print "Opening the file..."
target = open(filename, 'w') #supp: 'w' indica che il file e' aperto in modalita' scrittura. Restituisce un oggetto file relativo al file il cui percorso e' contenuto in filename (stringa passata come argomento allo script)

print "Truncating the file. Goodbye!"
target.truncate() #cancella il contenuto attuale del file cui l'oggetto file contenuto nella variabile target fa riferimento.

print "Now I'm going to ask you three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) #scrive sul file cui l'oggetto file contenuto nella variabile target fa riferimento (precedentemente svuotato) la stringa inserita da linea di comando e salvata nella variabile line1
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#modo alternativo per usare una sola volta il metodo write, facendo uso di stringhe, string formatters e escape characters
string = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(string)

print "And finally, we close it."
target.close() #chiude il file cui l'oggetto file contenuto nella variabile target fa riferimento.

