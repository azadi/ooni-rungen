#! /usr/bin/env python3

"""Generate an OONI Run link from a list of URLs.

This script generates an OONI Run link from a list of URLs that can be shared
with users to test if and how the website is censored using the OONI Probe.
This is the Python version of the original script that can be found at
https://github.com/ooni/run/blob/master/utils/links.js.
"""

import sys
import json
import logging
import argparse
import urllib.parse

BASE_URL = 'https://run.ooni.io'
MIN_VER = '1.2.0'
TEST_NAME = "web_connectivity"
OUTPUT_LIST = "{0}/nettest?tn={1}&ta={2}&mv={3}"


def rungen_urls(args):
    logging.debug(args)

    # Read the URLs from either the --file or the --list.
    urls = []
    if args.file:
        try:
            with open(args.file, "r") as f:
                for line in f:
                    urls.extend(line.split())
        except IOError as e:
            sys.exit("Error opening file: {0}".format(e))
        if not urls:
            sys.exit("No lines found in file {0}.".format(args.file))
    if args.list:
        urls = args.list[:]

    # Prefix URLs with https:// if the --prefix argument was passed.
    # Note that if the URL was http://, we don't change it.
    if args.prefix:
        logging.debug("Prefixing URLs...")
        urls = ["https://" + url
                if not url.startswith(("https://", "http://"))
                else url
                for url in urls]

    logging.debug("List of URLs: {0}".format(" | ".join(url for url in urls)))

    # Quote the URLs by escaping the special characters.
    quote_urls = urllib.parse.quote_plus(json.dumps({"urls": urls},
                                                    separators=(',', ':')))

    output = OUTPUT_LIST.format(BASE_URL, TEST_NAME, quote_urls, MIN_VER)
    logging.debug(output)
    return output


def parse_args():
    parser = argparse.ArgumentParser(
            description="Generate an OONI Run link from a list of URLs"
            )
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
            "--file",
            metavar="input-file",
            help="input file with list of URLs separated by a new line"
            )
    group.add_argument(
            "--list",
            nargs='+',
            help="enter list of URLs as command line arguments"
            )
    parser.add_argument(
            "--prefix",
            action="store_true",
            help="automatically prefix URLs with https://"
            )
    parser.add_argument(
            "--verbose",
            action="store_true",
            help="show verbose output (enable logging)"
            )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.verbose:
        logging.basicConfig(format='%(asctime)s %(message)s',
                            level=logging.DEBUG)
    if not any([args.file, args.list]):
        sys.exit("You must select either the --file or the --list option.")

    logging.debug("Starting {0}".format(sys.argv[0]))
    print(rungen_urls(args))
