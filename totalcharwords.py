sentence=input("Enter sentence:")
total_char_with_space=len(sentence)

spaces=0
for i in range(0,total_char_with_space):
    if sentence[i]==" ":
        spaces+=1
print(spaces)
total_words=spaces+1
total_char_without_space=total_char_with_space-spaces
print("Total Char with space"+str(total_char_with_space))
print("Total Char without space"+str(total_char_without_space))
print("Total words"+str(total_words))
print("Total spaces"+str(spaces))