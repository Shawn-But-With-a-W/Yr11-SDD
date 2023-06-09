function floodAdjacent(col, row) {
    let flooded = false;
    if ((col+1 <= userSettings.size) && (grid[col+1][row].Flood)){
        flooded = true;
    }
    if ((col-1 >= 0) && (grid[col-1][row].Flood)){
        flooded = true;
    }
    if ((row+1 <= 0) && (grid[col][row+1].Flood)){
        flooded = true;
    }
    if ((row-1 >= 0) && (grid[col][row-1].Flood)){
        flooded = true;
    }

    return flooded;
}