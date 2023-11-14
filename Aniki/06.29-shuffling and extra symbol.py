string1 = "abcd"
string2 = "abc"
def shuffling_and_extra_symbol(string_damaged,string_sended):

    for string in string_sended:
        string_damaged = string_damaged.replace(string, "", 1)
    print(string_damaged)

shuffling_and_extra_symbol(string1, string2)