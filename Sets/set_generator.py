"""
Using the set generator, select unique file names with a .png extension from the files list, regardless of name
case and extensions. Display file names along with extension, all on one line, in lower case, in alphabetical
order separated by spaces.
"""

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']

print(*sorted({i.lower() for i in files if i.lower().endswith(".png")}))

# output
# board.png png.png python.png stepik.png