adn1 = ("A", "C", "T", "G")
adn2 = ("C", "T", "C", "A")
print adn1
print adn2

adn3 = adn1 + adn2

print adn3
print len(adn3) 
# error, tuples are read only
# and1[0] = "T"

adn4 = ("A", "C", "G") 
adn4 = adn4 * 3
print and4 
