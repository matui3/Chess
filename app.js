const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

canvas.width = 1280
canvas.height = 860


c.fillStyle = '#FFFFFF'
c.fillRect(0, 0, canvas.width, canvas.height)


class Grid {
    constructor(position) {
        this.position = position;
    }

    draw() {
        c.beginPath();
        c.rect(this.position.x, this.position.y, 600, 600);
        c.stroke();
    }

}

class Tile {
    constructor(position) {
        this.position = position
    }

    draw() {
        c.fillStyle = 'black'
        c.fillRect(this.position.x, this.position.y, 50, 50)
    }
}

const tile = new Tile({
    x: 0,
    y: 0
})

console.log(tile)

tile.draw()

const grid = new Grid({
    x: 200,
    y: 200,
})

grid.draw()

console.log(grid)
