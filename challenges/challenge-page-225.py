import sys

fileName = input('Enter a name for your file: ')

try:
    file = open(str(fileName)+'.html', 'x')
except FileExistsError:
    print('\nFile already exists. Exiting...\n')
    sys.exit()

print(type(file))
file.write('<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t</head>\n\t<body>\n\t\t<p>Stay tuned for our amazing summer sale!</p>\n\t</body>\n</html>')
file.close()
