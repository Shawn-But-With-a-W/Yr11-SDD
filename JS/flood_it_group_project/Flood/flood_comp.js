var canvas = document.getElementById('canvas');
var ctx = canvas.getContext("2d");
var userSettings = {size:12,colors:5,cellSize:40};
var grid = [];

function randomcolor() {
	var colors = ["#B7CECE", "#BA546D", "#EFA7A7", "#616283", "#F4F0BB", "#FADB9E", "#A2BCE0", "#DBF4A7"]
	var randIndex = Math.floor(Math.random() * userSettings.colors)
	return colors[randIndex]
	}
/*	
function randomcolor()  { 
		var colors = ["green", "purple", "red", "cyan", "peach", "yellow", "magenta", "pink"];
		var randIndex = Math.floor(Math.random() * (userSettings.colors));
		 return colors[randIndex]
}*/

function gameWin() {
 total = userSettings.size * userSettings.size;
 return countFloodedCells() == total;
}

function displayOutcome() {
    document. getElementById("Outcome").innerHTML = "congratulation!";
}

function updateSettings(){
    userSettings.colors = document.getElementById("ColorsDrop").value;
    userSettings.size = document.getElementById("SizeDrop").value;
    userSettings.cellSize = 480 / userSettings.size;
}


function advanceTurn() {
    var turns = document.getElementById("Turns").textContent;
    turns++;
    document.getElementById("Turns").innerHTML = turns;
}

// BEGIN generateGrid ()
// 		grid.length = 0
// 		FOR i = 0 TO userSettings.size STEP 1
// 			row = []
// 			FOR j = 0 TO userSettings.size STEP 1
// 				rc = randomColour()	
// 				append {color: rc, Flood: false} to row
// 			NEXT j
// 			append row to grid
// 		NEXT i
// END

function generateGrid() {
    grid.length = 0;
    for (let i = 0; i < userSettings.size; i++) {
        let row = [];
        for (let j = 0; j < userSettings.size; j++) {
            let rc = randomcolor();
            row.push({color: rc, Flood: false});
        }
        grid.push(row);
    }
}


/*
function selectcolor(event) {
  let MousePositionX = event.clientX;
  let MousePositionY = event.clientY;
  let column = Math.floor(MousePositionX / userSettings.cellSize);
  let row = Math.floor(MousePositionY / userSettings.cellSize);
  let ccolor = grid[row][column].color;

  if (ccolor !== grid[0][0].color) {
    changeGridcolor(ccolor);
    advanceTurn();
    if (gameWin()) {
      displayOutcome();
    }
  }
}

}
*/

function selectColor(Event) {
    var MousePositionX = Event.clientX - canvas.offsetLeft + window.pageXOffset;
    var MousePositionY = Event.clientY - canvas.offsetTop + window.pageYOffset;
    var column = Math.floor(MousePositionX / userSettings.cellSize);
    var row = Math.floor(MousePositionY / userSettings.cellSize);
    var ccolor = grid[row][column].color
    console.log(ccolor)
    if (ccolor != grid[0][0].color) {
        changeGridcolor(ccolor);
        expandGrid(ccolor);
        advanceTurn();
        if (gameWin()) {
            displayOutcome();
        }
    }
}

function countFloodedCells() {
        var flooded = 0;
        for (let row = 0; row < userSettings.size; row++) {
            for (let cell = 0; cell < userSettings.size; cell++) {
                if (grid[row][cell].Flood == true) {
                    flooded++;
                }
            }
        }
        return flooded;
    }


function floodAdjacent(col, row) {
    let flooded = false;
    if ((col+1 < userSettings.size) && (grid[col+1][row].Flood)){
        flooded = true;
    }
    if ((col-1 >= 0) && (grid[col-1][row].Flood)){
        flooded = true;
    }
    if ((row+1 < userSettings.size) && (grid[col][row+1].Flood)){
        flooded = true;
    }
    if ((row-1 >= 0) && (grid[col][row-1].Flood)){
        flooded = true;
    }

    return flooded;
}

/*function expandGrid(color){

	for (let row = 0; row < grid.length; row++){

		for (let col = 0; col < grid.length; col++){

			if (grid[row][col].flood == False){
				
				if (grid[row][col].color === color){

					if (isAdjacent(row,col)){
						grid[row][col].Flood = True

					}

				}


			}

		}


	}

}*/


function expandGrid(ccolor) {
    console.log("expandGrid was called");
    for (let row=0; row < grid.length; row++){
        for (let col=0; col<grid[row].length; col++){
            if (grid[row][col].Flood == false){
                if (grid[row][col].color == ccolor) {
                    if (floodAdjacent(row, col)) {
                        grid[row][col].Flood = true;
                    }
                }
            }
        }
    }
}

/*
function changeGridcolor(color){
	for (let r = 0; r < grid.length; r++ ){
		for(let c = 0; c < grid.length; c++){
			if(grid[r][c].active == true)
				grid[r][c].color = color;
		}
	
	}
}*/

function changeGridcolor(color){
			for (var row = 0; row < grid.length; row++) {
				for (var column = 0; column < grid.length; column++) {
					if (grid[row][column].Flood == true) {
						grid[row][column].color = color;
                        console.log("this grid is now" + grid[row][column].color, color);
					}
				}
			}
		}

function displayGrid(){
    for (var row = 0; row < userSettings.size; row++){
        for (var col = 0; col < userSettings.size; col++){
            let color = grid[row][col].color;
			let size = userSettings.cellSize;
			let x = col * size;
			let y = row * size;
            ctx.fillStyle = color;
            ctx.fillRect(x, y, size, size);
            ctx.strokeRect(x, y, size, size);
        }
    }
}

function initialise() {
	document.getElementById("Outcome").innerHTML = "Moves: <span id='Turns'>0</span>";
	document.getElementById("Turns").innerHTML = "0";
	
	updateSettings();
	generateGrid();
    grid[0][0].Flood = true;
	expandGrid(grid[0][0].color);
	displayGrid();
	
	document.getElementById('canvas').addEventListener("click", function(e) {
		selectColor(e),
		displayGrid()}
		);
}

initialise();
