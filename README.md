# Password Strength Analyzer

A Python-based GUI application that evaluates password strength, checks for data breaches using the Have I Been Pwned API, and provides actionable suggestions for improvement.

## Features

- **Password Strength Calculation**  
  Uses entropy-based analysis to classify passwords as Weak, Moderate, or Strong.

- **Data Breach Detection**  
  Integrates with the Have I Been Pwned API to check if a password has appeared in known data breaches.

- **Improvement Suggestions**  
  Provides practical guidance on how to make the password more secure (length, character variety, special characters, etc.).

- **User-Friendly Interface**  
  Built with Tkinter, featuring a modern, accessible color palette and responsive design.

## Demo
![pass0](https://github.com/user-attachments/assets/ecc2fbe7-b15a-4878-bb26-0c9c92354858)
![pass1](https://github.com/user-attachments/assets/839b7186-a59b-493c-bc4d-b1df7792b173)
![pass2](https://github.com/user-attachments/assets/a8c8e493-2bd3-4196-af1b-42ec10013995)
![pass3](https://github.com/user-attachments/assets/03b42e1e-00c1-46ba-845a-5ae94445b650)
## Requirements

- Python 3.7+
- Required libraries:  
  ```bash
  pip install requests
## Disclaimer:
- This tool does not store or transmit your full password. For breach checks, it uses the HaveIBeenPwned API’s k-anonymity method, sending only the first 5 characters of the SHA1 hash.
