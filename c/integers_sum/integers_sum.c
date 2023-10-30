/*
Given two integers "a" and "b", which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers
are equal return "a" or "b".

Note: "a" and "b" are not ordered!

Examples

(a, b) --> output (explanation)

(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
*/

#include <stdio.h>

int get_sum(int a, int b) {
    
    if (a == b) {
        return a;  // If "a" and "b" are equal, return either one
    } else if (a < b) {
        
        // Sum all integers from a to b
        int sum = 0;
        
        for (int i = a; i <= b; i++) {
            sum += i;
        }

        return sum;
    } else {
        
        // Sum all integers from b to a
        int sum = 0;

        for (int i = b; i <= a; i++) {
            sum += i;
        }
        return sum;
    }
}

int main() {
    printf("%d\n", get_sum(1, 0));  // Output: 1

    return 0;
}
