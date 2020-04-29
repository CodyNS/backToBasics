// Java time!
import java.util.Scanner;

public class a {


    private static void print(String s) {
        System.out.print(s);
    }
    private static void println(String s) {
        System.out.println(s);
    }
    // private void print(String s) {
    //     System.out.print(s);
    // }


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
        keyboard.close();
        println("Thank you " + name + ". Half of that is: " + x/2);











        System.out.println();
    }
    
}