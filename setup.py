import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    # package name
    name='hellozawarudo',
    # MAJOR.MINOR.PATCH
    # - increment MAJOR when you make incompatible API changes
    # - increment MINOR when you add backward-compatible functionality
    # - increment PATCH when you make backwards-compatible bug fixes
    # to make sure the version numbers here and inside the packages are
    # kept consistent, you can use Bumpversion
    version='0.1.0',
    description='nothing really important',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HeitorBoschirolli/hello-za-warudo/tree/master',
    author='Heitor Boschirolli',
    author_email='heitor.boschirolli@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    # find_packages(exclude=()) finds all packs and sub-packs
    packages=['hellozawarudo'],
    # if True setuptools include any data files it finds inside the package
    # directories that are specified by MANIFEST.in
    include_package_data=True,
    # list any dependencies to thrid party libraries
    install_requires=['numpy', 'scikit-image'],
    # entry points are used to support dynamic discovery of services or
    # plugins provided by a project
    entry_points={
        'console_scripts': [
            'hellozawarudo=hellozawarudo.__main__:main'
        ]
    }
)
