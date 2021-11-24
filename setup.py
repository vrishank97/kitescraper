from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Tool for bulk scraping data from Zerodha Kite'
LONG_DESCRIPTION = 'Tool for bulk scraping data from Zerodha Kite'

# Setting up
setup(
        name="kitescraper", 
        version=VERSION,
        author="Vrishank Bhardwaj",
        author_email="vrishank1997@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)