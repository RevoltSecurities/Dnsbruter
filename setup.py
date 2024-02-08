from setuptools import setup, find_packages

setup(
    name='DNSBruter',
    version='1.0.3',
    author='D.Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description='A next level tool for subdomain bruteforcing',
    packages=find_packages(),
    install_requires=[
        'aiodns>=3.1.1',
        'aiofiles>=23.2.1',
        'alive_progress>=3.1.4',
        'art>=6.1',
        'async_dns>=2.0.0',
        'colorama>=0.4.4',
        'dnspython>=2.5.0',
        'Requests>=2.31.0',
        'urllib3>=1.26.18'
        ],
    entry_points={
        'console_scripts': [
            'dnsbruter = dnsbruter.dnsbruter:main'
        ]
    },
)
