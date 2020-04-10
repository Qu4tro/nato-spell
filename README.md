# nato-spell

**nato-spell** is a Python package that can be used to spell a string / file with the well-known NATO phonetic alphabet.

## Installation

System requirements:
  - **aplay** (ALSA command line player - it may already be installed on your computer)
  - **python >= 3**


Use [pip](https://pip.pypa.io/en/stable/) or pipx to install `homiectl`.

```bash
pip install nato-spell
```

## Usage

Minimal example
```
nato-spell SPELLME 
```

Spelling from stdin
```
echo SPELLME | nato-spell - 
```

Increase the delay between characters (unit is seconds, default is 0)
```
nato-spell SPELLME --char-delay=1
```

Use a different sound directory
```
nato-spell SPELLME --sound-dir=/home/me/my-sound-dir
```

And finally, an example, where we use them all together.
```
echo SPELLME | nato-spell - --sound-dir=/home/me/my-sound-dir --char-delay=1
```

## Sound assets 

These sounds were published by Tim Kahn and hosted on freesound.org
 - Tim Kahn ( https://freesound.org/people/tim.kahn/ )

Thank you Amy Gedgaudas and Tim Kahn for all these sounds.

They're licensed under:
http://creativecommons.org/licenses/by/3.0/


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
