import os
import sys

import PySide6

# NOTE: Модуль для упаковки приложения в установочные пакеты. https://cx-freeze.readthedocs.io/en/latest/
from cx_Freeze import setup, Executable

from ApplicationInfo import ApplicationInfo

plugins_path = os.path.join(PySide6.__path__[0], 'Qt', 'plugins')
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'
    plugins_path = os.path.join(PySide6.__path__[0], 'plugins')

options = {
    'build_exe': {
        'path': sys.path + ['src'],
        'include_files': [os.path.join(plugins_path, 'platforms')],
        'includes': ['queue'],
        'excludes': ['tkinter', 'unittest', 'pydoc', 'pdb'],
    },
    'bdist_msi': {
        # NOTE: uuid позволяет Windows правильно обновлять пакет после установки.
        'upgrade_code': '{C8568627-A138-4A54-9701-ABE32147933A}',
    }
}

executables = [
    Executable(
        script='main.py',
        base=base,
        target_name=ApplicationInfo.Name,
        shortcut_name=ApplicationInfo.Name
    )
]

setup(
    name=ApplicationInfo.Name,
    version=ApplicationInfo.Version,
    description=ApplicationInfo.Description,
    options=options,
    executables=executables
)
