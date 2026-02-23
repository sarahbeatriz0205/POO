public class Data{
    public int dia;
    public int mes;
    public int ano;

    public boolean dataEhValida(int dia, int mes, int ano){
        if ((dia >= 1) && (dia <= 31) && (mes >= 1) && (mes <= 12)){
            return true; // data é válida
        }
        else{
            return false;
        }
    }

    public String mostraData(){
        String data = String.format("A data é: %d/%d/%d", this.dia, this.mes, this.ano);
        return data;
    }

    public void inicializaData(int dia, int mes, int ano){
        if (dataEhValida(dia, mes, ano) == true){
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
            System.out.println(mostraData());
        }
        else{
            this.dia = 0;
            this.mes = 0;
            this.ano = 0;
            System.out.println("Erro!");
        }
    }
}