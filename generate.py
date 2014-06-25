from __future__ import print_function

import functools
import sys

import yaml

if __name__ == "__main__":
    src, dest = sys.argv[1:]
    with open(src) as f:
        categories = yaml.load(f)
    with open(dest, "w") as f:
        f.write("""cheatsheet do
  title 'Python Format Strings'
  docset_file_name 'python_format_strings'
  keyword 'pyfmt'

  introduction 'Python String Formatting Reference'
""")
        _print = functools.partial(print, file=f)
        for category in categories:
            _print("  category do")
            _print("    id {!r}".format(category['name']))
            for example in category['examples']:
                _print("    entry do")
                _print("      command {!r}".format(example["command"]))
                _print("      name {!r}".format(example["name"]))
                if '   ' not in eval(example["command"]):
                    #workaround, multiple spaces do not appear well...
                    _print("      notes {!r}".format('Output: `{}`'.format(eval(example["command"]))))
                _print("    end")
            _print("  end")
        _print("end")
