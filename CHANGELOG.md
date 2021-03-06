# CHANGELOG

This is a manually generated log to track changes to the repository for each release. 
Each section should include general headers such as **Implemented enhancements** 
and **Merged pull requests**. All closed issued and bug fixes should be 
represented by the pull requests that fixed them.

 - renamed commands
 - deprecated / removed commands
 - changed defaults
 - backward incompatible changes (recipe file format? image file format?)
 - migration guidance (how to convert images?)
 - changed behaviour (recipe sections work differently)

Versions in parentheses coincide with what is available on [pypi](https://pypi.org/project/scif/).

## [xxx](https://github.com/vsoch/scif/tree/master) (development)

 - copying of files should be relative to app folder (0.0.58)
 - fixed bug that install with python2 cannot use "exec" (0.0.55)
 - fixed bug in parsing filesystem that doesn't have SCIF (0.0.52)
 - added fix that install routine happens in context of approot
 - files need to be added before running commands
 - fixed bug with appfiles copy command (0.0.51)
 - initial creation of just the scif client. (0.0.5)
