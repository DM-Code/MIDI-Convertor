from mido import Message, MidiFile
import mido
import pygame.midi
import time

from midi_handler import MidiHandler


def start_text():
    line_space()
    print("MIDI Convertor")
    line_space()
    print()


def line_space():
    print("______________________________________________")


if __name__ == '__main__':
    start_text()

    midi_handler = MidiHandler('resources/bach_846.mid')

    playable_tracks = midi_handler.get_playable_midi_tracks()
    print(playable_tracks)
    midi_handler.show_all_midi_tracks()

    # Only play audio from a certain channel

    # pygame.midi.quit()
