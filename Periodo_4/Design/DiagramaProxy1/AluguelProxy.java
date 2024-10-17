package aluguel;

public class AluguelProxy implements Aluguel{
    private AluguelReal aluguelReal;
    private String autenticacao;

    private boolean verificacaoPermissao(){
        return "usuario autorizado".equals(this.autenticacao);
    }

    public Usuario getUsuario(){
        return this.aluguelReal.getUsuario();
    }

    public Item getItem(){
        return this.aluguelReal.getItem();
    }

    public boolean pagar(){
        return this.aluguelReal.pagar();
    }

    public boolean devolverItem(){
        return this.aluguelReal.devolverItem();
    }

}