from sys import argv #importa sys.argv

script, input_file = argv 
#spacchetta argv, ponendo
#script=argv[0] (nome dello script)
#input_file=argv[1]

def print_all(f): #dichiara una funzione di nome print_all, con parametro passato f
    print f.read() #legge il file cui e' associata l'oggetto f di tipo file, e poi lo stampa a std output

def rewind(f): #dichiara una funzione di nome rewind, con parametro passato f
    f.seek(0) #si sposta all'inizio del file cui l'oggetto f di tipo file si riferisce

def print_a_line(line_count, f): #dichiara una funzione di nome print_a_line, con paramentro passato f
    print line_count, f.readline() #legge una riga del file cui l'oggetto f di tipo file si riferisce, e poi la stampa a std output
    #Dall'output si vede bene come readline() mantenga lo \n a fine riga. Infatti, ciascuna riga stampata ha due a capo: quello della riga letta e quello inserito da print

current_file = open(input_file) #Inizializza la variabile current_file con un oggetto di tipo file associato al file il cui nome e' passato attraverso script

print "First let's print the hole file: \n"

print_all(current_file) #chiama la funzione print_all, stampando tutto il file cui l'oggetto current_file di tipo file fa riferimento

print "Now let's rewind, kind of like a tape."

rewind(current_file) #chiama la funzione rewind, riportandosi all'inizio del file cui l'oggetto current_file di tipo file fa riferimento

print "Let's print three lines:"

current_line = 1 #Inizializza current_line. current_line = 1
print_a_line(current_line, current_file) #chiama la funzione print_a_line, stampando a std output la prima linea del file cui l'oggetto current_file di tipo file fa riferimento

##current_line = current_line + 1 #(current_line)_new = (current_line)_old + 1 = 1 + 1 = 2
current_line += 1 #operatore incremento
print_a_line(current_line, current_file) #chiama la funzione print_a_line, stampando a std output la seconda linea del file cui l'oggetto current_file di tipo file fa riferimento

##current_line = current_line + 1 #(current_line)_new = (current_line)_old + 1 = 2 + 1 = 3
current_line += 1
print_a_line(current_line, current_file) #chiama la funzione print_a_line, stampando a std output la terza linea del file cui l'oggetto current_file di tipo file fa riferimento
