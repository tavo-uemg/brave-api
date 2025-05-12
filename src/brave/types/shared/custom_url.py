from pydantic import BaseModel, HttpUrl, field_validator

class AutoHttpUrl(BaseModel):
    url: HttpUrl

    @field_validator('url', mode='before')
    def prepend_http(cls, v):
        if isinstance(v, str) and not v.startswith('http'):
            return f'https://{v}'
        return v
