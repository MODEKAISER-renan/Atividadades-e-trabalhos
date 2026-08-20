import java.util.ArrayList;

class Chamados{

        private Double numero;
        private String descricao;
        private int prioridade;

        public Chamados(Double numero,String descricao,int prioridade){
            setNumero(numero);
            setDescricao(descricao);
            setPrioridade(prioridade);

        }
        public void setNumero(Double numero){
            if (numero != null && numero >= 0){ this.numero = numero;}
            else{System.out.println("Dado invalido, erro 1");}
        }
        public void setDescricao(String descricao){
            if (descricao != null && !descricao.isBlank()){ this.descricao = descricao;}
            else{System.out.println("Dado invalido, erro 2");}
        }
        public void setPrioridade(int prioridade){
            if (prioridade >= 0){ this.prioridade = prioridade;}
            else{System.out.println("Dado invalido, erro 3");}
        }
        public Double getNumero(){ return numero;}
        public String getDescricao(){ return descricao;}
        public int getPrioridade(){ return prioridade;}
    }
    

public class SysControl_v2_0 {

    static void Listar_Chamadas(ArrayList<Chamados> Chamadas){
        for(Chamados objeto : Chamadas){
            System.out.println("|Número do chamado: " + objeto.getNumero() + "\n|Descrição:" + objeto.getDescricao() + "\n|Prioridade do chamado: " + objeto.getPrioridade());

            }
    }

    public static void main(String[] args){
        
        ArrayList<Chamados> Lista_de_Chamadas = new ArrayList<>();

        Lista_de_Chamadas.add(new Chamados(1.0,"ta pegando fogo bicho", 10));

        Listar_Chamadas(Lista_de_Chamadas);


        System.exit(0);
    }
    
}

// Chamdo [número(positivo),descrição(não pode ser vazia),prioridade(valida),aberto]
//1 Criar objeto, 2 criar atributo vazio em campo obrigatorio (com resposta adequada), 3 tentar numero negativo (alteração recusada), 4 Executar um cmportamento permitido, 5Executar comportamento impossivel (falhar e retornar).
// 1	Criação do projeto e da classe da entidade.
// 2	Atributos privados e construtor.
// 3	Getters, setters e validações.
// 4	Métodos de comportamento.
// 5	Classe Main e casos de teste.
// 6	Correções após o checkpoint e README.