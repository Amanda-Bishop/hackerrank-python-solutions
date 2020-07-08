# email-verification
Solution to the Hackerrank problem Validating and Parsing Email Addresses  
This program determines whether an email is valid based on the following criteria:
- It has a username, domain name, and extension 
- The username starts with an English alphabetical character, and any following characters consist are either -,.,_ or an alphanumeric character 
- The domain and extension contain only English alphabetical characters 
- The extension is 1-3 characters in length  
It takes input in the following form:  
n (a number greater than 0 and less than 100) representing the number of lines to follow. 
And for each following line username <username@domain.extension>  
The program will output the valid emails in the following form:  
username <username@domain.extension> 
