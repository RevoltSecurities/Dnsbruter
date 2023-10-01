from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='DNSBruter',
    version='1.0.1',
    author='D.Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description='A next level tool for subdomain bruteforcing',
    packages=find_packages(),
    install_requires=[
        'dnspython==2.4.2',
        'colorama==0.4.4',
        'setuptools==68.1.2'
    ],
    entry_points={
        'console_scripts': [
            'dnsbruter = dnsbruter.dnsbruter:main'
        ]
    },
    package_data={
        'dnsbruter': ['wordlists.txt'],
    },
)
