from setuptools import setup, find_packages
import re

VERSIONFILE = "__init__.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
	verstr=mo.group(1)
else:
	raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open('requirements.txt') as f:
	requirements = f.read().splitlines()
	requirements = [l for l in requirements if not l.startswith('#')]

setup(name='cloudCAVEr',
	version=verstr,
	description='cloud volume and CAVE client additional tools/helpers',
	url='',
	author='Nik Drummond',
	author_email='nikolas.drummond@bi.mpg.de',
	license='MIT',
	packages=find_packages(),
	zip_safe=False
)