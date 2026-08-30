/*
*Diciplina: 2026-PS
*Estudante: Renan Soares da Silva
*Projeto: Aula32-projeto-secretaria
*arquivo: Aluno.java
*/

public class Aluno{

    private String nome;
    private String matricula;
    private String curso;
    private String telefone;

    public Aluno(String nome,String matricula,String curso,String telefone){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
        this.telefone = telefone;
    }

    public String getNome(){return nome;}
    public String getMatricula(){return matricula;}
    public String getCurso(){return curso;}
    public String getTelefone(){return telefone;}

    public void setNome(String nome){this.nome = nome;}
    public void setCurso(String curso){this.curso = curso;}
    public void setMatricula(String matricula){this.matricula = matricula;}
    public void setTelefone(String telefone){this.telefone = telefone;}

    public String toString(){
        return nome + " | " + matricula + " | " + curso + " | " + telefone ;
    }
    
}
