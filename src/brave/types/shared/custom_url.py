from pydantic import AfterValidator
from typing import Annotated

AutoHttpUrl = Annotated[
    str,
    AfterValidator(lambda v: f"https://{v}" if not v.startswith("http") else v)
]
