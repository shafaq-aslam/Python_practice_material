
# 29. poem.txt contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in your python program and find out words with maximum occurance.

word_dict = {}
with open('Revision_day_2//poem.txt','r') as file:
    for line in file:
        words = line.split(' ')
        for word in words:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word] = 1

print(word_dict)
max_num_list = list(word_dict.values())
max_num = max(max_num_list)

print()
for key, val in word_dict.items():
    if val == max_num:
      print(f'Maximum word is: {key}\nOccurance of {key} is: {val}')




