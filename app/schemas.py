from pydantic import BaseModel
from typing import Optional

class DummyPayload(BaseModel):
    title: str
    description: str