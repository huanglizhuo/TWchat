rm -rf dist
python setup.py bdist_wheel
twine upload dist/* -u $PYNAME -p $PYPWD
