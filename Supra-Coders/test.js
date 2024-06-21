function myFunction(){
    // Use the below methods in your code (you will need to change the passed in parameters)
    // Hint: the newline character used in this test is \n
    //Reads an input file and returns the contents as a string
    //let inputFile = fs.readFileSync(fileName)
    let names = [ 'michael smith', 'john doe', 'jane doe', 'kim brown' ]
    let capitalNames = []
    let outputNames = ''
    for (let i = 0; i < names.length; i++) {

        let letters = names[i].split('')

        let spaceIndex = letters.indexOf(' ')

        let lastNameIndex = spaceIndex + 1

        letters[0] = letters[0].toUpperCase()

        letters[lastNameIndex] = letters[lastNameIndex].toUpperCase()
        
        capitalNames.push(letters.join(''))
    }
    capitalNames = capitalNames.join('\n')
    console.log(capitalNames)
}
myFunction()
