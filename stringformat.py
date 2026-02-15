letter="Hey my name is {} and i am from {}"
country="India"
name="archit"
print(letter.format(name,country))

#or
print(f"hey my name is {name} and i am from {country}")

price=29.999999
text=f"for only {price:.2f} dollars"
print(text)