from fastapi import FastAPI, File, UploadFile
import uvicorn

from utils.audio_additional_info import get_audio_information
from utils.convert import convert_bytes_to_file
from utils.config import audio_folder_wd

app = FastAPI()

accepted_file_types = [
    "audio/mpeg",
    "audio/wav"
]

@app.post("/api/audio-info")
async def general_audio_info(audio: UploadFile):

    if audio.content_type not in accepted_file_types:
        return {"error": f"Enter a valid file type. Given type is {audio.content_type}"}
    
    audio_data = await audio.read()
    file_name = convert_bytes_to_file(audio_data, audio.content_type)
    
    if file_name:
        audio_info = get_audio_information(audio_folder_wd, file_name)
        audio_info["actualFileName"] = audio.filename
        return audio_info
    
    return {"error": "Invalid file"}
    