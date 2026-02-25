package poo_java.estudos;

public class Lampada {
    public boolean estaLigada;

    public void Acende() {
        this.estaLigada = true;
    }

    public void Apaga() {
        this.estaLigada = false;
    }

    public boolean Estado() {
        if (this.estaLigada) {
            System.out.println("Está acesa!");
        } else {
            System.out.println("Está apagada!");
        }
        return this.estaLigada;
    }
}