import os

cwd : str = os.getcwd()
audio_folder_wd : str = os.path.join(cwd, "AudioFolder")
praat_file_path : str = os.path.join(cwd, r"utils\praat-script-syllable-nuclei-v2file.praat")