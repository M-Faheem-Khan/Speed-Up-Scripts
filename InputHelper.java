/*
* Name: Muhammad F. Khan
* Version: 1.0
* FileName: InputHelper.java
* Timestamp(date comments added): 01/24/2020, 02:38:07
* Language: Java
* Description: Helps Get User Input in a Safe Way. Also prevents redundant code
* License: MIT
*/

import java.util.InputMismatchException;
import java.util.Scanner;

public class InputHelper {
    public static double getDouble(String prompt) {
        // GET DOUBLE FROM USER
        Scanner sc = new Scanner(System.in); // input scanner
        double userInput;
        while(true) {
            try{
                System.out.print(prompt);
                return sc.nextDouble();
            } catch (InputMismatchException e){
                System.out.println("== Invalid Input ==");
                sc.nextLine(); // clearing keyboard buffer
            }
        }
    }

    public static int getInteger(String prompt) {
        // GET INTEGER FROM USER
        Scanner sc = new Scanner(System.in); // input scanner
        int userInput;
        while(true) {
            try{
                System.out.print(prompt);
                return sc.nextInt();
            } catch (InputMismatchException e){
                System.out.println("== Invalid Input ==");
                sc.nextLine(); // clearing keyboard buffer
            }
        }
    }


    public static String getString(String prompt) {
        // GET STRING FROM USER
        Scanner sc = new Scanner(System.in); // input scanner
        String userInput;
        while(true) {
            try{
                System.out.print(prompt);
                return sc.nextLine();
            } catch (InputMismatchException e){
                System.out.println("== Invalid Input ==");
                sc.nextLine(); // clearing keyboard buffer
            }
        }
    }
}
