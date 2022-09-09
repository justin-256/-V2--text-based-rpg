from components.object import *
from components.container import *

data = {
    "otherthing": Object(
        name = "otherthing",
        synonyms = ["other thing"],
        description = "a really big thing"
    ),
    "thing": Object(
        name = "thing",
        synonyms = ["thiinggg"],
        description = "a thing"
    ),
    "bench": Object(
        name = "bench",
        synonyms = ["seat"],
        description = "There is a bench here."
    ), 
    "box": Container(
        name = "box",
        synonyms = ["cardboard box"],
        description = "A cardboard box lays on the lawn.",
        contents = ["thing", "otherthing"]
    )
}

