#merge two dictionaries

dictionary = { "jan":31,"feb":28,"mar":30,"apr":31,"may":30,"jun":31,"jul":30}

print("Before sorting : ")
print(dictionary)
print("After sorting : ")
print("asc ",sorted(dictionary.items()))
print("desc ",sorted(dictionary.items(),reverse=True))