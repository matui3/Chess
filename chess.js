const body = document.querySelector('body')

const grid = document.createElement('div')
grid.classList.add('grid')
body.appendChild(grid)

const rows = 8;
const columns = 8;

let gridArray = []

for (let i = 0; i < rows; i++) {
    const gridRow = []
    for (let j = 0; j < columns; j++) {
        const squares = document.createElement('div');
        grid.appendChild(squares)
        squares.classList.add('square')
        
        if (i % 2 == 0) {
            squares.classList.add('erows')
        } else {
            squares.classList.add('orows')
        }
        gridRow.push(squares)
    }
    gridArray.push(gridRow);
}
console.log(gridArray)

for (let i = 0; i < gridArray.length; i++) {
    for (let j = 0; j < gridArray[i].length; j++) {
        if (i < 2) {
            let piece = new Piece("exists", "white")
            let div = gridArray[i][j]
            console.log(div)
            div.appendChild(piece)
        } else if (i > 6) {
            let piece = new Piece("exists", "black")
            let div = gridArray[i][j]
            div.appendChild(piece)
        }
    }
}

// create 64 tile objects


// place pieces in center of object, add to an array of tiles



