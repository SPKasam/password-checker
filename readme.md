#Password Checker

This app was created to more securely check if my password
has been hacked or not, as I don't need to send my password to
another server/website where it may be intercepted.

Uses the pwnedpasswords.com api to check whether a
password has been hacked before or not (whether it is in their database).
Utilizes K anonymity and only sends the api the first 5 characters of our hashed
password. This means the api never sees our full password, making it very secure.
We then iterate through the list of hashed passwords that
have the same first 5 digits and locally check if our hashed
password is contained in the list. If my password was seen before,
the program will provide the number of times it has been seen in 
a data breach.


