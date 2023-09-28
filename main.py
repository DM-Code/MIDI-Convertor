from mido import Message, MidiFile
import mido
import pygame.midi
import time

def print_hi(name):
    print(f'Hi, {name}')

def line_space():
    print("______________________________________________")

if __name__ == '__main__':
    print_hi('PyCharm')

    pygame.midi.init()
    mid = MidiFile('resources/bach_846.mid')

    default_midi_output = pygame.midi.get_default_output_id()

    # Selects the default output device
    output = pygame.midi.Output(default_midi_output)

    for message in mid.play():
        if message.type == 'note_on':
            note = message.note
            velocity = message.velocity
            time = message.time
            output.note_on(note, velocity)

            if(velocity != 0):
                print("Note On: {}".format(note))
            else:
                print("Note Off: {}".format(note))

        elif message.type == 'note_off':
            output.note_off(note)
            print("Note Off: {}".format(note))

    # Track Names
    # TODO: Have this added to a list over only one for each loop
    # for i, track in enumerate(mid.tracks):
    #     print('Track {}: {}'.format(i, track.name))
    # line_space()
    #
    # for i, track in enumerate(mid.tracks):
    #     print('Track {}: {}'.format(i, track.name))
    #     for msg in track:
    #         if msg.is_meta:
    #             ...
    #         print(msg)
    #     line_space()
    #
    # for msg in mid.play():
    #     ...
    #     # port.send(msg)
    #


    pygame.midi.quit()

