import os
import sys

DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print('DIRECTORY:', DIRECTORY)

def translate(path):
    path = path.split('?', 1)[0].split('#', 1)[0]
    words = [w for w in path.split('/') if w]
    path_joined = os.path.join(DIRECTORY, *words) if words else DIRECTORY
    
    print(f"\nRequest: {path}")
    print(f"  Joined: {path_joined}")
    print(f"  Exists directly: {os.path.exists(path_joined)}")
    print(f"  .html exists: {os.path.isfile(path_joined + '.html')}")

translate('/about')
translate('/departments')
translate('/doctors')
translate('/doctors/')
translate('/doctors/dr-abu-bakar-siddique')
