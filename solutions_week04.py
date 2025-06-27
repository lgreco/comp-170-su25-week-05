
def longest_word(words: list[str]) -> str:
  longest = None
  if words is not None and len(words) > 0:
    longest = words[0]
    for word in words:
      if len(word) > len(longest):
        longest = word
  return longest

def shortest_word(words: list[str]) -> str:
  shortest = None
  if words is not None and len(words) > 0:
    shortest = words[0]
    for word in words:
      if len(word) < len(shortest):
        shortest = word
  return shortest

def odd_words(words: list[str]) -> list[str]:
  odds = None
  if words and len(words) > 0:
    odds = []
    for word in words:
      if len(word)%2 == 1:
        odds.append(word)
  return odds

def average_words(words: list[str]) -> list[str]:
  averages = None
  if words and len(words) > 0:
    averages = []
    avg = 0
    for word in words:
      avg += len(word)
    avg /= len(words)
    for word in words:
      if avg-1 <= len(word) and len(word) <= avg+1:
        averages.append(word)
  return averages

def intersect(foo: list[str], bar: list[str]) -> bool:
  intersection_found = False
  if foo and bar and len(foo) > 0 and len(bar) > 0:
    f = 0
    while not intersection_found and f < len(foo):
      b = 0
      while not intersection_found and b < len(bar):
        intersection_found = foo[f] == bar[b]
        b += 1
      f += 1
  return intersection_found
