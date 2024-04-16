import whisper
import warnings

audio_file = '../audio/audio.wav'
output_file = "../output/transcript.txt"

warnings.simplefilter("ignore")
model = whisper.load_model("tiny.en")

result = model.transcribe(audio=audio_file)

with open(output_file, "w") as outp:
    outp.write(result["text"])
    print(f"Transcript written to {output_file}")
