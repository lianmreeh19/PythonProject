# given the following: "the price of the shirt is 34$". find the product
sentence = "the price of the shirt is 34$"
index_1 = sentence.index("of the")+7
index_2 = sentence.index("is")
product = sentence[index_1:index_2-1]
print(product)