

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
