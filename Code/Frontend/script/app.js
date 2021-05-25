'use strict';

const lanIP = `${window.location.hostname}:5000`;
const socket = io(lanIP);

//#region ***  DOM references ***
let htmlFotodiodeBoven, htmlFotodiodeOnder, htmlBtnCreateValues;
//#endregion

//#region ***  Callback-Visualisation - show___ ***
const showValueFotodiode = function(jsonObject){
    console.log("fotodiodes");
    console.log(jsonObject);
    htmlFotodiodeBoven.value = jsonObject;
}
// const showValueFotodiode1 = function(jsonObject){
//     console.log("fotodiode1");
//     console.log(jsonObject);
//     htmlFotodiodeOnder.value = jsonObject;
// }
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***
//#endregion

//#region ***  Data Access - get___ ***
const getValuePhotodiode = function(id){
    console.log("get photodiodes");
    handleData(`http://127.0.0.1:5000/api/v1/fotodiode/${id}`, showValueFotodiode);
}

// const getValue1 = function(id){
//     console.log("value1");
//     handleData('http://127.0.0.1:5000/api/v1/fotodiode1', showValueFotodiode1)
// }
//#endregion

//#region ***  Event Listeners - listenTo___ ***

//#endregion
const listenToUI = function(){
    //values opvragen van meegestuurde channels
    socket.emit("F2B_getValuesPhotodiodes", {ch: [0, 1]})

    
}

const listenToSocket = function(){
    socket.on('connect', function(){
        console.log('Verbonden met socket webserver'); 
    })

    socket.on('B2F_connection', function(jsonObject){
        console.log(jsonObject)
    })

    socket.on('B2F_getValuesPhotodiodes', function(jsonObject){
        console.log(jsonObject[0])
        console.log(jsonObject[1])
        let boven = jsonObject[0]
        let onder = jsonObject[1]
        htmlFotodiodeBoven.value = boven;
        htmlFotodiodeOnder.value = onder;
        
        htmlBtnCreateValues.addEventListener('click', function(){
            //values in database steken
            socket.emit("F2B_createPhotodiodes", [htmlFotodiodeBoven.value, htmlFotodiodeOnder.value])
        })
        
    })
    
}


//#region ***  INIT / DOMContentLoaded  ***
const init = function () {
    console.log('DOM loaded');
    htmlFotodiodeBoven = document.querySelector('.js-boven');
    htmlFotodiodeOnder = document.querySelector('.js-onder');
    htmlBtnCreateValues = document.querySelector('.js-verzend-data');

    //getValuePhotodiode(0);
    //getValuePhotodiode(1);
    listenToSocket();
    listenToUI();
};
//#endregion

document.addEventListener('DOMContentLoaded', init);
