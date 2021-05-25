'use strict';

const backend_IP = 'http://localhost:5000';
const backend = backend_IP + '/api/v1';

//#region ***  DOM references ***
let htmlFotodiodeBoven, htmlFotodiodeOnder
//#endregion

//#region ***  Callback-Visualisation - show___ ***
const showValueFotodiode0 = function(jsonObject){
    console.log("fotodiode0")
    console.log(jsonObject);
    htmlFotodiodeBoven.value = jsonObject
}
const showValueFotodiode1 = function(jsonObject){
    console.log("fotodiode1")
    console.log(jsonObject);
    htmlFotodiodeOnder.value = jsonObject
}
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***
//#endregion

//#region ***  Data Access - get___ ***
const getValue0 = function(){
    console.log("value0")
    handleData('http://127.0.0.1:5000/api/v1/fotodiode0', showValueFotodiode0);
}

const getValue1 = function(){
    console.log("value1")
    handleData('http://127.0.0.1:5000/api/v1/fotodiode1', showValueFotodiode1)
}
//#endregion

//#region ***  Event Listeners - listenTo___ ***

//#endregion

//#region ***  INIT / DOMContentLoaded  ***
const init = function () {
    console.log('DOM loaded')
    htmlFotodiodeBoven = document.querySelector('.js-boven')
    htmlFotodiodeOnder = document.querySelector('.js-onder')

    getValue0();
    getValue1();
};
//#endregion

document.addEventListener('DOMContentLoaded', init);
