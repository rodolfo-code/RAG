from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Configurações de servidor
    PORT: int

    # Configurações de banco de dados
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    # Chaves de API
    OPENAI_API_KEY: str
    API_KEY_NVIDEA: Optional[str] = None

    # @property
    # def DATABASE_URL(self) -> str:
    #     """Retorna a URL de conexão com o banco de dados"""
    #     return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # class Config:
    #     env_file = ".env"
    #     case_sensitive = True


def get_settings() -> Settings:
    """
    Retorna uma instância das configurações do sistema.
    
    Returns:
        Settings: Uma instância da classe Settings com as configurações carregadas do arquivo .env
    """
    return Settings()
