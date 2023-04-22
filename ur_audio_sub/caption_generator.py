# I. Transcribe Youtube Videos
import os
import pandas as pd
import pytube
from pytube import YouTube
import whisper
from ur_gadget import *
import shutil

# Generate subtitle for a youtube video
def ytSub(link, model='medium', language='', translate=False, target_path='', extensions = ['.json', '.txt', '.srt', '.vtt', '.tsv'], basepath=ROOT_DIR):
  """
  Generate caption for any specific Youtube video.
  Args:
      link (:obj:`str`, required): Input the target Youtube video link "https://www.youtube.com/watch?v=21j_OCNLuYg&t=88s&ab_channel=TEDxTalks"
  """
  get_yt(link)
  path = newest_file(basepath)
  subGen_path(path, model=model, language=language, translate=translate, target_path=target_path, extensions=extensions)
  return 'Job finished for :' + path

# Generate subtitle for a local file
def subGen_path(file_path, target_path='', model='medium', language='', translate=False, extensions = ['.json', '.txt', '.srt', '.vtt', '.tsv']):
  """
  Input audio file path to generate the text caption 
  Args:
      file_path (str): Path to the audio file.
      target_path (str, optional): Path to the target folder. If this parameter is skipped, the target folder will be set as the working directory. Defaults to '' .
      model (str, optional): Choose 1 of 3 options: 'base', 'medium', 'large'. Default value = 'medium'.
      language (str, optional): Target language of the audio file to be generated caption. Auto detects language by default. Defaults to ''.
      translate (bool, optional): Translate caption to English. No translation by default. Defaults to False.
      extensions (List[str], optional): List of file extensions to move to the target folder. Defaults to ['.json', '.txt', '.srt', '.vtt', '.tsv'].
  """

  if language == '':
    if translate == False:
      os.system('whisper "{}" --model {}'.format(file_path, model))
    else:
      os.system('whisper "{}" --model {} --task translate'.format(file_path, model))
  else:
    if translate == False:
      os.system('whisper "{}" --model {} --language {}'.format(file_path, model, language))
    else:
      os.system('whisper "{}" --model {} --language {} --task translate'.format(file_path, model, language))
  print('Finish transcripting')
  
  # move subtitles to the target folder
  if target_path == '':
    pass
  else:
    if not os.path.exists(target_path): # Create the new folder if it does not exist
      os.makedirs(target_path)
    files = os.listdir(ROOT_DIR) # files listing
    for file in files:
      ext = os.path.splitext(file)[1]
      if ext in extensions: # Check if the file extension is in the list of extensions to move):
        shutil.move(ROOT_DIR + LMT + file, target_path) # Move the file to a specific folder
      else:
        pass
  print(f'You can find your transcription at: {target_path}')


# def subGen_path(file_path, model='medium', language='', translate=False):
#   """
#   Input audio file path to generate the text caption 
#   Args:
#       file_path (:obj:`str`, required): Eg: "/content/sample_recording.mp3"
#       model (:obj:`str`, optional): choose 1 of 3 options: 'base', 'medium', 'large'. Default value = 'medium'
#       language (:obj:`str`, optional): Target language of the audio file to be generated caption. Auto detects language by default.
#       translate (:obj:`str`, optional): Translate caption to English. No translation by default.
#   """
#   if language == '':
#     if translate == False:
#       os.system('whisper "{}" --model {}'.format(file_path, model))
#     else:
#       os.system('whisper "{}" --model {} --task translate'.format(file_path, model))
#   else:
#     if translate == False:
#       os.system('whisper "{}" --model {} --language {}'.format(file_path, model, language))
#     else:
#       os.system('whisper "{}" --model {} --language {} --task translate'.format(file_path, model, language))

def subGen_order(model='medium', lmt=LMT, basepath=ROOT_DIR):
  """Input a number corresponding to the audio file to the prompt to start generating a caption"""
  files_list = file_ls()
  print(pd.Series(files_list))
  no_input = input('Input the number corresponding to the target file: ')
  file = lmt.join([basepath, files_list[int(no_input)]])
  print('Generating caption for: ' + files_list[int(no_input)])
  os.system('whisper "{}" --model {}'.format(file, model))

def get_yt (link):
  """Download youtube video from its link"""
  yt = YouTube(link) # get Youtube video info
  yt.streams.filter(only_audio=True)[0]\
          .download(output_path='') # save audio file to current directory



