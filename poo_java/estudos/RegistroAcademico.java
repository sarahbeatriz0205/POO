package poo_java.estudos;

// aqui eu to tratando dados de data como string, 
// mas não acho que seja recomendado considerando os futuros tratamentos de erro de um sistema desse

public class RegistroAcademico{
    String nomeDoAluno, matricula, dataDeNascimento, anoDeMatricula;
    int ehBolsista;

    // Construtor
    public RegistroAcademico(String nome, String numeroMatricula, String nascimentoAluno, String anoMatricula, int Bolsista){
        this.nomeDoAluno = nome;
        this.matricula = numeroMatricula;
        this.dataDeNascimento = nascimentoAluno;
        this.anoDeMatricula = anoMatricula;
        this.ehBolsista = Bolsista;
    }

    public double calculaMensalidade(int bolsa){
        double mensalidade = 400;
        if (this.ehBolsista == 1){
            mensalidade = mensalidade / 2;
        }
        return mensalidade;
    }

    public void mostraRegistro(){
        System.out.println("=== Registro do aluno(a) " + this.nomeDoAluno + " ===");
        System.out.println("Nome do aluno: " + this.nomeDoAluno);
        System.out.println("Número da matrícula: " + this.matricula);
        System.out.println("Ano de nascimento: " + this.dataDeNascimento);
        System.out.println("Ano da matrícula: " + this.anoDeMatricula);
        if (this.ehBolsista == 1){ System.out.println("É bolsista? Sim");}
        else{System.out.println("É bolsista? Não");}
    }
}