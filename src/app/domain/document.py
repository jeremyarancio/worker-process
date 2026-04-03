from dataclasses import dataclass, field
from typing import Annotated, NewType
from uuid import UUID, uuid4


DocumentId = NewType("DocumentId", UUID)


@dataclass
class Document:
    id_: Annotated[DocumentId, field(default_factory=lambda: DocumentId(uuid4()))]
