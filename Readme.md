# Pattern-create - a based pattern_create/pattern_offset metasploit tool in Python

A python implementation of the tool pattern_create/pattern_offset that comes with metasploit framework

## Usage

```
$ ./pattern-create.py
usage: pattern [-c length | offset [subpattern length]]

optional arguments:
  -h, --help            show this help message and exit
  -c CREATE, --create CREATE
                        Create a pattern with the given length
  -o OFFSET [OFFSET ...], --offset OFFSET [OFFSET ...]
                        Find the offset of the given subpattern
```

To create a 1024 byte pattern run:

```
$ ./pattern-create.py -c 1024
Aa0Aa1Aa2...7Bh8Bh9Bi0B
```

To find an offset in the buffer, for example Jv1Jv, run:

```
$ ./pattern-create.py -o Jv1Jv
7653
```

You can also
look for memory values. The values need to be little-endian and prefixed
with 0x (supports both 32 and 64 bit numbers):

```
$ ./pattern-create.py -o 0x39684238
1016
```

```
$ ./pattern-create.py -o 0x4230694239684238
1016
```

By default, the offset mode searches through a 8192 byte pattern.
If you want a larger pattern, append the pattern length:

```
$ ./pattern offset 9Mc0
Not found
$ ./pattern offset 9Mc0 10000
9419
```
