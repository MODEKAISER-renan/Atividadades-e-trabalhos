import java.util.*;

public class Atividade04 {

    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       int A = Integer.parseInt(input.nextLine());
       double B = Double.parseDouble(input.nextLine());
       String C = input.nextLine();
       System.out.println("String: " + C + "\nDouble: " + B + "\nInt: " + A);
       input.close();
       System.exit(0);
       
    }
}