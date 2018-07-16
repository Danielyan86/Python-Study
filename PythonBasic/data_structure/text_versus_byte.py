s = 'cafe'
print(len(s))
b = s.encode('utf8')  # (the code point for “é” is encoded as two bytes in UTF-8
print(len(b), b)

print("=" * 60)
cafe = bytes('café', encoding='utf_8')
print(len(cafe), cafe)
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])
