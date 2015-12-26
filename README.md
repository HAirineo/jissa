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
         * Validate given input is in correct format, i.e. in correct mathematical form
         * Isolate each operands and operators
         * Run through the operands per character for the positional notation conversion (to convert the given operands to base 10) [Accomplished: 12.25.2015 (c), (e), & (f) update]
         * Convert the result to the target base by division operation
    
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
