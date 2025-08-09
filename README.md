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

## Requirements

- Python 3.7+
- Required libraries:  
  ```bash
  pip install requests
