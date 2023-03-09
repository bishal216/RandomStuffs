# LZW compression
def compress(data):
    dictionary = {chr(i) : i for i in range(256)}
    pattern = ""
    output = []
    for char in data:
        if pattern + char in dictionary:
            pattern = pattern + char
        else:
            output.append(dictionary[pattern])
            dictionary[pattern + char] = len(dictionary)
            pattern = char      
    output.append(dictionary[pattern])
    return output
def decompress(data):
    dictionary = {i : chr(i) for i in range(256)}
    current = data[0]
    output = dictionary[current]
    for i,code in enumerate(data[1:]):
        if code in dictionary:
            temp = dictionary[code]
        else:
            temp = dictionary[current] + dictionary[current][0]
        output += temp
        # print(output)
        dictionary[len(dictionary)] = dictionary[current] + temp[0]
        current = code
    return output
def LZW(input) :
    print('The input string is '+ input +' with length ' + str(len(input)))
    encoded = compress(input)
    print('The encoded stream is '+ str(encoded)+' with length ' + str(len(encoded)))
    decoded = decompress(encoded)
    print('The decoded stream is '+ str(decoded))
def main():
    LZW('This string has no repeated pattern.')
    LZW('sadsadsadsad')
    
    
if __name__ == '__main__':
    main()