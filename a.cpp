#include <iostream>
#include <string>

using namespace std;


int main() {
    cout << "\n";

    const double PI = 3.14159265358979;

    // format specifiers
    printf("%20.5lf %20.8lf \n\n", PI, PI);  

    // input
    string name;
    int x;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter an integer: ";
    cin >> x;
    cout << "Thank you " << name << ". Half of that is: " << x/2;



    cout << "\n\n";
    return 0;
}