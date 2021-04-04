words = {"носорог":"rhino", "орёл":"eagel","ящерица":"lizard","гепард":"cheetah","олень":"deer","лось":"elk","ёлка":"fir-tree","сосна":"pine-tree","представлять":"to imagine"}
rus_words=dict([[v,k] for k,v in words.items()])
def eng(word):
    find_word = word
    for i in words:
        if i == find_word:
            print(words.get(find_word) or 'No such key')
def rus(word):
    eng_words=dict([[v, k] for k,v in words.items()])
    find_word = word
    for i in eng_words:
        if i == find_word:
            print(eng_words.get(find_word) or 'No such key')
languege_to_translate = input("write the languege to translate words")
if languege_to_translate == "English":
    rus(input("write word to translate"))
else:
    eng(input("write word to translate"))

