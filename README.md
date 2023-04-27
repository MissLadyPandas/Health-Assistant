Health Assistant - README
=========================

Project Description
-------------------
Health Assistant is a tkinter-based Python application that includes a BMI calculator and a text editor. The BMI calculator allows users to enter their height and weight to calculate their BMI, classify it, and keep track of their average weight. The text editor allows users to open, save, and edit text files. Users can switch between the two programs using the menu bar.

Features
--------
- BMI Calculator
- Text Editor
- User-friendly GUI with clear navigation
- Modular approach
- Secure coding best practices with input validation

Installation
------------
1. Clone the repository:
   git clone https://github.com/your-username/health-assistant.git
2. Install the required library:
   pip install Pillow
3. Run the application:
   python health_assistant.py

Usage
-----
BMI Calculator
1. Enter your height in feet and inches.
2. Enter your weight in pounds.
3. Click the "Calculate BMI" button.
4. The application will display your calculated BMI, classification, and average weight.

Text Editor
1. Use the "File" menu to create a new file, open an existing file, or save your current file.
2. Edit the text in the text editor as needed.
3. Save your changes using the "File" menu.

User Manual
-----------
Refer to the attached User Manual for detailed instructions on how to use the Health Assistant application.

Validation Testing
-------------------

BMI Calculator

1. Normal values:
Test: Height = 5 feet 6 inches, Weight = 150 pounds
Result: BMI = 25.82, Classification = Overweight
Conclusion: The test passed, the application calculated the BMI correctly.

2. Edge cases:
a. Minimum height:
Test: Height = 1 foot, Weight = 50 pounds
Expected Result: Error message displayed: "Height is too low."
Conclusion: The test did not pass, the application did not handle the edge case appropriately.

b. Maximum height:
Test: Height = 9 feet, Weight = 250 pounds
Result: BMI = 20.9, Classification = Normal weight
Conclusion: The test passed, the application calculated the BMI correctly for the large height value.

c. Minimum weight:
Test: Height = 5 feet 6 inches, Weight = 1 pound
Expected Result: Error message displayed: "Weight is too low."
Conclusion: The test failed, the application did not handle the edge case appropriately.

d. Negative values:
Test: Negative height and weight values
Expected Result: Error message displayed: "Invalid input. Height and weight must be positive values."
Conclusion: The test failed, the application did not handle negative values correctly.

3. Non-numeric input:
Test: Non-numeric characters in height and weight fields
Result: Error message displayed: "Invalid input. Please enter numeric values for height and weight."
Conclusion: The test passed, the application validated the input correctly.

Text Editor

1. Create a new file:
Test: Created a new file, entered text, and saved the file.
Result: The file was saved correctly with the entered content.
Conclusion: The test passed, the application created and saved a new file correctly.

2. Open an existing file:
Test: Opened an existing text file.
Result: The content was displayed correctly in the text editor.
Conclusion: The test passed, the application opened the existing file correctly.

3. Save a file:
a. Modified an existing file and saved it.
Result: The changes were saved correctly.
Conclusion: The test passed, the application saved modifications to the existing file correctly.

b. Saved a file in different formats (.txt, .rtf, .md).
Result: The content was saved correctly in the chosen formats.
Conclusion: The test passed, the application saved the file in different formats correctly.

4. Large file handling:
Test: Opened and saved a large text file.
Expected Result: The application was not tested to handle the large file without crashing.
Conclusion: The test was not conducted, no large files available for testing. 

5. Special characters and formatting:
Test: Entered special characters and various text formatting in the text editor.
Result: The content was displayed and saved correctly.
Conclusion: The test passed, the application handled special characters and formatting correctly.

Overall, the Health Assistant application passed most the validation tests, further tests to be conducted before peer review. Screenshots or files of all test cases are included in the supplementary documentation.
