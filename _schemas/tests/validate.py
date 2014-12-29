
"""Checks our data for syntax errors and compliance with the
schema.
"""

from pathlib import Path
import sys

from jsonschema import (
    Draft4Validator as Validator,
    FormatChecker)
import yaml


def main(folder):
    exit_status = 0

    with (Path('_schemas')/'{filename}.yaml'.format(
            filename=folder.rstrip('s/'))).open() as f:
        validator = Validator(yaml.load(f), format_checker=FormatChecker(
            ['date']))

    for item in Path(folder).iterdir():
        with item.open() as f:
            errors = validator.iter_errors(yaml.load(f))
            if errors:
                exit_status = 1
                for error in errors:
                    print('{item}: [{field}] {message}'.format(
                        item=item, field='/'.join(map(str, error.path)),
                        message=error.message))

    return exit_status


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
