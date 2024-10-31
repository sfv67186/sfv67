def single_root_words (root_word, *other_words) :
    same_words = []
    other_words_w = []
    root_word = root_word.lower ()
    for i in range (len (other_words)) :
        other_words_w.append(other_words[i].lower())
        if root_word in other_words [i] :
            same_words.append (other_words [i])
        if other_words [i] in root_word :
            same_words.append(other_words [i])
    print (same_words)


single_root_words ("вод", "Подводный", "переводной", "водинистый", "твёрдый")
single_root_words ( "Сереневенький","рене", "вень", "твёрдый")