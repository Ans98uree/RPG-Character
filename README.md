RPG Character Creator

A Python-based console application that simulates an RPG (Role-Playing Game) character creation system. The program allows users to create custom characters by assigning points to core attributes while enforcing predefined game rules through input validation.

Overview
This project demonstrates fundamental Python programming concepts, including:

Functions

Conditional Statements
Input Validation
String Manipulation
Error Handling
User Input Processing
The application ensures that character creation follows specific constraints and prevents invalid configurations.

Features

Create custom RPG characters
Validate character names
Allocate stat points across attributes
Enforce game rules and constraints
Display a formatted character sheet
Provide descriptive error messages for invalid input
Character Attributes
Each character contains three primary attributes:

Attribute	Description

Strength (STR)	Represents physical power and combat ability
Intelligence (INT)	Represents knowledge, reasoning, and magical aptitude
Charisma (CHA)	Represents social influence and communication skills


Validation Rules
The system validates the following conditions before creating a character:

Character name must be a string
Character name cannot be empty
Character name cannot exceed 10 characters
Character name must not contain spaces
Attribute values must be integers
Attribute values must be between 1 and 4
The sum of all attributes must equal exactly 7 points

Example Output

rex
STR ●●○○○○○○○○
INT ●●●●○○○○○○
CHA ●○○○○○○○○○

