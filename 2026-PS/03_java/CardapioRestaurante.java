import java.util.Scanner;


public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        double valor = 0.0;
        int quantidade = 0;
        Double total = 0.0;
        int N_pedidos = 0;


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

        String[][] pedidos = new String[10][3];

        

        System.out.println("=================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("=================================");
        for(int i = 0; i < produtos.length; i ++){
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
                break;
            case 2: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
                break;
            case 3: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
                break;
            case 4: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
                break;
            case 5: 
                System.out.println("Você escolheu " + produtos[opcao-1]);
                valor = preco_produto[opcao-1];
                break;
            default: 
                System.out.println("Opção inválida.");
                break;
            }
            System.out.print("Quantos você vai querer?: ");
            quantidade = entrada.nextInt();
        
            pedidos[N_pedidos][0] = String.valueOf(quantidade);
            pedidos[N_pedidos][1] = produtos[opcao-1];
            pedidos[N_pedidos][2] = String.valueOf(valor);
            N_pedidos += 1;
            total += quantidade * valor + total;

            System.out.println("Deseja continuar comprando? [1]sim / [2]não");
            if (entrada.nextInt() == 1) {continue;} else {break;}
        }
        for(int i=0;i<N_pedidos;i++){System.out.println(pedidos[i][0]+" "+pedidos[i][1]+" R$ "+pedidos[i][2]);}
        System.out.printf("No total deu: R$ %.2f\n",total);

        entrada.close();
        System.exit(0);
    }
}