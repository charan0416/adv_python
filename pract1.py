# import re
#
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print(True)
# else:
#     print(False)

#
#
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
#
#
# txt = "heo planet"
#
# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
#
# x = re.findall("he.+o", txt)
#
# print(x)

# from re import split
#
# print(split('\W+', 'Words, words , Words'))
# print(split('\W+', "Word's words Words"))
# print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
# print(split(d+','On 12th Jan 2016, at 11:02 AM'))
#
#
# import re
# print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
# print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
# print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))
# #

#
# # import re
# print(re.sub('ub', '~*', 'Subject has Uber booked already',
#              flags=re.IGNORECASE))
# print(re.sub('ub', '~*', 'Subject has Uber booked already'))
# print(re.sub('ub', '~*', 'SUBject has uber booked already',
#              count=1, flags=re.IGNORECASE))
# print(re.sub(r'AND', ' & ', 'Baked Beans And Spam',
#
#               flags=re.IGNORECASE))

# # import re
#
# print(re.subn('ub', '~*', 'Subject has Uber booked already'))
#
# t = re.subn('ub', '~*', 'Subject has Uber booked already',
#             flags=re.IGNORECASE)
# print(t)
# print(len(t))
# print(t[0])


#
# # import re
# print(re.escape("This is Awesome even 1 AM"))
# print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))
#
# import re
# s = "Welcome to GeeksForGeeks"
# res = re.search(r"\bG", s)
# print(res.re)
# print(res.string)


# import re
# p = re.compile('\d')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
#
# p = re.compile('\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


# import re
#
# p = re.compile('\w')
# print(p.findall("He said * in some_lang."))
#
# p = re.compile('\w+')
# print(p.findall("I went to him at 11 A.M., he \
# said *** in some_language."))
#
# p = re.compile('\W')
# print(p.findall("he said *** in some_language."))

# import re
# p = re.compile('ab*')
# print(p.findall("ababbaabbb"))


import re
#

# match = re.search(regex, "I was born on June 24")
# if match != None:
#     print ("Match at index %s, %s" % (match.start(), match.end()))
#     print ("Full match: %s" % (match.group(0)))
#     print ("Month: %s" % (match.group(1)))
#     print ("Day: %s" % (match.group(2)))
#
# else:
#     print ("The regex pattern does not match.")


# import re
# s = 'geeks.forgeeks'
#
# # without using \
# match = re.search(r'.', s)
# print(match)
#
# # using \
# match = re.search(r'\.', s)
# print(match)

# import re
#
# pattern = r"abc"
# text = "abcdef"
# result = re.match(pattern, text)
#
# if result:
#     print("Match found:", result.group())
# else:
#     print("No match")

# import re
#
# pattern = r"\d+"  # Matches one or more digits
# text = "There are 123 apples and 456 oranges."
# result = re.findall(pattern, text)
#
# print(result)
#
#
# import re
#
# pattern = r"\d+"  # Matches digits
# text = "The price is 100 dollars."
# result = re.sub(pattern, "XXX", text)
#
# print(result)
#
# import re
#
# pattern = r"\s+"  # Matches one or more spaces
# text = "This  is   a test"
# result = re.split(pattern, text)
#
# print(result)
#
#
# pattern = r"apple"
# text = "apple pie"
# result = re.search(pattern, text)
# print(result.group())
#
#
# . (any character except newline)
# pattern = r"a.b"
# text = "acb"
# result = re.search(pattern, text)
# print(result.group())
#
#
# pattern = r"^Hello"
# text = "Hello world"
# result = re.search(pattern, text)
# print(result.group())
#
#
# pattern = r"world$"
# text = "Hello world"
# result = re.search(pattern, text)
# print(result.group())
#
#
# text = "I have 123 apples and 456 oranges"
#
# print(re.search(r"(\d+.*)", text).group())
#
# print(re.search(r"(\d+.*?)", text).group()
#
#
pattern = r"\."
text = "This is a sentence with a period."
result = re.search(pattern, text)
print(result.group())  # "."

import re

# def validate_email(email):
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
#
# email = "charanbaru@gmail.com"
# print(validate_email(email))  # True
#


# import re
# sample_txt = "The quick brown fox jumps over the lazy dog"
# x = re.search("brown.*jumps",sample_txt)
# if x :
#     print(True)
# else:
#     print(False)

# print(type(x))

#
# import re
# txt = "i am going to buy porsche in next 2 years"
# x = re.search("porsche",txt)
# if x :
#     print(True)
# else:
#     print(False)
#

# import re
#
#
# txt = "i will earn more than 20000000/month"
# x = re.split(r'\s+', txt) # Split by one or more whitespace characters
# print(x)



# import re
#
# txt = "apple123orange456banana789grape"
# x = re.split(r'\d+', txt)  # Split by one or more digits
# print(x)

#

