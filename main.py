import os
import pathlib
from pocketsphinx import LiveSpeech, get_model_path
from whisper_mic.cli import main

def detect_wake_word():
    current_path = pathlib.Path(__file__)
    current_dir = current_path.parent
    model_path = get_model_path()
    hmm_path = os.path.join(model_path, 'en-us/en-us')
    dict_path = os.path.join(model_path, 'en-us/cmudict-en-us.dict')

    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=hmm_path,
        lm=False,
        dict=dict_path,
        keyphrase='hey jarvis',
        kws_threshold=1e-20,
        # kws=f'{current_dir}/keywords.txt'
    )

    for phrase in speech:
        for segment in phrase.seg():
            print(segment.word)
            if segment.word.lower() == "hey jarvis":
                print("Wake word detected! Starting transcription...")
                return True

def speech_wake_up():
    print("Listening for wake word...")
    if detect_wake_word():
        main()

if __name__ == "__main__":
    speech_wake_up()
