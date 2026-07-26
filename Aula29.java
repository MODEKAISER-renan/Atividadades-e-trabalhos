import java.util.ArrayList;

public class Aula29 {

    static double media(double[] turma){
    double total = 0.0;
    double i = 0.0;
    double media = 0.0;
    for (double aluno : turma){
        total += aluno;
        i++;
    }
        media = total/i;
        return media;
        
    }

    static int contarAprovados(double[] notas){
        int acimaDaMedia = 0;
        for (double estudante : notas){
            if (estudante >= 6.0){acimaDaMedia += 1;}
        }
        return acimaDaMedia;
    }

    static void Mete(ArrayList<String> produtos, String nome){
        produtos.add(nome);
    }

    static void Mostra(ArrayList<String> produtos){

    int i = 0;
    for (String item : produtos){
        i++;
        System.out.println(i + " - " +item);
    }
    System.out.println("");
    }

    static int menage(int[] valores){
        int Maior = 0;
        for(int comparado : valores){ if (Maior<comparado){Maior = comparado;} }
        return Maior;
    }

    static int menage(int a, int b){
        if (a>b) {return a;} else {return b;}
    }

    static void Boletim(double[] notas){
        System.out.println(media(notas));
        System.out.println(contarAprovados(notas));
        if (contarAprovados(notas)>0){System.out.println("APROVADA");} else{System.out.println("REPROVADA");}

    }

    public static void main(String[] args){
        ArrayList<String> produto = new ArrayList<>();

        System.out.println(media(new double[] {7.0,8.0,9.0}));
        System.out.println(media(new double[] {6.0,6.0,6.0,6.0}));
        System.out.println(media(new double[] {5.0, 10.0}) + "\n");

        System.out.println(contarAprovados(new double[] {7.0, 4.0, 9.0, 6.0}));
        System.out.println(contarAprovados(new double[] {2.0, 3.0, 5.0}));
        System.out.println(contarAprovados(new double[] {10.0, 8.0, 6.0}) + "\n");

        Mete(produto,"Pizza");
        Mete(produto,"Suco");
        Mostra(produto);

        System.out.println(menage(new int[] {3, 9, 5}));
        System.out.println(menage(12,7));
        System.out.println(menage(new int[] {4, 4, 4}));

        Boletim(new double[] {7.0, 5.0, 9.0, 6.0});
        Boletim(new double[] {4.0, 3.0, 5.0});

        System.exit(0);
    }

}
