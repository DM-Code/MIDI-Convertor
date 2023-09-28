import pygame.midi
from mido import MidiFile

def stop():
    pygame.midi.quit()

def line_space():
    print("______________________________________________")

class MidiHandler:

    def __init__(self, midi_file_path):
        self.output = None
        self.mid = MidiFile(midi_file_path)

        self.init_midi()

    def init_midi(self):
        pygame.midi.init()
        default_midi_output = pygame.midi.get_default_output_id()
        self.output = pygame.midi.Output(default_midi_output)

    def play(self):
        for message in self.mid.play():
            if message.type == 'note_on':
                note = message.note
                velocity = message.velocity
                self.output.note_on(note, velocity)

                if velocity != 0:
                    print("Note On: {}".format(note))
                else:
                    print("Note Off: {}".format(note))
                    self.output.note_off(note)

            elif message.type == 'note_off':
                self.output.note_off(message.note)
                print("Note Off: {}".format(message.note))

    def play_midi_channel(self, channel):
        for message in self.mid.play():
            if message.channel == channel:
                if message.type == 'note_on':
                    note = message.note
                    velocity = message.velocity
                    midi_time = message.time
                    self.output.note_on(note, velocity)

                    if velocity != 0:
                        print("Note On: {}".format(note))
                    else:
                        print("Note Off: {}".format(note))
                        self.output.note_off(note)

                elif message.type == 'note_off':
                    self.output.note_off(note)
                    print("Note Off: {}".format(note))

    def show_midi_data(self):
        note_channels = []
        for i, track in enumerate(self.mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.is_meta:
                    ...
                if msg.type == "note_on":
                    note_channels.append(i)
                    print("Appended")
                    break

                # print(msg)
            line_space()

    def show_all_midi_tracks(self):
        # Track Names
        # TODO: Have this added to a list over only one for each loop
        for i, track in enumerate(self.mid.tracks):
            print('Track {}: {}'.format(i, track.name))
        line_space()

    def get_playable_midi_tracks(self):
        note_channels = []
        for i, track in enumerate(self.mid.tracks):
            for msg in track:
                if msg.is_meta:
                    ...
                if msg.type == "note_on":
                    note_channels.append(i)
                    break
        return note_channels

    # Channel
    def show_midi_data_channel(self, channel):
        for i, track in enumerate(self.mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.is_meta:
                    ...
                print(msg)
            line_space()

        for msg in self.mid.play():
            ...
            # port.send(msg)

    def get_channel_count(self):
        channel_count = 0
        for i, track in enumerate(self.mid.tracks):
            channel_count += 1

        return channel_count

