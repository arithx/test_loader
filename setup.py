from setuptools import setup, find_packages

setup(
    name='test-loader',
    version='0.0.1',
    description='Runs & Verifies a test list via tempest.',
    author='Stephen Lowrie',
    author_email='stephen.lowrie@rackspace.com',
    url='https://github.com/arithx/defcore_runner',
    packages=find_packages(exclude=('tests*', 'docs')),
    install_requires=open('requirements.txt').read(),
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'test-loader = defcore_runner.run:entry_point']})
