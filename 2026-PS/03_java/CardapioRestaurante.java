import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        double valor = 0.0;
        int quantidade = 0;
        String produto = "";

        System.out.println("=================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Caldo de kenga...... R$ 15,00");
        System.out.println("=================================");
        System.out.println("     Restaurante do Renan.");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        if (opcao == 1) {
            System.out.println("Você escolheu X-Burguer.");
            valor = 18.00;
            produto = "X-Burguer";
        } else if (opcao == 2) {
            System.out.println("Você escolheu Pizza.");
            valor = 35.00;
            produto = "Pizza";
        } else if (opcao == 3) {
            System.out.println("Você escolheu Suco Natural.");
            valor = 8.00;
            produto = "Suco Natural";
        } else if (opcao == 4) {
            System.out.println("Você escolheu Café.");
            valor = 5.00;
            produto = "Café";
        } else if(opcao==4){
            System.out.println("Você escolheu caldo de kenga");
            valor = 8.00;
            produto = "caldo de kenga";
        } else {
            System.out.println("Opção inválida.");
        }

        System.out.print("Quantos você vai querer?: ");
        quantidade = entrada.nextInt();
        System.out.print("Você pediu " + quantidade +" " + produto +" o preço total è R$ " + (quantidade*valor) + " ");


        entrada.close();
    }
}