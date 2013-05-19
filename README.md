This is a branched version of the NIST sts-2.1.1 statistical test suite.
The /conversionscripts folder is a bunch of useful python scripts for converting various files of random data into binary streams for inputting to the program.

The reason to branch the test suite is two-fold:
1. insert better error handling/printing, as the current suite likes to spit out errors that are extremely cryptic.
2. improve the interface over time, the current command-line interface does not support TAB completion etc.

Thanks to NIST for developing the software, get the original version here:
http://csrc.nist.gov/groups/ST/toolkit/rng/documentation_software.html

http://csrc.nist.gov/groups/ST/toolkit/rng/documents/SP800-22rev1a.pdf

Software disclaimer: "This software was developed at the National Institute of Standards and Technology by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. The NIST Statistical Test Suite is an experimental system. NIST assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgment if the software is used."
