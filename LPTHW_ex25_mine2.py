from LPTHW_ex25 import *
 
#acquisisce una frase   
#sentence = raw_input("Scrivi una frase: ")
sentence = "mamma mia, sono diventato blu!"

print "La lista delle parole ottenute dalla frase inserita e': ",  break_words(sentence)
print

print "La lista ordinata delle parole ottenute dalla frase inserita e': ",  sort_words( break_words(sentence))
print

print "Come sopra, ma con una altra funzione: ",  sort_words( break_words(sentence))
print

print "La prima parola in ordine alfabetico della frase inserita e': ",  print_first_word( sort_words( break_words(sentence)))
print

print "L'ultima parola in ordine alfabetico della frase inserita e': ",  print_last_word( sort_words( break_words(sentence)))
print

print "Come sopra, ma con una altra funzione.La prima e l'ultima parola della frase inserita sono: ",  print_first_and_last(sentence)
print

print "Come sopra, ma con una altra funzione. La prima e l'ultima parola in ordine alfabetico della frase inserita sono: ",  print_first_and_last_sorted(sentence)
print
