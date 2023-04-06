#convert "Don't panic!" to "on tap" //
phrase = "Don't panic!"
plist = list(phrase)
print(plist)
print(phrase)
new_phrase = ''.join(plist[1:3])
print(new_phrase)
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(new_phrase)
