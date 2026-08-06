import java.util.ArrayList;

public class Aula31 {
    static void calculaSoma(int [] somar){
        int soma = 0;
        for(int n : somar){
            soma += n;
        }
        System.out.println(soma);
    }
    static void calcularMedia(int [] notas){
        int media = 0;
        for(int nota : notas){
            media += nota;
        }
        System.out.println(media/notas.length);
    }
    static void MaiorValor(int [] panteao){
        int campeao = panteao[0];
        for(int guerreiro : panteao){
            if(campeao < guerreiro){campeao = guerreiro;}
        }
        System.out.println(campeao);
    }
    static void MenorValor(int [] panteao){
        int derrotado = panteao[0];
        for(int guerreiro : panteao){
            if(derrotado > guerreiro){derrotado = guerreiro;}
        }
        System.out.println(derrotado);
    }
    static void ContaAcima(int [] numeros){
        int limite = 6;
        int cont = 0;
        for(int numero : numeros){
            if(numero > limite){cont++;}
        }
        System.out.println(cont);
    }

    public static void main(String[] args){
    int[] lista = {8, 3, 10, 5, 12};
        calculaSoma(lista);

        calcularMedia(lista);

        MenorValor(lista);

        MaiorValor(lista);

        ContaAcima(lista);

    System.exit(0);
    }
}