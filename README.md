# I. INTRODUCTION
`ur_audio_sub` made generating captions easy for any audio files &amp; youtube video using OpenAI Whisper. Multiple languages support.

# II. REFERENCES
## 2.1. First thing first
### Install whisper package
You will need to install OpenAI whisper package from source using pip:
Let's runt this command in the terminal fist: `!pip install git+https://github.com/openai/whisper.git -q`

### Install ffmpeg
You also need ffmpeg be installed to start generating captions:
- on Ubuntu or Debian, or Google Colab: `sudo apt update && sudo apt install ffmpeg`
- on MacOS using [Homebrew](https://brew.sh/): `brew install ffmpeg`
- on Windows using [Chocolatey](https://chocolatey.org/): `choco install ffmpeg`
- on Windows using [Scoop](https://scoop.sh/): `scoop install ffmpeg`

### Google Colab is highly recommended
Go to the Google Colab menu: Select `Runtime` > `Change runtime type` and make sure that `GPU` has been chosen. You can run this AI model way faster with GPU on Google Colab than the normal CPU or your personal computer.
![gpu_setting](./src/Google%20Colab%20runtime%20GPU.png)

## 2.2. How to install this package?
- Using pip to installed pre-builded package on Pypip `pip install ur_audio_sub`
- If you want to use the latest pydata_master version instead of the stable one, you can install it from source with the following command:
`pip install git+https://github.com/thinh-vu/ur_audio_sub.git@main`

_(*) You might need to insert a `!` before your command when running terminal commands on Google Colab._

## 2.3. Where can I find the generated caption?
Please find it in the same folder where you store the audio file. On Google Colab, you can find it in the root folder when generating subtitles for Youtube videos.

# III. APENDICES
- This package has been built on top of pytube and OpenAI Whisper:
  - [pytube](https://github.com/pytube/pytube) is a genuine, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.
  - [whisper](https://github.com/openai/whisper): Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.

# IV. 🙋‍♂️ CONTACT INFORMATION
You can contact me at one of my social network profiles:

- 💼 LinkedIn: https://linkedin.com/in/thinh-vu
- :octocat: GitHub: https://github.com/thinh-vu
