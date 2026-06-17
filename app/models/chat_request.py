from pydantic import BaseModel,Field, field_validator

class ChatRequest(BaseModel):
    user_id:str = Field(
        min_length=1,
        max_length=10
    )
    prompt:str = Field(
        min_length=1,
        max_length=2000
    )

    @field_validator("prompt","user_id")
    @classmethod
    def validate_prompt(cls, value):
        if not value.strip():
            raise ValueError("user_id or prompt cannot be empty")
        return value