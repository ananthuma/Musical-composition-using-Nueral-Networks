import pysynth
song = (
                       ('c', 4),
  ('d#', 4), ('f', 4), ('g', 4),
  ('a#', 4), ('c5', 4),('c5', 4),('a#', 4),('a', 4),('g', 4),('f', 4),('d#', 4),('d', 4),('c', 4)
   
)
pysynth.make_wav(song, bpm = 250,  fn = "test.wav")
