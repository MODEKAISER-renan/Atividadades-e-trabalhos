public class Atividade_Modulos{
    static void calcularDesconto(double valor,double percentual){
    System.out.printf("%.1f",valor*(percentual/100));
    }

    public static void main(String args){
        calcularDesconto(100,10);
    }
}