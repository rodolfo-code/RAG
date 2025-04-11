from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Union, Any
from uuid import UUID, uuid4

class Document:
    """
    Entidade que representa um documento completo no sistema.
    """	
    id: Optional[int] = None
    name: str = ""
    file_type: str = ""
    content: bytes = field(default_factory=bytes)
    upload_date: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    
