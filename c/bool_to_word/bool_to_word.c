// Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

#include <stdio.h>
#include <stdbool.h>

const char* bool_to_word(bool value) {

    if (value == true) {
        return "Yes";
    } else {
        return "No";
    }
}

int main() {

    printf("%s\n", bool_to_word(true));
    printf("%s\n", bool_to_word(false));

    return 0;
}
