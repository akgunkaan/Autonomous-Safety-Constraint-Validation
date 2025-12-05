from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from typing import List

router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"],
)

def process_files(files: List[UploadFile]):
    """
    Placeholder function to simulate file processing.
    In a real implementation, this would trigger the workflow.
    """
    print(f"Processing {len(files)} files...")
    for file in files:
        print(f" - {file.filename}")
    # Here you would call the workflow/ingest.py logic
    print("File processing complete.")


@router.post("/files")
async def upload_files(background_tasks: BackgroundTasks, files: List[UploadFile] = File(...)):
    """
    Upload regulatory documents for processing.
    This endpoint accepts multiple files and processes them in the background.
    """
    background_tasks.add_task(process_files, files)
    return {"message": f"Started processing {len(files)} files in the background."}
