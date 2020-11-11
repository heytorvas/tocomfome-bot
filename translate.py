# -*- coding: utf-8 -*-

import translators as ts

# print(ts._deepl.language_map) # 'it', 'pt', 'zh', 'nl', 'de', 'pl', 'es', 'fr', 'ru', 'ja'

class Translate():

    def __init__(self):
        pass

    def get_words_translated(self):
        words = ['tô com fome']
        languages_list = ['it', 'en', 'zh', 'nl', 'de', 'pl', 'es', 'fr', 'ru', 'ja', 'hi']

        words_list = []
        for j in words:
            for i in languages_list:
                words_list.append(ts.google(j, from_language="pt", to_language=i, if_use_cn_host=True))
            words_list.append(j)
        
        return words_list

    def get_words_list(self):
        separator = ' OR '
        string = separator.join(self.get_words_translated())
        return string

    def write_txt_file(self):
        with open("words.txt","w") as f:
            words = self.get_words_translated()
            for i in range(len(words)):
                if words[i] == words[-1]:
                    f.write(words[i])
                else:
                    f.write("{}\n".format(words[i]))
            f.close()

