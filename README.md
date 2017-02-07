# srt2raw.py

Convert subtitle file (utf-8) to raw text.

## Installation

    $ wget https://raw.githubusercontent.com/eeve/srt2raw.py/master/srt2raw.py

## Usage

```bash
$ ./srt2raw.py -f ./test/Westworld\ S01E10.srt -o ./test/dist -e .md -l -t
```

## Options
```bash
$ srt2raw.py -h

  Usage: srt2raw.py [options]

  Options:

    -h, --help           output usage information
    -V, --version        output the version number
    -f, --file <path>    *set srt file path
    -o, --output <path>  set output file path
    -l, --linenumber     show line number
    -t, --timeline       show timeline
    -e, --extname <extname>  set output file extname

  Examples:

    $ srt2raw.py -f /path/to/file.srt -o /path/to/dist/filename -l -t
    $ srt2raw.py -f /path/to/file.srt -l -t
```

## License

[MIT](./LICENSE.md)

## Node.js
Please upgrade to [srt2raw for Node.js](https://github.com/eeve/srt2raw)
