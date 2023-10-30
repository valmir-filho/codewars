/*
Determine, whether a given year is a leap year or not.

In case you don't know the rules, here they are:

- Years divisible by 4 are leap years.
- Years divisible by 100 are not leap years.
- Years divisible by 400 are leap years.
*/

#include <stdio.h>
#include <stdbool.h>

bool IsLeapYear(int year) {
    
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
   
    int year = 2023;

    if (IsLeapYear(year)) {
        printf("%d is a leap year.\n", year);
    } else {
        printf("%d isn't a leap year.\n", year);
    }    

    return 0;
}
