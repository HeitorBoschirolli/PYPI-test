## Hello world package to test PYPI upload
This repository was based on
[this](https://realpython.com/pypi-publish-python-package/) guide.

### Upload to test.PYPI
* update the version on both __init__.py and setup.py
* create source archives and python wheels with 
`python setup.py sdist bdist_wheel`
* run `twine check dist/*` to check if the package description will render
  properly on PyPI
* run 
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
to upload the package

### Download the package using PIP
* `pip install pip install -i https://test.pypi.org/simple/ hellozawarudo`
