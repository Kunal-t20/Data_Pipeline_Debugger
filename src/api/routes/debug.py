from fastapi import APIRouter
from src.api.schemas import (
    DebugTextRequest,
    DebugFileRequest,
    DebugResponse,
)
from src.services.debugger import (
    run_debugger_from_text,
    run_debugger_from_file,
)

router = APIRouter(prefix="/debug", tags=["Debugger"])


@router.post("/text", response_model=DebugResponse)
def debug_from_text(req: DebugTextRequest):
    return run_debugger_from_text(req.log_text)


@router.post("/file", response_model=DebugResponse)
def debug_from_file(req: DebugFileRequest):
    return run_debugger_from_file(req.log_path)
