# List Known Hosts `lkh`

Small utility script to read, parse, and display host names from the `~/.ssh/known_hosts` file.

## Install

```
$ git clone https://github.com/tstringer/lkh.git
$ cd lkh
$ pip3 install .
```

## Usage

```
$ lkh
```

Or to narrow the output...

```
$ lkh | grep pattern
```

