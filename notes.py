import fractions


def mod12(n):
  return n % 12


def note_name(number):
  notes = "C C# D D# E F F# G G# A A# B".split()
  return notes[mod12(number)]


def notes_names(notes):
  return [note_name(n) for n in notes]


def accidental_delta(acc):
  if acc == '#':
    return 1
  elif acc == 'b':
    return -1
  else:
    return 0


def accidentals(note_string):
  acc = note_string[1:]
  return sum([accidental_delta(c) for c in acc])


def name_to_number(note_string):
  notes = "C . D . E F . G . A . B".split()
  name = note_string[0:1].upper()
  number = notes.index(name)
  acc = accidentals(note_string)
  return mod12(number + acc)


def note_duration(note_value, unity, tempo):
  return (60.0 * note_value) / (tempo * unity)


def durations(notes_values, unity, tempo):
  return [note_duration(nv, unity, tempo) for nv in notes_values]


def dotted_duration(duration, dots):
  ratio = fractions.Fraction(1, 2)
  return duration * (1 - ratio ** (dots + 1)) / ratio


def music_duration(time_sig, num_measures, tempo_note_reciprocal, tempo_bpm):
  beats, beat_value = time_sig.split('/')
  num_beats_per_measure = int(beats)
  beat_note_duration = 1 / int(beat_value)
  notes = [beat_note_duration] * num_beats_per_measure
  total_seconds = sum(durations(notes, 1 / tempo_note_reciprocal,
                                tempo_bpm)) * num_measures
  print(total_seconds)
  return total_seconds / 60


def interval(x, y):
  return mod12(x - y)


def transposition(notes, index):
  return [mod12(n + index) for n in notes]


def retrograde(notes):
  return list(reversed(notes))


def rotate(item, n=1):
  modn = n % len(item)
  return item[modn:] + item[0:modn]


c_major_scale = [0, 2, 4, 5, 7, 9, 11]

dorian_mode = rotate(c_major_scale)
phrygian_mode = rotate(dorian_mode)
lydian_mode = rotate(phrygian_mode)
mixolydian_mode = rotate(lydian_mode)
