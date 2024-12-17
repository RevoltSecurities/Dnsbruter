from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as streamr:
    long_description = streamr.read()

setup(
    name='DNSBruter',
    version='1.0.6',
    author='D. Sanjai Kumar @RevoltSecurities',
    author_email='bughunterz0047@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RevoltSecurities/Dnsbruter",
    description='dnsbruter is a powerful tool for asynchronous DNS bruteforcing and fuzzing with wildcard detection',
    packages=find_packages(),
    install_requires=[
        'aiodns>=3.2.0',
        'aiofiles>=24.1.0',
        'alive_progress>=3.2.0',
        'art>=6.1',
        'asynciolimiter>=1.1.0.post3',
        'colorama>=0.4.4',
        'Requests>=2.32.3',
        'setuptools>=68.1.2',
        'uvloop>=0.21.0'
    ],
    entry_points={
        'console_scripts': [
            'dnsbruter = dnsbruter.dnsbruter:main'
        ]
    },
)
