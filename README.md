# jissa

This is the coding playground for the program to be uploaded to the Intel Galileo board.

Note: Timestamp is in military time format

* Anaiss: An iPhone Passcode Brute-force Cracking Device
    * To-do list:
        * Get the iPhone hash/encryption file
        * Formulate algorithm for getting all permutations from 0000 to 9999
        * Input all permutations to the target iPhone device

* DigiLog: A Digital Logic Design Calculator
    * To-do list:
         * Study the schematic of a calculator
         * Validate given input is in correct format, i.e. in correct mathematical form [Accomplished: 12.29.2015 (a) & (b) update]
         * Isolate each operands and operators [Accomplished: 12.29.2015 (a) & (b) update]
         * Run through the operands per character for the positional notation conversion (to convert the given operands to base 10) [Accomplished: 12.25.2015 (c), (e), & (f) update]
         * Calculate the result [Accomplished: 12.29.2015 (a) & (b) update]
         * Convert the result to the target base by division operation [In progress: 12.31.2015 (d), (e), (f), & (g) update]


* Updated: 12.24.2015 - 01:24
   * Updated the project description
* Updated: 12.25.2015 - 02:06
   * Added the 'anaiss' and 'digilog' directories (a)
   * Moved the permutation.py to 'anaiss' directory (b)
   * Added modules whole-number-converter.py and decimal-number-converter.py (c)
   * Updated the project description (d)
* Updated: 12.25.2015 - 19:00
   * Logged the accomplished task -- [Accomplished: 12.25.2015 (c) update]
* Updated: 12.25.2015 - 19:12
   * Added the module for separation of whole number and decimal number of a given number (e)
* Updated: 12.25.2015 - 19:40
   * Updated the given-number.py to separate whole number and decimal number of a given number (f)
* Updated: 12.25.2015 - 19:52
   * Renamed all the files under the 'digilog' folder:
      * "decimal-number-converter.py" --> "decimal.py"
      * "given-number.py" --> "given.py"
      * "whole-number-converter.py" --> "whole.py"
* Updated: 12.25.2015 - 20:32
   * Added digilog/Digilog.java file as the Java version of the DigiLog project
* Updated: 12.26.2015 - 00:55
   * Added and completed the separate() function in Digilog.java class
* Updated: 12.26.2015 - 14:50
   * Changed the value of x to 0 (digilog/decimal.py, line 5) -- conversion for the decimal part must start from left to right
   * Changed the increment of x from x -= 1 to x += 1 to accomodate the conversion from left to right (digilog/decimal.py, line 9)
* Updated: 12.26.2015 - 15:05
   * Removed the HashMap as the return value for digilog/Digilog.java [Digilog.separate(), lines 6-17] since the value from the HashMap cannot be converted to a number data type
   * Completed the function to convert the decimal part to its base 10 equivalent [Digilog.decimal(), lines 19-25]
* Updated: 12.26.2015 - 15:38
   * Created the digilog/digilog package
   * Added the digilog/digilog/__init__.py for other modules to import the digilog/digilog package
   * Renamed digilog/decimal.py to digilog/digilog/Decimal.py
   * Renamed digilog/whole.py to digilog/digilog/Whole.py
   * Imported the digilog/digilog package in the digilog/given.py [given.py, line 2]
   * Used the methods from digilog/digilog/Decimal.py and digilog/digilog/Whole.py in the digilog/given.py [given.py, lines 16-17]
* Updated: 12.26.2015 - 20:45
   * Completed the function to convert the whole number part to its base 10 equivalent [Digilog.whole(), lines 27-33]
* Updated: 12.26.2015 - 21:40
   * Changed the source code documentation in digilog/digilog/Decimal.py, digilog/digilog/Whole.py, and digilog/given.py
* Updated: 12.27.2015 - 19:00
   * Added the draft version of the Research Plan for the two projects: (1) Digilog, and (2) Anaiss
* Updated: 12.27.2015 - 20:14
   * Written the main() method of digilog/given.py, the method utilizes the separation of decimal number and whole number, then convertion to its base-10 equivalent from the given base
      * To solve: Parsing of an expression (e.g. 123.123 (base 8) + 456.456 (base 16) = ?)
* Updated: 12.29.2015 - 00:29
   * Added the regular expression that recognizes mathematical expression input per token (e.g. '10', '+', '10') (a)
* Updated: 12.29.2015 - 19:05
   * Finalized the given.evaluate_expression() method (b)
* Updated: 12.29.2015 - 20:02
   * Renamed digilog/given.py to digilog/main.py
* Report: 12.30.2015 - 01:30
   * Bug: Error in parsing operations -, *, and /. Only works on +
* Bug fixed: 12.30.2015 - 01:46
   * Accepts subtraction (-) operation, but still problem with multiplication (*) and division (/)
* Report: 12.30.2015 - 02:05
   * decimal_separate() function still gives decimal digits even if the given is integer
      * Problem is in the conditional block [digilog/main.py, lines 12 - 17]
* Revision: 12.30.2015 - 12:21
   * decimal_separate() method has been revised of digilog/main.py. Instead of manual looping through characters, math.modf() function was used.
* Bug fixed: 12.30.2015 - 20:14
   * Fixed the problem with acceptance of operators
* Updated: 12.30.2015 - 20:24
   * Added a Try...Catch clause for Syntax Error in evaluate_expression() method [digilog/main.py, lines 25-28]
* Bug report: 12.30.2015 - 20:16
   * Add a validation to decline letter and other symbols as input
* Report: 12.30.2015 - 21:41
   * Must test the eval() in the digilog/main.py, and set some security measures
* Updated: 12.30.2015 - 21:51
   * Completed the separate() method in digilog/Digilog.java
* Bug report: 12.31.2015 - 02:54
   * Must accept parenthesis as token (a)
* Bug fixed: 12.31.2015 - 02:59
   * Already accepts parenthesis as token (b)
* Updated: 12.31.2015 - 03:14
   * Added the revised version of the Research Plan for DigiLog (c)
* Updated: 12.31.2015 - 14:59
   * Added the convert_result() method in  digilog/main.py (d)
* Updated: 12.31.2015 - 21:35
   * Added the hexa_convert() method in the digilog/main.py module. It converts digits 10-15 to their hexadecimal equivalent (e)
* Updated: 12.31.2015 - 23:12
   * Used the hexa_convert() method. Testing needed. (f)
* Updated: 12.31.2015 - 23:36
   * Added hexa_convert() method in the else block of convert_result() (g)
* Bug report: 01.01.2016 - 00:00
   * Does not output decimal [123.456 (base-16) --> 100100011 (base-2)]
* Bug report: 01.01.2016 - 00:04
   * Parse hexadecimal inputs (A -> 10, B -> 11, C -> 12, etc.)
* Updated: 01.01.2016 - 00:15
   * Revised the Research Plan for DigiLog, added connecting wires to the materials.
* Updated: 01.01.2016 - 00:45
   * Added the parsing of hexadecimal tokens into decimal
* Updated: 01.01.2016 - 13:10
   * Moved the methods convert_hexa(), convert_result(), and hexa_convert() of digilog/main.py to new module digilog/digilog/Converter.py
   * Modified the imports of digilog/digilog/__init__.py to include the methods from new module Converter.py
