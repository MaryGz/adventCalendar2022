directories = {
    'x' : {
        'a' : 'dir',
        'b.txt' : 14,
        'c.dat' : 85,
        'd' : 'dir'
    }
}

directories['a'] = {
    'e' : 'dir', 
    'f' : 2911, 
    'g' : 255, 
    'h' : 629
    }

directories['x']['a'] = directories['a']


print(directories)

with open("test.txt", 'r') as f:
    for line in f:
        if line[0:4] == "$ cd":
            print(line)