from dataclasses import dataclass
from decouple import config
import os


@dataclass
class Telegram:
    token: str


@dataclass
class Config:
    telegram: Telegram


def load_config():
    return Config(
        telegram=Telegram(
            token=config("BOT_TOKEN", cast=str),
        ),
    )
