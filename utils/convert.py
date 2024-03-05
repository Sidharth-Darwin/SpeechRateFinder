from utils.config import audio_folder_wd, os

def convert_bytes_to_file(file_byte_obj : bytes, file_type : str) -> str:
    if file_type == "audio/mpeg":
        file_name = "input_audio.mp3"
    elif file_type == "audio/wav":
        file_name = "input_audio.wav"
    else:
        return None
    with open(os.path.join(audio_folder_wd, file_name), "bw") as f:
        f.write(file_byte_obj)
        print("File created",f)
    return file_name
    