
    let cat = 'rat';
    let car = 'car';
   
    let regex = /[^a-z]/gi; // only count letters
    let catReg = cat.toLowerCase().replace(regex, '').split('').sort().join('');
    let carReg = car.toLowerCase().replace(regex, '').split('').sort().join('');

    if( catReg !== carReg)
        console.log(false)
    else
        console.log(true)
    
