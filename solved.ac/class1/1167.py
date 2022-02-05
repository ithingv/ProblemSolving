word = input().lower()
is_duplicate = False
max_word = 0
result = ""
word_dict = {}

for alpha in word:
    if alpha not in word_dict:
        word_dict[alpha] = 1
    else:
        word_dict[alpha] += 1

for alpha, curr_value in word_dict.items():
    if max_word == curr_value:
        is_duplicate = True
    elif max_word < curr_value:
        max_word = curr_value
        is_duplicate = False
        result = alpha
        
if is_duplicate == True:
    print("?")
else:
    print(result.upper())