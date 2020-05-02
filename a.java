// author: Cody N.S. |  project: "Back to Basics"
// Java time!

import java.util.Scanner;

public class a {

    // because I don't feel like typing System.out... every time
    private static void print(String s) {
        System.out.print(s);
    }
    private static void println(String s) {
        System.out.println(s);
    }


    public static void main(final String[] args) {
        System.out.println();

        final double PI = 3.14159265358979; 

        // format specifiers
        System.out.printf("%20.5f %20.8f \n\n", PI, PI); 


        // input
        String name;
        int x;
        Scanner keyboard = new Scanner(System.in);
        print("Enter your name: ");
        name = keyboard.nextLine();
        print("Enter an integer: ");
        x = keyboard.nextInt();
        println("\nThank you " + name + ". Half your input number is: " + x/2);


        // conditionals
        if (x > 200)
            println("Your input number is greater than 200");
        else if (100 < x && x <= 200)
            println("Your input is > 100 but <= 200");
        else
            println("Your input number is <= 100");
        

        // use natural language for not, and, or
        if (x % 25 == 0 || (x % 99 == 0 && x > 0))
            println("Woot! Special number!");
        

        // checking membership (works for strings, lists, other listy shit like that)
        print("Your name '" + name + "' is ");
        String st = "Hello, World!";
        if (!st.contains(name))
            print ("not ");
        println("in '" + st + "'\n");
        

        // loops
        int sum = 0;
        for (int i = 0; i <= 10; i++) {
            sum += i;
            println("i = " + i + "\t total = " + sum);
        }
        
        println("");
        String foo = "foobar";
        for (char ch : foo.toCharArray()) // like a for-each loop
            print(ch + "-");
        
        println("\n");
        sum = 0;
        int temp = 0;
        keyboard.nextLine(); // burn the "\n" that's caught in the stream at this point
        while (temp >= 0) {
            print("Enter a non-negative integer (negative to end the calculation): ");
            temp = keyboard.nextInt();
            if (temp >= 0)
                sum += temp;
        }
        println("\n  Final total: " + sum);




        keyboard.close(); // don't close a System.in object unless at very end of program
        System.out.println();
    }
    
}