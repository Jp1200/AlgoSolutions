def caesarCipherEncryptor(string, key):
    code = []
    newKey = key % 26
    for char in string:
        code.append(getNewChar(char, newKey))
    return "".join(code)


def getNewChar(letter, key):
    newLetterCode = ord(letter) + key
    print(newLetterCode)
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


caesarCipherEncryptor('dqm', 4)
