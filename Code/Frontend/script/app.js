'use strict';

const lanIP = `${window.location.hostname}:5000`;
const socket = io(lanIP);

//#region ***  DOM references ***
let htmlHome, htmlData, htmlSettings, htmlAbout, htmlUserManuals;
let htmlFotodiodeBoven, htmlFotodiodeOnder, htmlBtnCreateValues, htmlToggleNav, htmlBtnFeedManually;
let htmlTemp, htmlWaterlevel;
//#endregion

//#region ***  Callback-Visualisation - show___ ***
const showValueFotodiode = function(jsonObject){
    console.log("fotodiodes");
    console.log(jsonObject);
    htmlFotodiodeBoven.value = jsonObject;
}
//#endregion

//#region ***  Event Listeners - listenTo___ ***
const listenToClickFeedManually = function(){
    htmlBtnFeedManually.addEventListener('click', function(){
        console.log("Feed manually")
        document.querySelector("body").classList.toggle("c-modal");
    })
}
//#endregion

//#region ***  UI Listeners - listenTo___ ***
const listenToUI = function(){
    toggleNav();

    //values opvragen van meegestuurde channels
    //socket.emit("F2B_getValuesPhotodiodes", {ch: [0, 1]});

    /***index.html***/
    //watertemp opvragen
    socket.emit("F2B_getWaterTemp", "get watertemp");

    //watercapaciteit opvragen
    // socket.emit("F2B_getCapacity", "get capacity container");


    /***Analysis.html***/
    //get all data
    const getDataFromDb = function(){
        socket.emit("F2B_getAllData", "get data");
    }
    
    
}

const listenToSocket = function(){
    socket.on('connect', function(){
        console.log('Verbonden met socket webserver'); 
    })

    socket.on('B2F_connection', function(jsonObject){
        console.log(jsonObject)
    })

    // socket.on('B2F_getValuesPhotodiodes', function(jsonObject){
    //     console.log(jsonObject[0])
    //     console.log(jsonObject[1])
    //     let boven = jsonObject[0]
    //     let onder = jsonObject[1]
    //     htmlFotodiodeBoven.value = boven;
    //     htmlFotodiodeOnder.value = onder;
        
    //     htmlBtnCreateValues.addEventListener('click', function(){
    //         //values in database steken
    //         socket.emit("F2B_createPhotodiodes", [htmlFotodiodeBoven.value, htmlFotodiodeOnder.value])
    //     })
        
    // })

    socket.on('B2F_value_watertemp', function(jsonObject){
        console.log(jsonObject.temp)
        let html = `<p>${jsonObject.temp}°C</p>`;
        htmlTemp.innerHTML = html;
    })
    
    // socket.on('B2F_value_capacity', function(jsonObject){
    //     console.log(jsonObject.level)
    //     let html = `<p>${jsonObject.level}°C</p>`;
    //     htmlWaterlevel.innerHTML = html;
    // })
}
//#endregion

const toggleNav = function(){
    for (let i = 0; i < htmlToggleNav.length; i++) {
        htmlToggleNav[i].addEventListener("click", function() {
            document.querySelector("body").classList.toggle("has-mobile-nav");
        })
    }
}

//#region ***  INIT / DOMContentLoaded  ***
const init = function () {
    console.log('DOM loaded');
    htmlFotodiodeBoven = document.querySelector('.js-boven');
    htmlFotodiodeOnder = document.querySelector('.js-onder');
    htmlBtnCreateValues = document.querySelector('.js-verzend-data');

    htmlToggleNav = document.querySelectorAll(".js-toggle-nav");

    htmlHome = document.querySelectorAll(".js-home");
    htmlData = document.querySelectorAll(".js-data");
    htmlSettings = document.querySelectorAll(".js-settings");
    htmlAbout = document.querySelectorAll(".js-about");
    htmlUserManuals = document.querySelectorAll(".js-usermanuals");

    htmlTemp = document.querySelector('.js-watertemp');
    htmlWaterlevel = document.querySelector('.js-waterlevel');
    htmlBtnFeedManually = document.querySelector('.js-btn-feedmanually');
    
    
    listenToSocket();
    listenToUI();

    if(htmlHome){
        listenToClickFeedManually();
    }

    if(htmlData){
        console.log("on data page")
        getDataFromDb()
    }

};
//#endregion

document.addEventListener('DOMContentLoaded', init);
