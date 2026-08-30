/*
*Diciplina: 2026-PS
*Estudante: Renan Soares da Silva
*Projeto: Aula32-projeto-secretaria
*arquivo: Aluno.java
*/

import java.util.ArrayList;
import java.util.Scanner;


public class Main{

    static void Relatorio(ArrayList<Aluno> lista, Scanner input){
        System.out.println("Contar alunos de qual curso?");
        String pesquisa = input.nextLine().trim();
        int contador = 0;
        for(Aluno aluno : lista){
            if(aluno.getCurso().equals(pesquisa)){
                contador ++;
            }
        }
        System.out.println("Existem " + contador + " alunos cadastrados nesse curso e ao todo há " + lista.size() + " alunos.");
    }

    static void Delet(Aluno aluno,Scanner input,ArrayList<Aluno> lista){
        if(aluno == null){
            System.out.println("Aluno não encontrado, opreção invalida!");
        }
        else{
            System.out.println("Deseja mesmo apagar aluno " + aluno.getNome() + " de matricula " + aluno.getMatricula() + " ? [1] sim [0] não");
            String resposta = input.nextLine().trim();
            if(resposta.equals("1")){
                System.out.println("Aluno " + aluno.getNome() + " removido...");
                lista.remove(aluno);
                return;
            }
            else{
                System.out.println("Recusado ou opção  invalida, ação cancelada!");
                return;
            }
        }
    }

    static void Atualizar(Aluno aluno,Scanner input,ArrayList<Aluno> lista){
        if(aluno == null){
            System.out.println("Aluno não encontrado, encerrando operação!");
        }
        else{       
            System.out.println("Qual atributo desse alterar?\n[1] Nome\n[2] Matricula\n[3] Curso\n[4] Telefone");
            String escolha = input.nextLine().trim();
            if(escolha.equals("1")){
                System.out.print("Digite o novo nome:");
                String novo_nome = input.nextLine().trim();
                aluno.setNome(novo_nome);
                System.out.println("Nome alterado com sucesso!!!");
            }
            else if(escolha.equals("2")){
                String nova_matricula = Validacao_Matricula(lista, input);
                aluno.setMatricula(nova_matricula);
                System.out.println("Matricula alterado com sucesso!!!");
            }
            else if(escolha.equals("3")){
                System.out.print("Digite o novo curso:");
                String novo_Curso = input.nextLine().trim();
                aluno.setCurso(novo_Curso);
                System.out.println("Curso alterado com sucesso!!!");
            }
            else if(escolha.equals("4")){
            System.out.print("Digite o novo telefone:");
            String novo_Telefone = input.nextLine().trim();
            aluno.setTelefone(novo_Telefone);
            System.out.println("Telefone alterado com sucesso!!!");
            }else{
                System.out.println("Opção invalida, voltando ao menu.");
            }
        }
    }

    static Aluno Busca(ArrayList<Aluno> lista, Scanner input){
        System.out.println("Buscar por nome ou por matricula? [1]Nome [2]Matricula");
        String escolha = input.nextLine().trim();
        if(escolha.equals("2")){
            System.out.println("Busca por qual matricula? ");
            String matricula_busca = input.nextLine().trim();
            for(Aluno aluno : lista){
                if(matricula_busca.equals(aluno.getMatricula())){
                    return aluno;
                }
            }
            System.out.println("Matricula não encontrada!!!");
            return null;
        }else if(escolha.equals("1")){
            System.out.println("Busca por qual Nome? ");
            String nome_busca = input.nextLine().trim();
            for(Aluno aluno : lista){
                if(nome_busca.equals(aluno.getNome())){
                    return aluno;
                }
            }
            System.out.println("Nome não encontrado!!!");
            return null;
        }
        else{
            System.out.println("Opção invalida!");
            return null;
        }

    }

    static String Validacao_Matricula(ArrayList<Aluno> lista,Scanner input){
        while(true){
            boolean matricula_correta = true;
            System.out.print("Matricula: ");
            String matricula = input.nextLine().trim();
            for(Aluno numero : lista){
                if(matricula.equals(numero.getMatricula())){
                    matricula_correta = false;
                    break;
                }
            }
            if(matricula_correta == true){
                System.out.println("Matricula valida!.");
                return matricula;

            }
            else{
                System.out.println("Matricula invalida ou já cadastrada, tente novamnete!.");
            }
        }

    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner input){
        System.out.print("Nome: ");
        String nome = input.nextLine().trim();

        System.out.print("Curso ");
        String curso = input.nextLine().trim();

        System.out.print("Telefone: ");
        String telefone = input.nextLine().trim();

        String matricula = Validacao_Matricula(lista, input);
            
        Aluno novo = new Aluno(nome,matricula,curso,telefone);
        lista.add(novo);

    }

    
    static void Listar(ArrayList<Aluno> lista){
        for(Aluno aluno : lista){
            System.out.println(aluno);
        }
    }
    static void Listar(Aluno aluno){
        if(aluno == null){
            return;
        }
        else{
        System.out.println(aluno);
        }
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        ArrayList<Aluno> lista = new ArrayList<Aluno>();
        
        while (true){
            System.out.println("==========================================================");
            System.out.println("     SECRETARIA DO RENAN            ");
            System.out.println("==========================================================");
            System.out.println("[1] Cadastrar Aluno");
            System.out.println("[2] Listar Alunos");
            System.out.println("[3] Buscar Aluno");
            System.out.println("[4] Atualizar dados do Aluno");
            System.out.println("[5] Excluir Aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = input.nextLine().trim();

            if (opcao.equals("0")){System.out.println("Secretaria fechada. Ate a proxima!"); break;}
            else if(opcao.equals("1")){cadastrar(lista,input);}
            else if(opcao.equals("2")){Listar(lista);}
            else if(opcao.equals("3")){Listar(Busca(lista,input));}
            else if(opcao.equals("4")){Atualizar(Busca(lista, input),input,lista);}
            else if(opcao.equals("5")){Delet(Busca(lista, input),input,lista);}
            else if(opcao.equals("6")){Relatorio(lista,input);}
            else{System.out.println("Opção invalida! as opções são apenas 1, 2, 3, 4, 5 e 6 !!!");}
        }
    }
}