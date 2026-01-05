# nato-spell

**nato-spell** is a Python package that spells text using the NATO phonetic alphabet.

## Installation

System requirements:
- **aplay** (ALSA command line player - likely already installed on Linux)
- **Python >= 3.9**

### From PyPI

```bash
pip install nato-spell
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv tool install nato-spell
```

### From AUR (Arch Linux)

```bash
yay -S nato-spell-git
```

## Usage

Spell a string:
```bash
nato-spell HELLO
```

Spell from stdin:
```bash
echo SECRET | nato-spell -
```

Adjust delay between characters (seconds):
```bash
nato-spell HELLO --char-delay=0.5
```

Use custom sounds:
```bash
nato-spell HELLO --sound-dir=/path/to/sounds
```

## Sound Credits

Sounds by Tim Kahn, hosted on freesound.org:
- https://freesound.org/people/tim.kahn/

Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## License

[MIT](LICENSE)
