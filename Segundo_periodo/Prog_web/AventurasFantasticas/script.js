const map = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,2,2],
    [2,2,2,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4,4]
] //6x10
//10 moedas (4), 7 armas (3), 5 inimigos (2), 3 buracos (1), o restante é chao (0) 

let life = 3;
let coins;
let endGame;
let posicao = map[0][0];

function resetGame() {
    life = 3;
    coins = 0;
    endGame = false;
    shuffle();
}

function shuffle() {
    for(i=0; i<1000; i++) {
        i1 = Math.floor(Math.random() * 6);
        j1 = Math.floor(Math.random() * 10);
        i2 = Math.floor(Math.random() * 6);
        j2 = Math.floor(Math.random() * 10);
        let temp = map[i1][j1];
        map[i1][j1] = map[i2][j2];
        map[i2][j2] = temp;
    }
}

function mapOnClick(indX, indY) {
    if(endGame) return;

    const mapa = document.getElementById(`mapa${indX}${indY}`);
    const type = map[indX][indY];
    map.src = getImage(type);
    update_score(type);
}

function getImage(type){
    switch (type) {
        case 0: 
            return "img/chao.JPG"
            break
        case 1: 
            return "img/buraco.JPG"
            break
        case 2: 
            return "img/inimigo.JPG"
            break
        case 3: 
            return "img/arma.JPG"
            break
        case 4: 
            return "img/moeda.JPG"
            break
    }
}

function mover(direcao) {
    switch (direcao) {
        case 'Norte':
            
        break;
      case 'Sul':
        
        break;
      case 'Leste':
        
        break;
      case 'Oeste':
        
        break;
      default:
        console.log("Direção desconhecida");
    }
  }