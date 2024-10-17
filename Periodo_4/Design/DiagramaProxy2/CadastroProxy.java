package cadastro;

public class CadastroProxy implements Cadastro{
    private CadastroReal cadastroReal;
    private String autenticacao;

    private boolean verificacaoPermissao(){
        return "usuario autorizado".equals(this.autenticacao);
    }

    public void setNome(String nome){
        return this.cadastroReal.setNome(nome);
    }
    public void setEmail(String email){
        return this.cadastroReal.setEmail(email);
    }
    public void setSenha(String senha){
        return this.cadastroReal.setSenha(senha);
    }

}