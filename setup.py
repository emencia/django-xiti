from setuptools import setup, find_packages

setup(
    name='django-xiti',
    version=__import__('xiti').__version__,
    description=__import__('xiti').__doc__,
    long_description=open('README.rst').read(),
    author='Emencia',
    author_email='dthenon@emencia.com',
    url='https://github.com/emencia/django-xiti',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)