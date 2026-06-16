import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        double valor = 0.0;
        int quantidade = 0;

        String[] produtos = {
            "X-Burguer",
            "Pizza",
            "Suco Natural",
            "Café",
            "Caldo de Kenga"
        };

        Double[] preco_produto = {
            18.00,
            35.00,
            8.00,
            5.00,
            15.00
        };


        System.out.println("=================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("=================================");
        for(int i = 1; i < produtos.length; i ++){
            System.out.println((i+1) + " -- " + produtos[i] + " R$ " + preco_produto[i]);
        }
        System.out.println("=================================");
        System.out.println("      Restaurante do Renan.");
        System.out.println("=================================");
    
        while(true)
        {
            System.out.print("Escolha uma opção: ");
            int opcao = entrada.nextInt();
            switch(opcao){
            case 1: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
            case 2: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
            case 3: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
            case 4: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
            case 5: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
            default: 
                System.out.println("Opção inválida.");
            }
            System.out.print("Quantos você vai querer?: ");
            quantidade = entrada.nextInt();
            System.out.println("Deseja continuar comprando? [1]sim / [2]não");
            if (entrada.nextInt() == 1) {continue;} else {break;}
        }

        System.out.print("Você pediu " + quantidade +" " +" o preço total è R$ " + (quantidade*valor) + " ");


        entrada.close();
    }
}