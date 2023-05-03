# LZW compression
def compress(data):
    dictionary = {chr(i) : i for i in range(256)}
    pattern = ""
    output = []
    for char in data:
        # print(pattern)
        if pattern + char in dictionary:
            pattern = pattern + char
            # print('if exists : '+pattern)
        else:
            output.append(dictionary[pattern])
            # print('Append'+str(output))
            dictionary[pattern + char] = len(dictionary)
            # print('if not : ' + pattern + char)
            pattern = char      
    output.append(dictionary[pattern])
    return output
def decompress(data):
    dictionary = {i : chr(i) for i in range(256)}
    current = data[0]
    output = dictionary[current]
    for i,code in enumerate(data[1:]):
        # print(output)
        print('For'+str(code))
        if code in dictionary:
            temp = dictionary[code]
            print('If in dict : ' + temp)
        else:
            temp = dictionary[current] + dictionary[current][0]
            print('If not dict : ' + temp)
        output += temp
        print(output)
        dictionary[len(dictionary)] = dictionary[current] + temp[0]
        print('Append ('+str(dictionary[current])+'): '+dictionary[current] + temp[0])
        current = code
    # print(dictionary)
    return output
def LZW(input) :
    print('The input string is '+ input +' with length ' + str(len(input)))
    encoded = compress(input)
    print('The encoded stream is '+ str(encoded)+' with length ' + str(len(encoded)))
    decoded = decompress(encoded)
    print('The decoded stream is '+ str(decoded))
def main():
    # LZW('This string has no repeated pattern.')
    # LZW('sadsadsadsad')
    LZW('hellohellohello')
    
    
    
if __name__ == '__main__':
    main()