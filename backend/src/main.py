from fastapi import  FastAPI, File, UploadFile,Form
import uvicorn
from extractor import  extract
import uuid
import  os

maahi = FastAPI()

@maahi.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),  #It is similar to None(...)
        file: UploadFile = File(...),
):
    content = file.file.read()
    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"
    with open(file_path, "wb") as f:
        f.write(content)
    try:
        data = extract(file_path,file_format)
    except Exception as e:
        data = {
            "error": str(e)
        }
    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == "__main__":
    uvicorn.run(maahi, host="127.0.0.1", port=8080)
