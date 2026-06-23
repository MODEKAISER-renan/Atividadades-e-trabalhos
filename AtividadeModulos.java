public class AtividadeModulos{

    static void calcularDesconto(double valor,double percentual){
    System.out.printf("%.1f\n",valor - valor*(percentual/100));
    }

    static void maiorNumero(int a, int b){
        if (a > b){
            System.out.println(a);
        }
        else{
            System.out.println(b);
        }
    }

    static void calcularFrete(double peso){
        if(peso <= 1){
            System.out.println("10.0");
        }else if(peso <= 5){
            System.out.println("20.0");
        }
        else{
            System.out.println("35.0");
        }
    }

    static void somar(int a, int b){
        System.out.println(a+b);
    }
    static void somar(double a,double b){
        System.out.printf("%.1f\n",a+b);
    }

    static void cardapio(String nome){
        System.out.println(nome);
    }
    static void cardapio(String nome, double preco){
        System.out.printf("%s\nR$ %.2f\n",nome,preco);
    }

    public static void main(String[] args){
        calcularDesconto(100,10);
        maiorNumero(10, 20);
        calcularFrete(8);
        somar(5,3);
        somar(2.5,3.5);
        cardapio("Refrigerante");
        cardapio("Pizza",39.90);
    }
}