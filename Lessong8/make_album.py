"""
Напишите функцию make_album(), которая создает словарь с описанием музыкального альбома.
Функция должна получать имя исполнителя и название альбома и возвращать словарь, 
содержащий эти два вида информации. Испльзуйте эту функцию для создания двух словарей, 
представляющий разные альбомы. Выведите все возвращаемые значения, чтобы показать,
что информация правильно сохраняеться во всех трех словарях.
"""

def make_album(artist, album, tracks=None):
  album_dict = {
    'artist': artist,
    'album': album,
  }

  if tracks:
    album_dict['tracks'] = tracks

  return album_dict

while True:
  print("\nPlease enter the name of an artist: ")
  name = input()

  print("\nPlease enter the name of an album: ")
  album = input()

  print("\nPlease enter the number of tracks: ")
  tracks = input()

  if tracks == 'q':
    break

  album_dict = make_album(name, album, tracks)
  print(album_dict)