# SOUNDEX (Sounds Like) Algorithm in Python 3+

> This repository is purely for reference and is illustrative in it is purpose. This is one of the many ways of implementing this algorithm. 


This project illustrates an implementation of the [SOUNDEX Algorithm](https://en.wikipedia.org/wiki/Soundex) in Python. The Soundex Algorithm is a phonetic algorithm that allows indexing of english pronunciations regardless of minor differences of spelling.

Examples would be **Ghosh** and **Gauss**, or **Ladd** and **Lloyd**, as they "*sound alike*".

The Soundex Algorithm is mostly seen closer to the database/datastore tier, however there is often a need to utilize this functionality in the application tier and even the front end in some cases. This is an example of doing just that. It is also an interesting algorithm as it teaches a lot of the basics and nuances of a language through implementation.

> **IMPORTANT**
>
> This algorithm was authored to be *readable* as to the steps to achieve consistant and expected SOUNDEX codes given the specification provided . **This code can be refactored to be more compact and performant if needed.**


## Prerequisites

Before you continue, ensure you have met the following requirements:

* Python 3 installed
* PyTest installed (to run the unit tests if need be)

## Running / Testing

* Issue from the command line **pytest**


## Notes

* This implementation will differ from the SQL implementaton of SOUNDEX, and provide different results in somecases.
* This repository is heavily commented to provide context as to what and why, if in VS Code feel free to collapse all comments if they are obtrusive
    * On Mac -> Press <kbd>&#8984;</kbd> + <kbd>K</kbd> then <kbd>&#8984;</kbd> + <kbd>/</kbd> 
    * On Windows & Linux -> Press <kbd>Ctrl</kbd> + <kbd>K</kbd> then <kbd>Ctrl</kbd> + <kbd>/</kbd> 
* The SOUNDEX validation words are from various sites across the web, there will be more added and augmentation of the algorithm when edge cases are found.

## Try

* adding or removing parts of the code to achieve the SQL implementation where **Tymczak** == **T520** instead of **T522**
* adjusting the parameters to allow for more precision on the coded output
