

#capitalize
text1 = "File Edit"
print(text1.capitalize())

#casefold

text2 = "FFFFFFFFFFFF"
print(text2.casefold)

#center

text3 = "Student"
print(text3.center(100))


#count

text4 = "FFFFFFIIIIIIIIIEEEEEEEWWWWWWWDFDFFFFFFFFFFFFFFFFFIIIIIIIIII"
print(text4.count("F"))


#encode

text5 = "HI"
print(text5.encode())

#endswith
print(text5.endswith("I"))

#expandtabs
print("expands tab ----------")
text6 = "FhelloFFFFFI\tIIIIIIIIE  EEEEEEWWWWWWWDFDFFFFFFFFFFFFFFFFFIIIIIIIIII"
print(text6.expandtabs(33))

#find
print("find ----------")
print(text6.find("hello"))

#format
print("format =======")
text7 = "I am ayush yadav and my age is {age}"
print(text7.format(age = 23))
