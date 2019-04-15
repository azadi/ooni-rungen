# rungen.py: OONI Run link generator.

This script generates an [OONI Run](https://run.ooni.io/) link from a list of URLs which can then be shared with users to test if and how the website is censored, using the OONI Probe.  This is the Python version of the original script that can be found at https://github.com/ooni/run/blob/master/utils/links.js.

## Requirements

Python 3

## Usage

```
usage: rungen.py [-h] [--file input-file | --list LIST [LIST ...]] [--prefix]
                 [--verbose]

Generate an OONI Run link from a list of URLs

optional arguments:
  -h, --help            show this help message and exit
  --file input-file     input file with list of URLs separated by a new line
  --list LIST [LIST ...]
                        enter list of URLs as command line arguments
  --prefix              automatically prefix URLs with https://
  --verbose             show verbose output (enable logging)

```
## Input Formats

The script takes input a file (specified with `--file`) with the list of URLs separated by a new line. You can also pass arguments on the command line as well with the `--list` option.

For passing a file,

```
$ cat tests/four-urls.txt
https://wikipedia.org
https://en.wikipedia.org
https://es.wikipedia.org
https://twitter.com
https://whatsapp.com
```

```
$ python3 rungen.py --file tests/four-urls.txt 
https://run.ooni.io/nettest?tn=web_connectivity&ta=%7B%22urls%22%3A%5B%22https%3A%2F%2Fwikipedia.org%22%2C%22https%3A%2F%2Fen.wikipedia.org%22%2C%22https%3A%2F%2Fes.wikipedia.org%22%2C%22https%3A%2F%2Ftwitter.com%22%2C%22https%3A%2F%2Fwhatsapp.com%22%5D%7D&mv=1.2.0
```

For passing the list through the command line:

```
$ python3 rungen.py --list wikipedia.org en.wikipedia.org
https://run.ooni.io/nettest?tn=web_connectivity&ta=%7B%22urls%22%3A%5B%22wikipedia.org%22%2C%22en.wikipedia.org%22%5D%7D&mv=1.2.0
```

## Prefixing HTTPS

If you pass the `--prefix` argument, the script will prefix `https://` to the URLs. (If the URLs already have `http://` prefixed, they are not modified.)

## Tests

There are currently two simple tests that match the output from the script with the output from https://run.ooni.io/.

```
$ python3 -m unittest discover tests -v
test_foururls (test_rungen.TestRunGen) ... ok
test_twourls (test_rungen.TestRunGen) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

```
