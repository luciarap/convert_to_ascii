import unicodedata


if __name__ == '__main__':

    with open("slovak_dict_ascii.txt", 'w') as output:
        sk_dict = open("sk.dic", "r", encoding='utf8')
        f_lines = sk_dict.readlines()
        for line in f_lines:
            line_normalized = line.lower().replace(" ", "")
            output.write(''.join(
                (c for c in unicodedata.normalize('NFD', line_normalized) if unicodedata.category(c) != 'Mn')))

    output.close()
    sk_dict.close()
