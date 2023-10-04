
board1 =[[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]


    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

    let arr = []
    let subox = []
         
    // row and column
            for (let i = 0; i < board.length; i++){
                for (let j = 0; j < board.length; j++){
                    if (board[i][j] == '.') {
                        board[i][j] = 0
                        //console.log(board[i][j])
                    }
                    else {
                        board[i][j] = parseInt(board[i][j])
                        //console.log(board[i][j])
                    }

                    
                    
                }

                const Row = board[i]
                const column = board.map((row=> {
                    if (row[i] == '.') {
                        return 0
                    }
                    else {
                        return parseInt(row[i])
                }
                }))
                //console.log('Row:', Row);
                //console.log('column:', column);

                let filterRow = Row.filter((value) => value != 0)

                let filterColumn = column.filter((value) => value != 0)

                //console.log('col:', filterColumn);

                const setRow = new Set(filterRow)
                const setColumn = new Set(filterColumn)

                //console.log('setcol:', setColumn);

                if( setRow.size === filterRow.length && setColumn.size === filterColumn.length){
                    //console.log('is a sudoku')
                    arr.push(true)
                }else{
                    //console.log('not a sudoku')
                    arr.push(false)
                }
            }


            //subgrid
            for (let i = 0; i< 9; i+=3){
                for (let j = 0; j < 9; j+=3){
                    let subgrid = [];
                    for (let k = i; k < i+3; k++){
                        for (let l = j; l < j+3; l++){
                            subgrid.push(board[k][l])
                        }

                        subox.push(subgrid)
                    }
                }


            let subgridfilter = subox.map((sublist) => 
                sublist.filter(value => value !== 0))
        
            let subgridSet = subgridfilter.map((sublist) => new Set(sublist))

            let validSubgrid = subgridSet.every((sublist) => sublist.size === subgridfilter.length)

            if(validSubgrid){
                arr.push(true)
            }else{
                arr.push(false)
            }

            }


            
            //console.log(subox)
            //console.log('subfilter', subgridfilter)
            //console.log('subSet', subgridSet)


            


            if(arr.includes(false)){
                console.log('not a sudoku')
                return false
            }else{
                console.log('is a sudoku')
                return true
            }
         

            


        