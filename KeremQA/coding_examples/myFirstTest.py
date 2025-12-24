full_name = "Lian Mreeh"
index_1 = full_name.index(" ")
first_name_by_slicing = full_name[0:index_1]
# another way: first_name = full_name[:index_1]
last_name_by_slicing = full_name[index_1+1:len(full_name)] # the +1 is in order to remove the space in the beginning of the last name
# another way: last_name = full_name[index_1+1:]
print(full_name)
print(f"first name: {first_name_by_slicing}, last name: {last_name_by_slicing}")

full_name = full_name.replace("Lian", "Lilo")
print(full_name)
# the command "replace" replaces a word with a new word that I pick

sentence = "hi my name is Lian, I live in daliat el carmel"
index_2 = sentence.index("in")+3
slice_in_opposite_order = sentence[index_2:-9]
# the minus before the number is in order to slice the sentence from the opposite order
print(slice_in_opposite_order)

words = sentence.split(" ")
print(words)
# the command "split" slicing a sentence by something that I pick, and place them in a list

