# -*- coding: utf-8 -*

x = "There are %d types of people." % 10 #Costruisce la stringa "There are 10 types of people"
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #Costruisce la stringa "Those who know binary and those how don't"

print x #Stampa: "There are 10 types of people"
print y #Stampa: "Those who know binary and those how don't"

print "I said: %r." % x #Stampa: "I said: There are 10 types of people". Inserisce una stringa come oggetto in una altra stringa (2° livello di annidamento)
print "I also said: '%s'." % y #Stampa: "Those who know binary and those how don't"


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #sostituendo al nome delle variabili il loro rispettivo valore stringa, questa istruzione stamperà: "Isn't that joke so funny?! False"

w = "This is the left side of..."
e = "a string with a right side."

print w + e #sostituendo al nome delle variabili il loro rispettivo valore stringa, questa istruzione stamperà: "his is the left side of... a string with a right side."
