from TTS.api import TTS

# single
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
# tts.tts_to_file(text="How can a clam cram in a clean cream can?", file_path='./outputs/tacotron2-DDC.wav')

# multilingual
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
speaker = "Royston Min"
language = "ko"
text = "간장 공장 공장장은 장 공장장이고 된장 공장 공장장은 강 공장장이다."

numbering = "a"

model_array = model_name.split('/')
model_length = len(model_array)
model_name_only = model_array[model_length - 1] 

speaker_name = speaker.replace(" ", "-")

file_name = "tts_" + model_name_only + "_" + language + "_" + speaker_name + "_" + str(numbering) + ".wav"
file_path = './outputs/' + file_name

tts = TTS(model_name=model_name)
tts.tts_to_file(speaker=speaker, language=language, text=text, file_path=file_path)

