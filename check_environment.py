import sys
import importlib

packages = ['pandas', 'IPython', 'seaborn', 'pyarrow']

bad = []
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        bad.append("Can't import %s" % package)
else:
    if len(bad) > 0:
        print('\n'.join(bad))
        sys.exit(1)

