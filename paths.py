import os

print('\n-----------os-----------')
print('1-whole directory')
print(os.path.abspath(__file__))

print('\n2-base directory')
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

print('\n3-file name with extension')
print(os.path.basename(__file__))


print('\n-----------pathlib-----------')

from pathlib import Path, PurePath

print('1-whole directory')
print(type(Path(__file__).absolute()))

print('\n2-base directory')
print(Path(__file__).parent.absolute())
print(Path.cwd())

print('\n3-file name with extension')
print(PurePath(__file__))

print('\n4-file name without extension')
print(Path(__file__).stem)

print('\n5-home directory')
print(Path.home())
