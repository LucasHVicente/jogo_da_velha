const PLAYERS = {
    x: 'X',
    o: 'O',
    none: ' '
}

Object.freeze(PLAYERS)

const GAME = [
            PLAYERS.none,PLAYERS.none,PLAYERS.none,
            PLAYERS.none,PLAYERS.none,PLAYERS.none,
            PLAYERS.none,PLAYERS.none,PLAYERS.none
        ]

let CURRENT_PLAYER = PLAYERS.x

// função que escreve qual o jogador ativo na tela
function drawCurrentPlayer(player){
    const currentPlayer = document.getElementById('player')
    currentPlayer.innerText = `Jogador atual: ${player}`
}

// função que verifica se o slot está vazio
function isSlotEmpty(position){
    const slotValue = GAME[position]
    return slotValue === PLAYERS.none
}

// função para preencher o slot com o símbolo do jogador
function drawPlayerInSlot(player, position){
    const gameBoard = document.getElementById('jogo')

    const slot = gameBoard.children[position]
    slot.innerText = player
    GAME[position] = player
}

//função para verificar se alguem ganhou o jogo
function getGameWinner(board) {
    // array de resultados possiveis
    const gameStatus = [
        //resultados na diagonal
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
        //resultados em colunas
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        //resultados em linhas
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]]
    ]

    //retorna o primeiro resultado onde todos os slots tem o mesmo jogador
    const result = gameStatus.find(result=>{
        //compara se todos os slots pertencem ao jogador atual
        return result.every(slot=>slot===CURRENT_PLAYER)
    })
    // se todos os slots estiverem preenchidos e não tiver um vencedor da em empate
    if(board.every(slot=>slot!==PLAYERS.none) && !result ) return PLAYERS.none

    return result? CURRENT_PLAYER : false
}

// função para resetar o tabuleiro e começar uma nova partida
function resetGame() {
    CURRENT_PLAYER = PLAYERS.x
    GAME.forEach((_item, index)=>{
        GAME[index] = PLAYERS.none
    })
    drawBoard(GAME)
    console.log(CURRENT_PLAYER)
    drawCurrentPlayer(CURRENT_PLAYER)
}

//função para apresentar o jogador que venceu a partida
function announceGameWinner(player) {
    if(player===PLAYERS.none){
        alert(`Empate`)
    }else{
        alert(`O jogador ${player} venceu`)
    }
}

//função que registra o clique e seleciona o slot
function onClickSlot(position){        
    if(isSlotEmpty(position)){
        drawPlayerInSlot(CURRENT_PLAYER, position)
        const winner = getGameWinner(GAME)//caso empate Players.none
        if(Object.values(PLAYERS).includes(winner)) {
            announceGameWinner(winner)
            resetGame()
        }
        swapPlayers()
    }
}

//função que renderiza o tabuleiro com os slots clicaveis
function drawBoard(board) {
    const gameBoard = document.getElementById('jogo')
    gameBoard.innerHTML = null
    board.forEach((slotValue, position)=>{
        const slot = document.createElement('button')
        slot.addEventListener('click', ()=>onClickSlot(position))
        slot.innerText = slotValue
        gameBoard.appendChild(slot)
    })
}

// função que troca o jogador
function swapPlayers() {
    // alternativamente essa validação poderia ter sido feita dessa maneira:
    // currentPlayer = currentPlayer === PLAYERS.x ? PLAYERS.o : PLAYERS.x
    
    if(CURRENT_PLAYER === PLAYERS.x){
        CURRENT_PLAYER = PLAYERS.o
    }else{
        CURRENT_PLAYER = PLAYERS.x
    }
    drawCurrentPlayer(CURRENT_PLAYER)
}

// Coisas que ainda podem ser feitas ou correções necessárias
//TODO: quando alguem ganha a ultima jogada não renderiza
//TODO: botão para rendição
//TODO: botão para reiniciar o jogo
//TODO: placar

function init(){
    drawBoard(GAME)
    drawCurrentPlayer(CURRENT_PLAYER)
}

init()
