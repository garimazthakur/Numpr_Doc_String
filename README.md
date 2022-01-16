# Numpr_Doc_String
In this repo we will create a documentation in the numpy doc string

# To get the clear view of the doc string, you can use 
import inspect
print(inspect.getdoc(the_function_name))

# You can get example_numpy.py here
https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html 

# For the basic python OOPs code that has been used, you can get it from the link given below:

https://github.com/codebasics/py/blob/master/Basics/17_class.pys

Also, instead of using:
print(function_name.__doc__) as __doc__ attribute contains the raw docstring i.e. tabs or spaces, So to get the clear version  use getdoc() from inspect module i.e. print(inspect.getdoc(function_name)) 

For more details refer to the link below:
https://www.youtube.com/watch?v=l3084gzo6Eo&ab_channel=DataCamp

# Add the follwing in the extensions object in config.py
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon']

# uncomment the path and add the folder to the path where your pyhton file exists, in the config.py
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
# Add
sys.path.append('source')

# For hosting your documentaion you can use https://readthedocs.org




