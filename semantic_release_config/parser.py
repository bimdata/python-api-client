"""
BIMData.io commit style parser
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING, Tuple

from pydantic.dataclasses import dataclass

from semantic_release.commit_parser._base import CommitParser, ParserOptions
from semantic_release.commit_parser.token import ParsedCommit, ParseError, ParseResult
from semantic_release.enums import LevelBump
from semantic_release.commit_parser.util import parse_paragraphs

if TYPE_CHECKING:
    from git.objects.commit import Commit

log = logging.getLogger(__name__)


def _logged_parse_error(commit: Commit, error: str) -> ParseError:
    log.debug(error)
    return ParseError(commit, error=error)


@dataclass
class BimdataParserOptions(ParserOptions):
    """Options dataclass for AngularCommitParser"""

    allowed_tags: Tuple[str, ...] = (
        "MAJOR",
        "MINOR",
        "PATCH",
    )
    major_tags: Tuple[str, ...] = ("MAJOR",)
    minor_tags: Tuple[str, ...] = ("MINOR",)
    patch_tags: Tuple[str, ...] = ("PATCH",)
    default_bump_level: LevelBump = LevelBump.NO_RELEASE


class BimdataCommitParser(CommitParser[ParseResult, BimdataParserOptions]):
    """
    BIMData.io parser
    """

    parser_options = BimdataParserOptions

    def __init__(self, options: BimdataParserOptions | None = None) -> None:
        super().__init__(options)
        self.re_parser = re.compile(r"^(?P<type>\w+)?:?\s*(?P<subject>.+)")

    # The problem is the cache likely won't be present in CI environments
    def parse(self, commit: Commit) -> ParseResult:
        """
        Attempt to parse the commit message with a regular expression into a
        ParseResult
        """
        message = str(commit.message)
        subject = message.split("\n")[0]

        parsed = self.re_parser.match(subject)
        if not parsed:
            return _logged_parse_error(
                commit, f"Unable to parse the given commit message: {message}"
            )
        parsed_type = parsed.group("type")

        level_bump = self.options.default_bump_level
        level = "unknown"
        if parsed_type in self.options.major_tags:
            level_bump = LevelBump.MAJOR
            level = "breaking"
        elif parsed_type in self.options.minor_tags:
            level_bump = LevelBump.MINOR
            level = "feature"
        elif parsed_type in self.options.patch_tags:
            level_bump = LevelBump.PATCH
            level = "fix"
        else:
            log.debug(
                f"commit {commit.hexsha} didn't match any tag, use default {level_bump} level_bump"
            )
        log.debug(f"commit {commit.hexsha} introduces a {level_bump} level_bump")

        descriptions = parse_paragraphs(message)

        return ParsedCommit(
            bump=level_bump,
            type=level,
            scope="",
            descriptions=descriptions,
            breaking_descriptions=(
                descriptions[1:] if level_bump is LevelBump.MAJOR else []
            ),
            commit=commit,
        )
