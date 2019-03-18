

def raindrops(number):
    output = ''
    for n, char in ((3, 'Pling',),(5,'Plang'),(7,'Plong')):
       if number % n == 0:
        output += char
    
    if output == '':
        return str(number)
    else:
        return output

    
