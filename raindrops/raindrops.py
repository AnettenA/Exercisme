def convert(number):
    output = []
    if number % 3 == 0:
        output.append('Pling')
    if number % 5 == 0:
        output.append('Plang')
    if number % 7 == 0:
        output.append('Plong')
    if output == []:
        output = str(number)
    return ''.join(output)