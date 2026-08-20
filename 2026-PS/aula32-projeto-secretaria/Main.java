/*
*Diciplina: 2026-PS
*Estudante: Renan Soares da Silva
*Projeto: Aula32-projeto-secretaria
*arquivo: Aluno.java
*/

import java.util.ArrayList;
import java.util.Scanner;


public class Main{

    static void cadastrar(ArrayList<Aluno> lista, Scanner input){
        System.out.print("Nome: ");
        String nome = input.nextLine().trim();
        System.out.print("Matricula: ");
        String matricula = input.nextLine().trim();
        System.out.print("Curso ");
        String curso = input.nextLine().trim();
        Aluno novo = new Aluno(nome,matricula,curso);
        lista.add(novo);
        }
    
    static void Listar(ArrayList<Aluno> lista){
        for(Aluno aluno : lista){
            System.out.printf("\nNome: " + aluno.getNome() + "\nMatricula: " + aluno.getMatricula() + "\nCurso: " + aluno.getCurso() + "\n");
        }
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while (true){
            System.out.println("==========================================================");
            System.out.println("     SECRETARIA DO RENAN            ");
            System.out.println("==========================================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = input.nextLine().trim();

            if (opcao.equals("0")){System.out.println("Secretaria fechada. Ate a proxima!"); break;}
            else if(opcao.equals("1")){cadastrar(lista,input);}
            else if(opcao.equals("2")){Listar(lista);}
            else{System.out.println("Opção invalida!");}
        }
    }


}