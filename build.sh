rm -rf dist
pip install twine
python setup.py bdist_wheel
#twine upload dist/* -u $PYNAME -p $PYPWD
