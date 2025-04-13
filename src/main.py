import uvicorn
from api.app import app
import logging

from config import get_settings

settings = get_settings()

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    port = settings.PORT
    logger.info(f"Iniciando aplicação na porta {port}...")
    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        port=port,
        reload=True
    ) 