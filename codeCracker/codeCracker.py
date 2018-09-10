def decrypt(my_dict, message):
    default_char = '?'
    response = ''
    if message is None:
        return '' 
    else :
        for x in list(message):
            response += my_dict.get(x, default_char)
    return response

if __name__=="__main__":
    my_dict = {'a' : '!', 'b' : '"'}        
    print(decrypt(my_dict, "ab7"));
