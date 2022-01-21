print("-----------------------------------------------------------")
#I think I know classes! Don't judge naming. It is just to better understand it.
class test:
  def __init__(gay, hi, fuck):
    gay.hello = hi
    gay.sex = fuck
    
  def lol(gay):
    print("Hi, I'm " + str(gay.sex) + " and I want to intercourse " + gay.hello)

text = test("You", 18)
print(text.hello)
print(text.sex)
text.lol()