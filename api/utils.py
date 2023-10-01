import moviepy.editor as mp
import speech_recognition as sr
import os


def video_transcription(video_path):
	video = mp.VideoFileClip(video_path)
	audio_file = video.audio
	audio_file.write_audiofile("vid_audio.wav")
	r = sr.Recognizer()
	with sr.AudioFile("vid_audio.wav") as source:
		data = r.record(source)
	text = r.recognize_google(data)
	os.remove('vid_audio.wav')
	return text
