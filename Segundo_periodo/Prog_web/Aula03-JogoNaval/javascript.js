function tabela() {
    for(i=0; i<5; i++){
        document.write("<tr>")
        for(j=0; j<8; j++) {
            document.write(`<td width=50 onclick='shipOnClick(${i}, ${j})'><img id='ship${i}${j}' src='img/capa.png'></td>`)
        }
    }
}
function shipOnClick(i,j){
    alert(`${i}${j}`);
    // i1= Math.floor(Math.random() * 5);
    // j1= Math.floor(Math.random() * 8);
    // i2= Math.floor(Math.random() * 5);
    // j2= Math.floor(Math.random() * 8);
}
function ship(){
    const type = ships[indX][indY];
    ship.src = getImage(type);
}
function score(){
    const scoreboard = document.getElementsById("divScoreboard");
    scoreboard.innerHTML = "Pontos: " + points + " - Vidas: " + life;
}
let map = [
    [0,0,0,1,2,0,0,2],
    [1,0,0,0,0,2,0,0],
    [0,0,2,1,0,1,0,0],
    [0,2,1,2,0,0,0,1],
    [2,0,0,0,0,1,2,0]
]