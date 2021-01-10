from os import listdir
from os.path import isfile, join

funny_songs = [x for x in listdir(r"C:\Users\pawci\Desktop\MyAlexa\funny songs")
               if isfile(join(r"C:\Users\pawci\Desktop\MyAlexa\funny songs", x))]

print(funny_songs)