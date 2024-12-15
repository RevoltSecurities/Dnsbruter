from setuptools import setup, find_packages


    
setup(
    name='DNSBruter',
    version='1.0.5',
    author='D.Sanjai Kumar @RevoltSecurities',
    author_email='bughunterz0047@gmail.com',
    
    url="https://github.com/RevoltSecurities/Dnsbruter",
    description='dnsbruter is a powerfull tool for asynchronous dns brutforcing and fuzzing with wildcard detection',
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
