# import re
# text = "Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth."
# # x = re.search(" it has One moon",text,flags= re.IGNORECASE)
# if x:
#     print(True)
# else:
#     print(False)
import re

# x = re.search("^e.+.$",text,flags=re.IGNORECASE)
# if x:
#     print(True)
# else:
#     print(False)

# x = re.split(r"\s+","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth.",maxsplit=10)
# print(x)


# x= re.split(r"\d+","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth.",maxsplit=10)
# print(x)

# print(re.sub("Earth","planet","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth."))

# print(re.findall("th","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth.",flags=re.IGNORECASE))


# import re
#
# pattern = re.compile(r"\+", flags=re.IGNORECASE)
# matches = pattern.findall("Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth.")
# print(matches)


# import re
# def validate(text):
#     pattern = r"[^a-zA-Z0-9$]"
#     if re.search(pattern, text):
#         return True
#     else:
#         return False
# text = "earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth1."
#
# print(validate(text))
#
# import re
# pattern = r"\."
# text = "earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth1."
# result = re.search(pattern, text)
# print(result.group())



# import re
#
# text = "earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth1."
# print(re.sub("the","is",text))

import re
# text = "127 37 dfywgfyu wyyu3 3 3 3  ygyfgygeg 3 23 33 yg ygyugyugyuga ygfyuwgyug ygyefwuegf gyuefg y yge wgyuyg"
# x = re.split("\d+", text, maxsplit=15)
# print(x)

# import re
# text = "127 37 dfywgfyu wyyu3 3 3 3  ygyfgygeg 3 23 33 yg ygyugyugyuga ygfyuwgyug ygyefwuegf gyuefg y yge wgyuyg"
# x = re.split(r"\s+", text)
# if x:
#     print("First whitespace found at index:", x.start())
# else:
#     print("No whitespace found")
# print(x)

# import re
# text = "hdh dhhd hdhd hdhd hd dhd hd dhd dhdhd hddhdhd hddh dhd dhdhd hdhd dhd dhd dhd"
# x = re.findall("dh","hdh dhhd hdhd hdhd hd dhd hd dhd dhdhd hddhdhd hddh dhd dhdhd hdhd dhd dhd dhd")
# print(x)
#
# import re
# text = "65675675  tr drdrtud drddrfdrdr 56756  ftftff 676767 fttyftftyftf tftftf tftft tftyftf65656 6 tft ftf 65665ftff r57576 "
# x = re.split("\s+",text,maxsplit=10)
# print(x)
#
# import re
# text = "65675675  tr drdrtud drddrfdrdr 56756  ftftff 676767 fttyftftyftf tftftf tftft tftyftf65656 6 tft ftf 65665ftff r57576 "
# x = re.split("\d+",text,maxsplit=10)
# print(x)




# import re
#
# p = re.compile('\w')
# print(p.findall("Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth."))
#
#
# p = re.compile('\w+')
# print(p.findall("Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth."))

# import re
# p = re.compile("\d+")
# print(p.findall("Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth."))

# import re
# p=re.findall("h","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth.")
# print(p)

# import re
# p = re.compile("\s+")
# print(p.findall("Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth."))

# import re
# p = re.search("3rd planet","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth")
# if p :
#     print(True)
# else:
#     print(False)



# import re
# p = re.search("3rd.*only","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth")
# if p :
#     print(True)
# else:
#     print(False)


# import re
# p = re.sub("3rd.*only","abcdefghijklmnopqrstuvwxyz","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth")
# print(p)


# import re
# p = re.search("3rd.*Only","Earth is the 3rd planet from the Sun, and it has one Moon. It is the only planet in our Solar System which is suitable for sustaining life. The composition of the Earth's surface is 70% water and only 30% land. Water bodies such as oceans, rivers, lakes, glaciers and seas make up 70% of the water content on Earth",flags=re.IGNORECASE)
# if p :
#     print(True)
# else:
#     print(False)

#
# import re
# text = """
# Hello there! Welcome to the world of regex.
# Today, we will be learning about patterns.
# Regex helps us extract information from text.
# For example, email addresses can be captured using regex.
# Let's practice with some phone numbers too.
# Emails look like this: test@example.com.
# You can also find dates in formats like 12/25/2023.
# This can include all types of content, like: regex, text, data, or more.
# Once we understand how regex works, we can manipulate texts easily.
# Enjoy working with regular expressions!
# """
#
# emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)
# print("Emails found:", emails)
#
#
# phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
# print("Phone numbers found:", phone_numbers)
#
# r_words = re.findall(r'\br\w+', text, re.IGNORECASE)
# print("Words starting with 'r':", r_words)
#
# replaced_text = re.sub(r'regex', 'REGEX', text, flags=re.IGNORECASE)
# print("\nReplaced text with 'REGEX':\n", replaced_text)
#
#
# lines = re.split(r'\n', text)
# print("\nLines split from text:")
# for line in lines:
#     print(line)
#
#
# dates = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b', text)
# print("\nDates found:", dates)
#
# regex_count = len(re.findall(r'\bregex\b', text, flags=re.IGNORECASE))
# print("\n'Regex' appears", regex_count, "times.")
#
#
# data_match = re.search


