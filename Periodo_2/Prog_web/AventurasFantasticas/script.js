const map = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,2,2,0],
    [2,2,2,3,3,3,3,3,3,3,0],
    [4,4,4,4,4,4,4,4,4,4,0]
] //7x11
//10 moedas (4), 7 armas (3), 5 inimigos (2), 3 buracos (1), o restante é chao (0) 

let life = 3;
let arma = 0
let coins = 0;
let endGame;
let posX;
let posY;


function resetGame() {
    life = 3;
    coins = 0;
    arma = 0;
    posicao = map[4][6];
    endGame = false;
    shuffle();
}

function shuffle() {
    for(i=0; i<1000; i++) {
        i1 = Math.floor(Math.random() * 7);
        j1 = Math.floor(Math.random() * 11);
        i2 = Math.floor(Math.random() * 7);
        j2 = Math.floor(Math.random() * 11);
        let temp = map[i1][j1];
        map[i1][j1] = map[i2][j2];
        map[i2][j2] = temp;
    }
}

function mapOnClick(posY, posX) {
    if(endGame) return;

    const mapa = document.getElementById(`mapa${posX}${posY}`);
    const type = map[posX][posY];
    map.src = getImage(type);
    map.src = mover(type);
    update_score(type);
}

function getImage(type){
    switch (type) {
        case 0: 
            return "img/chao.JPG"

            break
        case 1: 
            life--;
            return "img/buraco.JPG"
            break
        case 2: 
            if(arma > 0){
                arma--;
            }
            else{
                life--;
            }
            return "img/inimigo.JPG"
            break
        case 3: 
            arma++;
            return "img/arma.JPG"
            break
        case 4: 
            coins++;
            return "img/moeda.JPG"
            break
    }
}

function mover(direcao) {
    switch (direcao) {
        case 'Norte':
            if (posX <= 0 || posX >= 10){
                alert('Não é possivel ir para o norte, o mapa acaba aqui!')
            }
            else {
                posY++;
            }
        break;
      case 'Sul':
            if (posX <= 0 || posX >= 10){
                alert('Não é possivel ir para o norte, o mapa acaba aqui!')
            }
            else{
                posY--;
            }
        break;
      case 'Leste':
            if (posY <= 0 || posY >= 6){
                alert('Não é possivel ir para o norte, o mapa acaba aqui!')
            }
            else{
                posX++;
            }
        break;
      case 'Oeste':
            if (posY <= 0 || posY >= 6){
                alert('Não é possivel ir para o norte, o mapa acaba aqui!')
            }
            else{
                posX--;
            }
        break;
      default:
        console.log("Direção desconhecida");
    }
  }