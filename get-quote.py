import random

def mine():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #last = len(quotes) - 1
  rnd_one = randomize(quotes)
  rnd_two = randomize(quotes)	
  print(quotes[rnd_one])
  print(quotes[rnd_two])
  
def randomize(quotes):
  last = len(quotes) - 1
  rnd = random.randint(0, last)	

  return rnd
  
if __name__== "__main__":
  mine()
