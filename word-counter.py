file = open("hamlet.txt","r")
text = file.read()
file.close()
words = text.split()

words_dict = {}

word_count = int(input("How many words would you like to check in 'Hamlet'? the maximum is {} words \n".format(len(text)-48)))

punctuation = '''!()-[]{};:\, <>./?@#$%^&*_~'''


for word in words[47:word_count + 47]:
 # print(word)
 word = word.lower()
 for c in word:
   if c in punctuation:
     word = word.replace(c,"")

 words_dict[word] = words_dict.get(word,0) + 1


keys = list(words_dict.keys())
best_key = keys[0]
worst_key = keys[0]

best_key_tied_count = 0
worst_key_tied_count = 0

for key in keys:
  count = words_dict[key]
  if count > words_dict[best_key]:
    best_key = key
  if count < words_dict[worst_key]:
    worst_key = key

for key in keys:
  count = words_dict.get(key,0)
  if words_dict[key] == words_dict[best_key] and key is not best_key:
    best_key_tied_count +=1
  if words_dict[key] == words_dict[worst_key] and key is not worst_key:
    worst_key_tied_count+=1

print("The word with the least amount of appearances was '{}' with {} appearance(s), tied with {} other word(s) \n".format(worst_key,words_dict[worst_key],worst_key_tied_count))
print("The word with the most amount of appearances was '{}' with {} appearance(s), tied with {} other word(s) \n".format(best_key,words_dict[best_key],best_key_tied_count))

read_all = input("Would you like to see a list of ALL of the apperances of each word? type Y to get a list of all occurences. \n")

if read_all.lower() == "y":
  for word in words_dict:
    print("The word '{}' appears {} time(s) in the first {} words of Hamlet".format(word,words_dict[word],word_count))

def get_specific_word(word):
  count = words_dict.get(str(word),0)
  print("The word '{}' appears {} time(s) in the first {} words of Hamlet".format(word,count,word_count))

specific_word = input("Would you like to to see how many times a specific word occurs in Hamlet? Type in the word you wish to see. Type 'STOP' to stop execution. \n")

while specific_word != "STOP":
  get_specific_word(specific_word)
  specific_word = input("Would you like to to see how many times a specific word occurs in Hamlet? Type in the word you wish to see. Type 'STOP' to stop execution. \n")