import translators as ts

# print(ts._deepl.language_map) # 'it', 'pt', 'zh', 'nl', 'de', 'pl', 'es', 'fr', 'ru', 'ja'

class Translate():

    def __init__(self):
        pass

    def get_words_translated(self):
        words = ['fome', 'faminto']
        languages_list = ['it', 'en', 'zh', 'nl', 'de', 'pl', 'es', 'fr', 'ru', 'ja']

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

    def read_txt_file(self):
        txt_list = ''
        with open("words.txt","r") as f:
            txt_list = f.readlines()
            f.close()
        
        words_list = []
        for i in txt_list:
            words_list.append(i.replace('\n', ''))

        return words_list


# t = Translate()
# t.read_txt_file()
# t.write_txt_file()