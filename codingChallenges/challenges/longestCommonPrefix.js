

const longString = (arrayStr) => {
    console.log(arrayStr)
    let str = ""
    let counter = 0



        while(counter < arrayStr[0].length){
            let char = arrayStr[0][counter] 
            console.log('char', char)
            

            for(let i = 1; i < arrayStr.length; i++ ){
                if(counter >= arrayStr[i].length || arrayStr[i][counter] !== char){
                    return str

                }
            }

            str += char
            counter += 1

        } 
  
   
        
        

   
}

console.log(longString(["flower", "flow", "flight"]))

