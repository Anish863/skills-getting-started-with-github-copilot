import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.print("Enter first number: ");
            double a = sc.nextDouble();

            System.out.print("Enter operator (+ - * / %): ");
            String op = sc.next();

            System.out.print("Enter second number: ");
            double b = sc.nextDouble();

            switch (op) {
                case "+":
                    System.out.println("Result: " + (a + b));
                    break;
                case "-":
                    System.out.println("Result: " + (a - b));
                    break;
                case "*":
                case "x":
                case "X":
                    System.out.println("Result: " + (a * b));
                    break;
                case "/":
                    if (b == 0) {
                        System.out.println("Error: Division by zero");
                    } else {
                        System.out.println("Result: " + (a / b));
                    }
                    break;
                case "%":
                    if (b == 0) {
                        System.out.println("Error: Modulo by zero");
                    } else {
                        System.out.println("Result: " + (a % b));
                    }
                    break;
                default:
                    System.out.println("Invalid operator");
            }

            System.out.print("Do another calculation? (y/n): ");
            if (!sc.next().equalsIgnoreCase("y")) break;
        }

        sc.close();
        System.out.println("Goodbye!");
    }
}