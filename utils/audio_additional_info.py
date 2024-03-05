import json
import os
from typing import Dict
import parselmouth
from utils.config import cwd, praat_file_path

silence_threshold : int = -25
min_dip_btw_peeks : int =  2
min_pause_duration : float = 0.4
min_sounding_duration : float = 0.1
keep_soundfiles_and_textgrids : str = "no"

def get_audio_information(audio_folder: str, audio_file_name: str) -> Dict:
    """This function calculates the following information from the given audio: 
    * fileBaseName
    * syllableCount
    * pauseCount
    * totalDuration
    * speakingTotalDuration
    * speakingRate
    * articulationRate
    * averageSylableDuration
    * scriptVersion

    Returns:
        Dict: Calculated information in the form of python dictionary. 
    """
    result = parselmouth.praat.run_file(
        praat_file_path, 
        silence_threshold, 
        min_dip_btw_peeks, 
        min_pause_duration, 
        min_sounding_duration, 
        keep_soundfiles_and_textgrids, 
        audio_folder, 
        audio_file_name, 
        capture_output=True
    )
    result_dict = json.loads(result[1])
    return result_dict

if __name__ == "__main__":
    print(get_audio_information(os.path.join(cwd, "AudioFolder"), "output.wav"))