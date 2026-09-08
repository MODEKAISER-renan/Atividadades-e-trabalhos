import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Produto> produtos = new ArrayList<>();

    static Produto Busca(ArrayList<Produto> lista,Integer verificacao){
        for(Produto produto : lista){
            if(verificacao.equals(produto.getCodigo())){
                return produto;
            }
        }
        return null;
    }

    static void Cadastrar(int codigo,String nome , double preco,ArrayList<Produto> lista){
        Produto p = new Produto(codigo, nome, preco);
        lista.add(p);
    }

    static void Listar(ArrayList<Produto> lista){
        for (Produto p : lista) {
            System.out.println(p);
        }
    }

    static void AlterarPreco(double preco, Produto p){
        if(p == null){
            System.out.println("Código do produto incorreto!");
            return;
        }else{
            p.setPreco(preco);
            System.out.println("Preço atualizado para " + preco + " com sucesso!");
        }
    }

    static void Excluir(Produto p,ArrayList<Produto> lista){
        if(p == null){
            System.out.println("Código do produto incorreto!");
            return;
        }else{
            lista.remove(p);
            System.out.println("Produto " + p + " excluido com sucesso com sucesso!");
        }
    }

    public static void main(String[] args) {
        ArrayList<Produto> lista = new ArrayList<Produto>();
        int opcao = 0;

        while (opcao != 5) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preço");
            System.out.println("4 - Remover");
            System.out.println("5 - Sair");
            System.out.print("Opção: ");

            opcao = teclado.nextInt();
            teclado.nextLine();

            if (opcao == 1) {
                System.out.print("Digite o código do produto:");
                int codigo = teclado.nextInt();

                System.out.print("Digite o nome do produto:");
                String nome = teclado.nextLine();

                System.out.print("Digite o preço do produto:");
                double preco = teclado.nextDouble();

                Cadastrar(codigo,nome,preco,lista);

            } else if (opcao == 2) {
                Listar(lista);

            } else if (opcao == 3) {
                System.out.print("Digite o código do produto que deseja alterar o preço:");
                Integer verificacao = teclado.nextInt();

                System.out.print("Digite o novo preço:");
                double preco = teclado.nextDouble();

                AlterarPreco(preco, Busca(lista, verificacao));
                
            } else if (opcao == 4) {
                System.out.print("Digite o código do produto que deseja excluir:");
                Integer verificacao = teclado.nextInt();
                Excluir(Busca(lista, verificacao), lista);
            }
        }

        System.out.println("Sistema encerrado.");
    }
}