package poo_java.estudos;

public class HoraAproximada{
    int hora = 0;
    int minutos = 0;

    public HoraAproximada(int horas, int minuto){
        this.hora = horas;
        this.minutos = minuto;
    }

    public boolean horaEhValida(){
        if ((this.hora >=0) && (this.hora <= 23) && (this.minutos >= 0) && (this.minutos <= 59)){
            System.out.println("Hora válida!");
            return true;
        }
        else{
            System.out.println("Erro! Hora inválida.");
            return false;
        }
    }

    public void mostraHora(){
        if (horaEhValida()){
            String horaFormatada = String.format("%02d", this.hora);
            String minutoFormatado = String.format("%02d", this.minutos);
            System.out.println("Horário inicializado: " + horaFormatada + ":" + minutoFormatado);
        }
        else{

        }
        
    }
}