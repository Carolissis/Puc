package aluguel;

public interface Aluguel{
    Usuario getUsuario();
    Item getItem();
    boolean pagar();
    boolean devolverItem();
}