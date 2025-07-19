from pydantic import BaseModel, Field
from typing import List


class NEXTAIBaseModel(BaseModel):
    response: str = Field(..., description="Generate content based on the input & Instructions provided.")