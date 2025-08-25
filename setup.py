from setuptools import setup, find_packages

setup(
    name='whomst',
    version='0.1.0',
    description='Alan adı ve IP adresi sorgulamak için Python ile yazılmış bir WHOIS aracı.',
    author='mstsecurity',
    author_email='mailspammer444@gmail.com',
    url='https://github.com/mstsecurity/whomst',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: System :: Networking'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'whomst = whomst.whomst:main',
        ],
    },
)
