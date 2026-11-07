import os
from pathlib import Path

from pydub import AudioSegment
from pydub.playback import play

DRIVE_DIRECTORY = Path.cwd() / "Mundo-01" / "data"

song = AudioSegment.from_mp3(os.path.join(DRIVE_DIRECTORY, "Nocturne_in_B_major_Op_9_no_3.mp3"))
play(song)
