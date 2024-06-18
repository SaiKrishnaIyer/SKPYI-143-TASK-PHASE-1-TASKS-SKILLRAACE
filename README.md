# SkillRaace Internship Phase - 1

## Phase 1 Tasks

### Task 1A

#### i) Sentence Generation

Write a Python program to generate all sentences where the subject is in ["I", "You"], the verb is in ["Play", "Love"], and the object is in ["Cricket", "Ludo"].

#### ii) Emoji Conversion

Convert emojis into text in Python using the `demoji` module. The module accurately removes and replaces emojis in text strings.

### Task 1B

#### i) Book and Ebook Class Design

Design a `Book` class with the following instance variables:
- Title
- Author
- Publisher
- Price
- Author's Royalty

Provide getter and setter properties for all variables. Define a method `royalty()` to calculate the royalty amount the author can expect to receive based on sales:
- 10% of the retail price on the first 500 copies sold
- 12.5% for the next 1,000 copies sold
- 15% for all further copies sold

Design a new `Ebook` class inherited from the `Book` class. Add an additional instance variable for the ebook format (EPUB, PDF, MOBI, etc.). Override the `royalty()` method to deduct GST at 12% on ebooks.

#### ii) Simple FLAMES Game Implementation

Implement a simple FLAMES game using Python.
