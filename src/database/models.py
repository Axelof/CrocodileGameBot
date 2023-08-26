from asyncio import run
from datetime import datetime

from pydantic import Field, BaseModel as PydanticModel

from database.utils import generate_unique_id
from enums.game import GameDurationEnum


class BaseModel(PydanticModel):
    unique_id: int = Field(default_factory=lambda: run(generate_unique_id()))

    class Meta:
        abstract = True


class CreatedAtMixin(PydanticModel):
    created_at: datetime = Field(default_factory=datetime.now)


class CrossPlatformID(BaseModel, CreatedAtMixin):
    telegram: int | None = None
    vk: int | None = None


class PlayfulStatistics(PydanticModel):
    leading: int = 0
    playing: int = 0


class User(CreatedAtMixin):
    id: int
    statistics: PlayfulStatistics = PlayfulStatistics()

    class Config:
        ignore_extra = True


class Game(CreatedAtMixin):
    participating: list[User] = []
    leader: User | None = None

    @property
    def is_available(self):
        return


class ChatSettings(PydanticModel):
    show_top: bool = True
    game_duration: GameDurationEnum = GameDurationEnum.SMALL


class Chat(CreatedAtMixin):
    id: int
    users: list[User]

    banned: list[User] = []
    settings: ChatSettings = ChatSettings()

    game: Game | None = None
