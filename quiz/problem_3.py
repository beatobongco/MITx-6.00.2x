songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7),
         ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]


def song_playlist(songs, max_size):
  """
  songs: list of tuples, ('song_name', song_len, song_size)
  max_size: float, maximum size of total songs that you can fit

  Start with the song first in the 'songs' list, then pick the next
  song to be the one with the lowest file size not already picked, repeat

  Returns: a list of a subset of songs fitting in 'max_size' in the order
           in which they were chosen.
  """
  r = []

  if songs[0][2] > max_size:
    return r

  current_size = 0
  _songs = songs.copy()

  # Deal with first candidate
  first = _songs.pop(0)
  r.append(first[0])
  current_size += first[2]

  # Sort remaining
  _songs.sort(key=lambda x: x[2])
  while True:
    try:
      candidate = _songs.pop(0)
    except IndexError:
      return r

    if candidate[2] + current_size > max_size:
      return r

    r.append(candidate[0])
    current_size += candidate[2]


assert song_playlist(songs, 12.2) == ['Roar', 'Wannabe', 'Timber']
assert song_playlist(songs, 11) == ['Roar', 'Wannabe']
assert song_playlist(songs, 3) == []
