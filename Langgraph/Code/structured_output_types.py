from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

## With the mentioned Schema
class Country(BaseModel):
    """Information about a country"""
    name : str = Field(description="name of the country")
    language : str = Field(description="language of the country")
    capital : str = Field(description="Capital of the country")


structured_llm = llm.with_structured_output(Country)
structured_llm
structured_llm.invoke("Tell me about France")

-----------------------------------------------------------------------------------
# Without rule of any predefined format (Schema)

from typing_extensions import Annotated,TypedDict
from typing import Optional

#TypedDict
class Joke(TypedDict):
    """Joke to tell user"""

    setup: Annotated[str,...,"The setup of the joke"]

    punchline: Annotated[str,...,"The punchline of the joke"]
    rating : Annotated[Optional[int],None,"How funny the joke is,from 1 to 10"]

structured_llm=llm.with_structured_output(Joke)
structured_llm.invoke("Tell me a joke about cats")

---------------------------------------------------------------------------------------------
json_schema = {
    "title": "joke",
    "description": "Joke to tell user.",
    "type": "object",
    "properties": {
        "setup": {
            "type": "string",
            "description": "The setup of the joke",
        },
        "punchline": {
            "type": "string",
            "description": "The punchline to the joke",
        },
        "rating": {
            "type": "integer",
            "description": "How funny the joke is, from 1 to 10",
            "default": None,
        },
    },
    "required": ["setup", "punchline"],
}
structured_llm = llm.with_structured_output(json_schema)

structured_llm.invoke("Tell me a joke about cats")
