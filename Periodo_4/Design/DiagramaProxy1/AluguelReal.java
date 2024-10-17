package aluguel;

public class AluguelReal implements Aluguel{
    private Usuario usuario;
    private Item item;
    private boolean pagamento;
    private boolean devolvido;

    public Usuario getUsuario(){
        return this.usuario;
    }

    public Item getItem(){
        return this.item;
    }
    public boolean pagar(){
        this.pagamento = true;
    }
    public boolean devolverItem(){
        this.devolvido = true;
    }
}