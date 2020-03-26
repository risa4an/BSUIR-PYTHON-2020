from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='lab2',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='Katya Risunova',
    author_email='katya.risunova@icloud.com',
    description='',
    long_description = long_description,
    entry_points={
        'console_scripts':
            ['mergesort = lab2.merge_sort.py',
             'nvector = lab2.n_vector.py']
        }

)
