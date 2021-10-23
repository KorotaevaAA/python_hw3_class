class CountVectorizer:
    # def __init__(self, lowercase=True):
    #     self.lowercase = lowercase

    def create_dict_of_words(self, corpus):
        dict_of_words = {}
        for index, string in enumerate(corpus):
            new_string = ''
            for symbol in string:
                if symbol == ' ':
                    if new_string != '':
                        dict_of_words.setdefault(new_string, [0 for i in range(len(corpus))])
                        dict_of_words[new_string][index] += 1
                        new_string = ''
                else:
                    new_string += symbol.lower()
            if new_string != '':
                dict_of_words.setdefault(new_string, [0 for i in range(len(corpus))])
                dict_of_words[new_string][index] += 1
        return dict_of_words

    def get_feature_names(self, corpus):
        return list(self.create_dict_of_words(corpus))

    def fit_transform(self, corpus):
        list_of_arrays = []
        for i in range(len(corpus)):
            list_of_arrays.append([])
        for word, list_of_cnt in self.create_dict_of_words(corpus).items():
            for index, cnt in enumerate(list_of_cnt):
                list_of_arrays[index].append(cnt)
        return list_of_arrays


if __name__ == '__main__':
    text = ['Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    # text = ['This is the first document', 'This document is the second document',
    #         'And this is the third one', 'Is  IS this the first document']
    vector = CountVectorizer()
    print(vector.get_feature_names(text))
    print(vector.fit_transform(text))
