from pydantic import BaseModel,Field, field_validator

class ChatRequest(BaseModel):
    prompt:str = Field(
        min_length=1,
        max_length=2000
    )

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value):
        if not value.strip():
            raise ValueError("prompt cannot be empty")
        return value