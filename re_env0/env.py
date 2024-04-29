import os
import sys

from enum import StrEnum
from typing_extensions import Annotated, get_type_hints
from rich import print


class Env(StrEnum):
    ENV0_API_KEY = "ENV0_API_KEY"
    ENV0_API_KEY_SECRET = "ENV0_API_KEY_SECRET"
    ENV0_PROJECT_ID = "ENV0_PROJECT_ID"
    ENV0_BASE_URL: Annotated["Env", "https://api.env0.com"] = "ENV0_BASE_URL"

    @classmethod
    def val(cls, name):
        if name not in cls.__members__:
            raise ValueError(f"Unknown environment variable name: {name}")

        return os.environ.get(name, cls.get_optional_value(name))

    @classmethod
    def get_optional_value(cls, n, type_hints=None):
        if type_hints is None:
            type_hints = get_type_hints(cls, include_extras=True)
        try:
            return type_hints[n].__metadata__[0]
        except (IndexError, KeyError) as _:
            return None

    @classmethod
    def check(cls):
        type_hints = get_type_hints(cls, include_extras=True)

        res = True

        for name in cls.__members__:
            if (
                os.environ.get(name) is None
                and cls.get_optional_value(name, type_hints) is None
            ):
                print(
                    f"Environment variable [red]{name}[/red] not set", file=sys.stderr
                )
                res = False

        return res
