#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import time
from pathlib import Path
from typing import NamedTuple

DEFAULT_SOUND_DIRECTORY = Path(__file__).resolve().parent / "sounds"


class Speller(NamedTuple):
    string: str
    char_delay: float = 0.3
    sound_dir: Path = DEFAULT_SOUND_DIRECTORY

    @property
    def files(self):
        return self.file_sequence(self.string)

    def play(self):
        for sounds in self.char_sounds:
            for file in sounds:
                self.play_file(file)
            time.sleep(self.char_delay)

    @property
    def char_sounds(self):
        return [self.char_to_files(char) for char in self.string]

    def char_to_files(self, char: str):
        if not char.isalnum():
            raise ValueError("Character is not an alphanumeric character")

        files = []
        if char.isupper():
            capital = self.sound_dir / "capital.wav"
            files.append(capital)

        char_file = self.sound_dir / f"{char.lower()}.wav"
        files.append(char_file)
        return files

    @staticmethod
    def play_file(filepath):
        os.system(f"aplay {filepath}")

    @staticmethod
    def arg_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "infile",
            nargs="?",
            type=argparse.FileType("r"),
            default=sys.stdin,
            help="Text to be spelled",
        )
        parser.add_argument("instring", type=str, help="Text to be spelled")
        parser.add_argument(
            "-d1",
            "--char-delay",
            type=float,
            help="Tinker with the delay between character",
        )
        parser.add_argument(
            "--sound-dir",
            type=lambda p: Path(p).absolute(),
            default=DEFAULT_SOUND_DIRECTORY,
            help="Path to the sound directory",
        )
        return parser

    @classmethod
    def from_args(cls, args: dict):
        kwargs = {}

        if args.instring == "-":
            kwargs["string"] = args.infile.read().strip()
        else:
            kwargs["string"] = args.instring

        if "char_delay" in args and args.char_delay:
            kwargs["char_delay"] = args.char_delay

        if "sound_dir" in args and args.sound_dir:
            kwargs["sound_dir"] = args.sound_dir

        return cls(**kwargs)


def main():
    args = Speller.arg_parser().parse_args()
    speller = Speller.from_args(args)
    speller.play()


if __name__ == "__main__":
    main()
