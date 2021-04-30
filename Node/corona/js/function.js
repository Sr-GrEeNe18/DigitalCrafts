var Positivenumbers = [5, -10, -15, 20, -25];

let PositivenewArr = Positivenumbers.filter(Positivenumbers =>{
    return Positivenumbers > 0;
})
console.log(PositivenewArr)

var numberEven = [5, 10, 15, 20, 25];
let numEvenewArr = numberEven.filter(numberEven =>{
    return numberEven % 2 == 0;
})
console.log(numEvenewArr)


var cities = [
{name: 'Los Angeles', temperature: 60.0},
{name: 'Atlanta', temperature: 52.0},
{name: 'Detriot', temperature: 48.0},
{name: 'New York', temperature: 80.0} ];

let Citiesnewarr = cities.filter(cities =>{
    return cities.temperature < 70;
})
console.log(cities)


var cities = [
    {name: 'Los Angeles', temperature: 60.0},
    {name: 'Atlanta', temperature: 52.0},
    {name: 'Detriot', temperature: 48.0},
    {name: 'New York', temperature: 80.0} ];

    let NamenewArr = cities.map(cities =>{
        return cities.name;
    })

    console.log(NamenewArr)
var people = ['Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur'];

let goodjob = people.map(people =>{
    return `good job ${people}`;
})
    console.log(goodjob)

var people = ['Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur'];

people.sort;
console.log(people)

var people = ['Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur'];

let peoplenewArr = people.sort(people =>{
    return people;
})

console.log(peoplenewArr)

let call3Times = "Hello World".repeat(3)
console.log(call3Times)



