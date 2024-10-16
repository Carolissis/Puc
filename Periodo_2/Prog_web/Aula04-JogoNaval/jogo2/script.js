const ships = [

    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3,3,3,3,3]];
    
let life = 3;
let points;
let endGame;

function setarVidas(number){
    let life = number
    console.log(number)
}


function tabela(){
    for(i=0; i<8; i++) {
        document.write("<tr>")
        for(j=0; j<12; j++) {
            document.write(`<td onclick='shipOnClick(${i}, ${j})'><img id='ship${i}${j}'  src='images/back.jpg'></td>`)
        }
        document.write("</tr>")
    }
}


function resetGame() {
    life = 10;
    points = 0;
    endGame = false;
    shuffle();
}


function shuffle() {
                
    for(i=0; i<1000; i++) {
        i1 = Math.floor(Math.random() * 8);
        j1 = Math.floor(Math.random() * 12);
        i2 = Math.floor(Math.random() * 8);
        j2 = Math.floor(Math.random() * 12);
        let temp = ships[i1][j1];
        ships[i1][j1] = ships[i2][j2];
        ships[i2][j2] = temp;
    }
}


function shipOnClick(indX, indY) {
    
    if (endGame) return;
    
    const ship = document.getElementById(`ship${indX}${indY}`);
    const type = ships[indX][indY];
    ship.src = getImage(type);
    ship.src = mens(type)
    update_scoreboard(type);
}


function getImage(type) {
    switch (type) {
        case 0:
            return "images/agua.jpg";
            break;
        case 1:
            return "images/submarino.jpg";
            break;
        case 2:
            return "images/porta_avioes.jpg";
            break;
        case 3:
            return "images/navio_de_guerra.jpg";
            break;
    }
    
    return "images/back.jpg";
}

function mens(type) {
    switch (type) {
        case 0:
            return(`<img src="images/agua.jpg" alt="Agua" onclick="changeText('Deu água')">`);
            break;
        case 1:
            return(`<img src="images/submarino.jpg" alt="Sub" onclick="changeText('Você destruiu o navio!!')">`);
            break;
        case 2:
            return(`<img src="images/porta_avioes.jpg" alt="aviao" onclick="changeText('Você DETONOU o porta aviões :O')">`);
            break;
        case 3:
            return(`<img src="images/navio_de_guerra.jpg" alt="navio" onclick="changeText('Você afundou o navio!!')">`);
            break;
    }
    
    return "images/back.jpg";
}

function changeText(description) {
    const div = document.getElementById('imageDescription');
    div.textContent = description;
}

function update_scoreboard(type) {
    
    points += type;
    if (type == 0) {
        life--;
        update_scoreboard_view();
        if (life == 0) {
            alert('Você perdeuuu!!! Com '+ points +' pontos.');
            endGame = true;
        }
    }
    else {
        update_scoreboard_view();
    }
}

function update_scoreboard_view() {
    
    const scoreboard = document.getElementById("divScoreboard");
    scoreboard.innerHTML = "Pontos: " + points + " - Vidas: " + life;
}

resetGame();

function checkCheckboxState() {
    const checkbox = document.getElementById('myCheckbox');

    if (checkbox.check) {
        alert('A checkbox está marcada!');
    } else {
        alert('A checkbox não está marcada!');
    }
}