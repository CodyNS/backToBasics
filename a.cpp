// author: Cody N.S. |  project: "Back to Basics"

#include <iostream>
#include <string>

using namespace std;

void print(string st) {
    cout << st << endl;
}

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
    cout << "\nThank you " << name << ". Half your input number is: " 
         << x/2  << endl;


    // conditionals
    if (x > 200)
        print("Your input number is greater than 200");
    else if (100 < x && x <= 200)
        print("Your input is > 100 but <= 200");
    else
        print("Your input number is <= 100");
    

    // use natural language for not, and, or
    if (x % 25 == 0 || (x % 99 == 0 && x > 0))
        print("Woot! Special number!");
    

    // checking membership (works for strings, lists, other listy shit like that)
    cout << "Your name '" + name + "' is ";
    string st = "Hello, World!";
    if (st.find(name) == string::npos)
        cout << "not ";
    cout << "in '" + st + "'\n\n";
    

    // loops
    int sum = 0;
    for (int i = 0; i <= 10; i++) {
        sum += i;
        cout << "i = " << i << "\t total = " << sum << endl;
    }
    
    print("");
    string foo = "foobar";
    for (char ch : foo)  // for-each loop
        cout << ch << "-";
    
    print("\n");
    sum = 0;
    int temp = 0;
    while (temp >= 0) {
        cout << "Enter a non-negative integer (negative to end the calculation): ";
        cin >> temp;
        if (temp >= 0)
            sum += temp;
    }
    print("\n  Final total: " + to_string(sum));


    cout << endl;
    return 0;
}