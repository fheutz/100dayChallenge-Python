integerVar = 1234
doubleFloatVar = 1.234
stringVar = "Hello World"
listVar = [1,2,3,4]
toupleVar = (1,2,3,4)

# prints var on position x 
print(stringVar[3], stringVar[4], stringVar[2]) 

# length
print("length:", len(stringVar) )

# count letters
print("Number of l: ", stringVar.count("l"))

# Finding
print("Find 'orl':", stringVar.find("orl"))
print("Index 'orl':", stringVar.index("orl"))

# Slicing
print("Slice n' dice:", stringVar[0:4])
print("Slice n' dice from behind:", stringVar[:-3])
print("Slice n' dice from the front:", stringVar[-3:])

# Splitting
print("Split", stringVar.split(" "))

# Starts/Ends With
print("Starts with h: ", stringVar.startswith("H"), " ends with P: ", stringVar.endswith("P") )

# Repeat 
print("repeat " * 2, stringVar * 10)

# Replace
print("Replacing for compliments: " + stringVar.replace("World", "Beautiful"))

print("upside down", "".join(reversed(stringVar)))

print("concatenation: ", stringVar+"!", "full join", ":)".join(stringVar))

# .upper() .lower .title() .capitalize() .swapcase() for changing Capitalization < too lazy for that
# .strip() .lstrip() .rstrip() strips of leading and ending whitespaces

# Playspace
stringVar += "!"
print(stringVar)
stringVar *= 2
print(stringVar)

# the Format method seems to be intresting: you can define a string in which objects get transformed to a string
# "formstring".format(Data)
formString = "{1} {0} {2} {3}"
print ( formString.format("eins", "zwei", "drei", "vier") ) 

# Unicode decoding
formString = "{0!r} {0!a}"
print ( formString.format("ölf") ) 

# Padding
formString = "{:>100}"
print ( formString.format("I am cool") ) 
formString = "{0:20} {1}"
print ( formString.format("I am cool", "!") ) 
formString = "{0:^20} {1}"
print ( formString.format("I am cool", "!") ) 
formString = "{0:_^20} {1}"
print ( formString.format("I am cool", "!") ) 

formString = "{last} {first}"
data = {"first": "cool!", "last": "you are"}
print ( formString.format(**data) ) 

# Datestring Prettyprint
from datetime import datetime
formString = '{:%Y-%m-%d %H:%M}'
formStringEurope = '{:%H:%M %d.%m.%Y}'
data = datetime(2019, 11, 7, 12, 13)
print ("AMERICAN: ", formString.format(data), "EUROPEAN: ", formStringEurope.format(data))

formStringEurope = '{:%Y-%m-%d %H:%M}'
