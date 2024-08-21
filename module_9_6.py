"""
module_9_6
"""
def all_variants(text):
    for substring_length in range(1, len(text)+1):
        for shift in range(len(text)):
            substring = text[shift : shift + substring_length]
            if len(substring) < substring_length:
                break
            yield substring


a = all_variants("abc")
for i in a:
    print(i)

b = all_variants("abcde")
for i in b:
    print(i)
