from pydantic import BaseModel
from typing import List


class DebugTextRequest(BaseModel):
    log_text: str


class DebugFileRequest(BaseModel):
    log_path: str


class DebugResponse(BaseModel):
    category: str
    confidence: float
    stage: str
    root_cause: str
    fixes: List[str]
