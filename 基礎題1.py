# -*- coding: utf-8 -*-

def reverse_sentence(sentence):
    s_l = len(sentence)
    result = ""
    for i in range(s_l):
        result += sentence[s_l-1-i]

    return result

def reverse_words(sentence):
    # 先斷句
    words = sentence.split(" ")
    # 再反轉每個單字
    result = ""
    for word in words:
        w_l = len(word)
        for i in range(w_l):
            result += word[w_l-1-i]
        result += " "

    return result[:-1]

if __name__ == '__main__':
    the_sentence_1 = "junyiacademy"
    print("「反轉整個句子」")
    print("原本的句子： %s" % the_sentence_1)
    print("反轉過後　； %s" % reverse_sentence(the_sentence_1))
    print("")

    the_sentence_2 = "flipped class room is important"
    print("「反轉句子中的每個單字」")
    print("原本的句子： %s" % the_sentence_2)
    print("反轉過後　； %s" % reverse_words(the_sentence_2))