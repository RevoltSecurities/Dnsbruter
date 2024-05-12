from setuptools import setup, find_packages

with open("README.md", "r") as streamr:
    long_description = streamr.read()
    
setup(
    name='DNSBruter',
    version='1.0.4',
    author='D.Sanjai Kumar @RevoltSecurities',
    author_email='bughunterz0047@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RevoltSecurities/Dnsbruter",
    description='dnsbruter is a powerfull tool for asynchronous dns brutforcing and fuzzing with wildcard detection',
    packages=find_packages(),
    install_requires=[
        'aiodns>=3.1.1',
        'aiofiles>=23.2.1',
        'alive_progress>=3.1.4',
        'art>=6.1',
        'colorama>=0.4.4',
        'Requests>=2.31.0',
        'urllib3>=1.26.18'
        ],
    entry_points={
        'console_scripts': [
            'dnsbruter = dnsbruter.dnsbruter:main'
        ]
    },
)
