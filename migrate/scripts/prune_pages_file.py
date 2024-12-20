"""
Prunes the pages file by removing pages which are marked as redirects but have no corresponding
redirect in the redirects file.

Output is written to stdout.
"""

import io
import sys
import gzip

# Validate input arguments.
if len(sys.argv) < 3:
  print('[ERROR] Not enough arguments provided!')
  print('[INFO] Usage: {0} <pages_file> <redirects_file>'.format(sys.argv[0]))
  sys.exit()

PAGES_FILE = sys.argv[1]
REDIRECTS_FILE = sys.argv[2]

if not PAGES_FILE.endswith('.gz'):
  print('[ERROR] Pages file must be gzipped.')
  sys.exit()

if not REDIRECTS_FILE.endswith('.gz'):
  print('[ERROR] Redirects file must be gzipped.')
  sys.exit()

# Create a dictionary of redirects.
REDIRECTS = {}
with gzip.open(REDIRECTS_FILE, 'rt', encoding='utf-8') as redirects_file:
    for line in redirects_file:
        source_page_id, _ = line.rstrip('\n').split('\t')
        REDIRECTS[source_page_id] = True

# Loop through the pages file, ignoring pages which are marked as redirects but which do not have a
# corresponding redirect in the redirects dictionary, printing the remaining pages to stdout.
with gzip.open(PAGES_FILE, 'rt', encoding='utf-8') as pages_file:
    for line in pages_file:
        page_id, page_title, is_redirect = line.rstrip('\n').split('\t')

        # Keep the page if it is not a redirect or if it has a corresponding entry in REDIRECTS
        if is_redirect == '0' or page_id in REDIRECTS:
            print('\t'.join([page_id, page_title, is_redirect]))
