import java.util.Scanner;

public class Atividade05 {
    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);

                String s1=sc.next();int x1=sc.nextInt();
                String s2=sc.next();int x2=sc.nextInt();
                String s3=sc.next();int x3=sc.nextInt();

            System.out.println("================================");
            System.out.printf("%-15s%03d\n",s1,x1);
            System.out.printf("%-15s%03d\n",s2,x2);
            System.out.printf("%-15s%03d\n",s3,x3);
            System.out.println("================================");
            sc.close();
            System.exit(0);

    }
    
}
