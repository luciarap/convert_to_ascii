import unicodedata


# removes special characters from .dic file
# see example file
def dic_file_ascii(outputfile, inputfile):
    with open(outputfile, 'w') as output:
        sk_dict = open(inputfile, "r", encoding='utf8')
        f_lines = sk_dict.readlines()
        for line in f_lines:
            line_normalized = line.lower().replace(" ", "")
            output.write(''.join(
                (c for c in unicodedata.normalize('NFD', line_normalized) if unicodedata.category(c) != 'Mn')))

    output.close()
    sk_dict.close()


# used to extract the first word (adjective) and removes special characters
# see example file
def first_adjective_ascii(outputfile, inputfile):
    prid_mena = []
    with open(inputfile, 'r', encoding='utf8') as f:
        for line in f:
            prid_mena.append(line.split(None, 1)[0])
    with open(outputfile, 'w') as output:
        for p in prid_mena:
            p_low = p.lower()
            output.write(''.join(
                (c for c in unicodedata.normalize('NFD', p_low) if unicodedata.category(c) != 'Mn')))
            output.write("\n")

    f.close()
    output.close()


if __name__ == '__main__':
    dic_file_ascii("sk_dic_outputfile_example.txt", "sk_dic_inputfile_example.dic")
    first_adjective_ascii("adjectives_outfile_example.txt", "adjectives_inputfile_example.txt")
    print("---")

