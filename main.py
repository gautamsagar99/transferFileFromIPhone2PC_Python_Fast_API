from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

app = FastAPI()

# Mount the static files directory to serve the HTML file
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_index():
    # Serve the index.html file
    with open("static/index.html", "r") as f:
        content = f.read()
    return HTMLResponse(content)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file to the server
    with open(file.filename, "wb") as f:
        contents = await file.read()
        f.write(contents)

    return {"filename": file.filename}
