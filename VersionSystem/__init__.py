from .VersionSystem import VersionSystem


__all__ = [
    "VersionSystem",
    "VersionSystemRulesMDFileContent"
]

def _() -> str:
    import os, pathlib

    folder = pathlib.Path(__file__).parent.resolve()

    with open(os.path.join(folder, './VersionSystemRules.md'), 'r', encoding='UTF-8') as f:
        VersionSystemRulesMDFileContent = f.read()

    del f, os, pathlib, folder

    return VersionSystemRulesMDFileContent

VersionSystemRulesMDFileContent = _()

del _

import _del_

_del_.del___pycache__()

del _del_
