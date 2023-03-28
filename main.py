def to_jaden_case(string):
    string = string.lower()
    string = list(string)
    for i in range(len(string)):
        if string[i] == " ":
            string[i+1] = string[i+1].upper()
        if i == 0:
            string[i] = string[i].upper()
    string = "".join(string)
    print(string)


to_jaden_case("MDeH FTWREGWf h")