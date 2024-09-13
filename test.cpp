#include <iostream>
using namespace std;

int main() {
    int n=5, sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    // Output the result
    cout << "The summation of numbers from 1 to " << n << " is: " << sum << endl;

    return 0;
}
