import os
import subprocess
import pathlib
# import gtts
# import vlc
import playsound
import webbrowser
import openai
from gtts.cli import tts_cli
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
        keyphrase='hey test',
        kws_threshold=1e-20,
        # kws=f'{current_dir}/keywords.txt'
    )

    for phrase in speech:
        for segment in phrase.seg():
            print(segment.word)
            if segment.word.lower() == "hey test":
                print("Wake word detected! Starting transcription...")
                return True

def text_to_speech():
    # subprocess.run(["gtts-cli", "--file", "transcribed_text.txt", "output", "answer.mp3"])
    subprocess.run(["gtts-cli", "--file", "transcribed_text.txt", "--output", "answer.mp3"])

def speech_wake_up():
    print("Listening for wake word...")
    if detect_wake_word():
        playsound.playsound("yes.mp3")
        subprocess.run(["whisper_mic", "--save_file", "--model", "small"])

if __name__ == "__main__":
    webbrowser.open('https://play.hbomax.com/page/urn:hbo:page:GXdXk0ge49KXCPQEAAB6D:type:episode', new=2)
    # speech_wake_up()
    # text_to_speech()
    # playsound.playsound("answer.mp3")
    # subprocess.run(["whisper_mic", "--save_file", "--model", "small"])

    # client = openai.OpenAI()
    # completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "user", "content": "say something"}
    #     ]
    # )
    # print(completion.choices[0].message)