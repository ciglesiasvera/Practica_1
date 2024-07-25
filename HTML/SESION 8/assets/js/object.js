let backpack = {
//Object properties
color: 'black',    
size: '9in',
pocketsQuantity: 2,
zippersQuantity: 2,
//Object methods
open() {
    console.log('The Backpack is Open')
},
close() {
    console.log('The Backpack is Closed')
}
};
console.log(backpack);
//Access to objects properties
console.log(backpack.color);
console.log(backpack.size);
console.log(backpack.pocketsQuantity);
console.log(backpack.zippersQuantity);
//Access to objects methods
backpack.open();
backpack.close();