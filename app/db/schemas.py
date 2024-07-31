from typing import Optional
from pydantic import BaseModel


class HelloWorldBase(BaseModel):
    text: Optional[str] = " "


class HelloWorldInput(HelloWorldBase):
    pass


class HelloWorldOutput(HelloWorldBase):
    pass
