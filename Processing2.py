def counter(fname):
    newLines = ''
    with open(fname, 'r') as f:
        for line in f:
            num_spaces = 0
            
            for letter in line:
                if letter != ' ':
                    break
                num_spaces += 1
            print('Number Of Spaces : ', num_spaces)       

            if num_spaces == 3:
                print('E3')
                line = line.replace(' '*3, '\\t')
            elif num_spaces == 4:
                print('E4')
                line = line.replace(' '*4, '\\t')
            elif num_spaces == 7:
                print('E5')
                line = line.replace(' ' *7, '\\t\\t')
            elif num_spaces == 8:
                print('E6')
                line = line.replace(' ' * 8, '\\t\\t')
            #newLines = newLines + '\\n' + line
            line = line + '\\n'
            newLines = newLines + line
    a1 = ''.join(newLines)
    print(a1)
    with open('edited_1.txt', 'w') as f1:
        f1.write(a1)

    

counter('test_1.txt')