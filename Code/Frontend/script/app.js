'use strict';

const lanIP = `${window.location.hostname}:5000`;
const socket = io(lanIP);

//#region ***  DOM references ***
let htmlHeader;
let htmlHome, htmlAnalysis, htmlSettings, htmlAbout, htmlUserManuals;
let htmlFotodiodeBoven, htmlFotodiodeOnder, htmlBtnCreateValues, htmlToggleNav, htmlBtnFeedManually;
let htmlCapacity, htmlTemp, htmlWaterlevel, htmlInfoMessage;
let htmlBar, htmlBars;
let htmlTable, htmlTableDatetime, htmlTableCapacity, htmlTableLevelTemp;
let htmlBtnSave, htmlGrams, htmlTime, htmlStateSpeaker;

let value_watertemp, value_waterlevel, value_capacity;
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
        //document.querySelector("body").classList.toggle("c-modal");
        socket.emit('F2B_startProcess')

        console.log("values: ")
        console.log("watertemp: ", value_watertemp)
        console.log("waterlevel: ", value_waterlevel)
        console.log("capacity: ", value_capacity)
               
        //toevoegen aan db
        socket.emit("F2B_addToDb", {"watertemp" : value_watertemp, "waterlevel": value_waterlevel, "capacity": value_capacity});
    })
}

const listenToClickSave = function(){
    //als de pagina geladen is
    let previousGrams = htmlGrams.value
    let previousTime = htmlTime.value
    let previousStateSpeaker = htmlStateSpeaker.checked
    console.log(previousGrams)
    console.log(previousTime)
    console.log(previousStateSpeaker)

    htmlBtnSave.addEventListener('click', function(){
        console.log('save');
        let grams = htmlGrams.value;
        let time = htmlTime.value;
        let stateSpeaker = htmlStateSpeaker.checked;
        console.log(grams);
        console.log(time);
        console.log(stateSpeaker);

        if (previousGrams != grams){
            socket.emit("F2B_grams", grams);
        }
        if (previousTime != time){
            socket.emit("F2B_time", time);
        }
        if (previousStateSpeaker != stateSpeaker){
            socket.emit("F2B_stateSpeaker", stateSpeaker)
        }
    })
}
//#endregion

//#region ***  UI Listeners - listenTo___ ***
const listenToUI = function(){
    console.log("listentoui")
    toggleNav();

    window.onscroll = function(){
        let sticky = htmlHeader.offsetTop;
        if (window.pageYOffset > sticky){
            htmlHeader.classList.add('.c-header--fixed');
        } else {
            htmlHeader.classList.remove('.c-header--fixed');
        }
    }

    //values opvragen van meegestuurde channels
    //socket.emit("F2B_getValuesPhotodiodes", {ch: [0, 1]});

    if (htmlHome){
        /***index.html***/
        //watercapaciteit opvragen
        socket.emit("F2B_getCapacity", "get capacity container");

        //watertemp opvragen
        socket.emit("F2B_getWaterTemp", "get watertemp");

        //waterlevel opvragen
        socket.emit("F2B_getWaterlevel", "get waterlevel");
        
        
    }

    if (htmlAnalysis){
        //data in database opvragen
        socket.emit("F2B_getDataFromDb", "get data");
    }
    


    
    
    
}
// // ***Analysis.html***/
//     //get all data
// const getDataFromDb = function(){
//     socket.emit("F2B_getAllData", "get data");
// }


const listenToSocket = function(){
        
    socket.on('connect', function(){
        console.log('Verbonden met socket webserver'); 
    })

    // socket.on('B2F_connection', function(jsonObject){
    //     console.log(jsonObject)
    // })

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
    if (htmlHome){
        socket.on('B2F_value_capacity', function(jsonObject){
            console.log(jsonObject.capacity)
            value_capacity = jsonObject.capacity
            let html = `${value_capacity}%`;
            htmlCapacity.innerHTML = html;

            // for(const bar of htmlBars){
            //     console.log(bar)
            // }

            const removeCSSClass = function(num, action, status){
                let CSSclass = null
                if (status == "empty"){
                    CSSclass = "c-status-bar--empty"
                }else if(status == "almost"){
                    CSSclass = "c-status-bar--almost-empty"
                }else if(status == "full"){
                    CSSclass = "c-status-bar--full"
                }

                if (num == "all"){
                    if (action == "remove"){
                        for (let i =0 ; i <= 9; i++){
                        htmlBars[i].classList.remove("c-status-bar--empty");
                        htmlBars[i].classList.remove("c-status-bar--almost-empty");
                        htmlBars[i].classList.remove("c-status-bar--full");
                        }
                    }else if (action == "add"){
                        for (let i =0 ; i <= 9; i++){
                            htmlBars[i].classList.add("c-status-bar--empty");
                            htmlBars[i].classList.add("c-status-bar--almost-empty");
                            htmlBars[i].classList.add("c-status-bar--full");
                            }
                    }
                    
                    
                }else{
                    if (action == "add"){
                        htmlBars[num].classList.add(CSSclass);
                    } else if (action == "remove"){
                        htmlBars[num].classList.remove(CSSclass);
                    } 
                }

            }

            if (value_capacity > 0 && value_capacity <= 10){
                console.log("container empty");
                htmlBars[9].classList.add('c-status-bar--empty');
                htmlBars[9].classList.remove('c-status-bar--almost-empty');
                htmlBars[9].classList.remove('c-status-bar--full');
                htmlBars[8].classList.remove('c-status-bar--empty');
                htmlBars[8].classList.remove('c-status-bar--almost-empty');
                htmlBars[8].classList.remove('c-status-bar--full');
                htmlBars[7].classList.remove('c-status-bar--almost-empty');
                htmlBars[7].classList.remove('c-status-bar--full');
                htmlBars[6].classList.remove('c-status-bar--almost-empty');
                htmlBars[6].classList.remove('c-status-bar--full');
                htmlBars[5].classList.remove('c-status-bar--almost-empty');
                htmlBars[5].classList.remove('c-status-bar--full');
                htmlBars[4].classList.remove('c-status-bar--full');
                htmlBars[3].classList.remove('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                //removeCSSClass("all", null, null);
                htmlInfoMessage.innerHTML = `The container is almost empty!`;

            } else if (value_capacity > 0 && value_capacity <= 20){
                htmlBars[9].classList.add('c-status-bar--empty');
                htmlBars[8].classList.add('c-status-bar--empty');
                htmlBars[7].classList.remove('c-status-bar--almost-empty');
                htmlBars[7].classList.remove('c-status-bar--full');
                htmlBars[6].classList.remove('c-status-bar--almost-empty');
                htmlBars[6].classList.remove('c-status-bar--full');
                htmlBars[5].classList.remove('c-status-bar--almost-empty');
                htmlBars[5].classList.remove('c-status-bar--full');
                htmlBars[4].classList.remove('c-status-bar--full');
                htmlBars[3].classList.remove('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is almost empty!`;
                
            } else if (value_capacity > 0 && value_capacity <= 30){
                htmlBars[9].classList.add('c-status-bar--almost-empty');
                htmlBars[8].classList.add('c-status-bar--almost-empty');
                htmlBars[7].classList.add('c-status-bar--almost-empty');
                htmlBars[6].classList.remove('c-status-bar--almost-empty');
                htmlBars[6].classList.remove('c-status-bar--full');
                htmlBars[5].classList.remove('c-status-bar--almost-empty');
                htmlBars[5].classList.remove('c-status-bar--full');
                htmlBars[4].classList.remove('c-status-bar--full');
                htmlBars[3].classList.remove('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is half empty`;
                
            } else if (value_capacity > 0 && value_capacity <= 40){
                htmlBars[9].classList.add('c-status-bar--almost-empty');
                htmlBars[8].classList.add('c-status-bar--almost-empty');
                htmlBars[7].classList.add('c-status-bar--almost-empty');
                htmlBars[6].classList.add('c-status-bar--almost-empty');
                htmlBars[5].classList.remove('c-status-bar--almost-empty');
                htmlBars[5].classList.remove('c-status-bar--full');
                htmlBars[4].classList.remove('c-status-bar--full');
                htmlBars[3].classList.remove('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is half empty`;
                
            } else if (value_capacity > 0 && value_capacity <= 50){
                htmlBars[9].classList.add('c-status-bar--almost-empty');
                htmlBars[8].classList.add('c-status-bar--almost-empty');
                htmlBars[7].classList.add('c-status-bar--almost-empty');
                htmlBars[6].classList.add('c-status-bar--almost-empty');
                htmlBars[5].classList.add('c-status-bar--almost-empty');
                htmlBars[5].classList.remove('c-status-bar--full');
                htmlBars[4].classList.remove('c-status-bar--full');
                htmlBars[3].classList.remove('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is half empty`;
                
            } else if (value_capacity > 50 && value_capacity <= 60){
                htmlBars[9].classList.add('c-status-bar--full');
                htmlBars[8].classList.add('c-status-bar--full');
                htmlBars[7].classList.add('c-status-bar--full');
                htmlBars[6].classList.add('c-status-bar--full');
                htmlBars[5].classList.add('c-status-bar--full');
                htmlBars[4].classList.add('c-status-bar--full');
                htmlBars[3].classList.remove('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is full`;
                
            } else if (value_capacity > 50 && value_capacity <= 70){
                htmlBars[9].classList.add('c-status-bar--full');
                htmlBars[8].classList.add('c-status-bar--full');
                htmlBars[7].classList.add('c-status-bar--full');
                htmlBars[6].classList.add('c-status-bar--full');
                htmlBars[5].classList.add('c-status-bar--full');
                htmlBars[4].classList.add('c-status-bar--full');
                htmlBars[3].classList.add('c-status-bar--full');
                htmlBars[2].classList.remove('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is full`;
                
            } else if (value_capacity > 50 && value_capacity <= 80){
                htmlBars[9].classList.add('c-status-bar--full');
                htmlBars[8].classList.add('c-status-bar--full');
                htmlBars[7].classList.add('c-status-bar--full');
                htmlBars[6].classList.add('c-status-bar--full');
                htmlBars[5].classList.add('c-status-bar--full');
                htmlBars[4].classList.add('c-status-bar--full');
                htmlBars[3].classList.add('c-status-bar--full');
                htmlBars[2].classList.add('c-status-bar--full');
                htmlBars[1].classList.remove('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is full`;
                
            } else if (value_capacity > 50 && value_capacity <= 90){
                // for (let i = 0; i<= 9; i++){
                //     htmlBars[i].classList.add('c-status-bar--full');
                // }
                htmlBars[9].classList.add('c-status-bar--full');
                htmlBars[8].classList.add('c-status-bar--full');
                htmlBars[7].classList.add('c-status-bar--full');
                htmlBars[6].classList.add('c-status-bar--full');
                htmlBars[5].classList.add('c-status-bar--full');
                htmlBars[4].classList.add('c-status-bar--full');
                htmlBars[3].classList.add('c-status-bar--full');
                htmlBars[2].classList.add('c-status-bar--full');
                htmlBars[1].classList.add('c-status-bar--full');
                htmlBars[0].classList.remove('c-status-bar--full');
                htmlInfoMessage.innerHTML = `The container is full`;
                
            } else if (value_capacity > 50 && value_capacity <= 100){
                for (let bar of htmlBars){
                    bar.classList.add('c-status-bar--full');
                }
                htmlInfoMessage.innerHTML = `The container is full`;
                
            }
        })

        socket.on('B2F_value_watertemp', function(jsonObject){
            console.log(jsonObject);
            value_watertemp = jsonObject;
            console.log(value_watertemp);
            let html = `${jsonObject}°C`;
            htmlTemp.innerHTML = html;
        })
        
        socket.on('B2F_value_waterlevel', function(jsonObject){
            value_waterlevel = jsonObject.level
            console.log(value_waterlevel)
            let html = `${value_waterlevel}%`;
            htmlWaterlevel.innerHTML = html;
        })

        
     
    }    

    if (htmlAnalysis){
        socket.on('B2F_DataFromDb', function(jsonObject){
            // console.log(jsonObject.capacity);
            // console.log(jsonObject.watertemp);
            // console.log(jsonObject.waterlevel);
            
            // let html = '';
            // for (let row of htmlTable){
            //     html += `<td class="c-table__item js-table-datetime">25/05/21<br>19:00</td>
            //     <td class="c-table__item js-table-capacity">${jsonObject.capacity}%</td>
            //     <td class="c-table__item js-table-level-temp">${jsonObject.waterlevel}%<br>${jsonObject.watertemp}°C</td>`;
            // }

            // htmlTable.innerHTML = html;
            console.log("Frontend")
            console.log(jsonObject);
        })
    }
    
}
//#endregion

const toggleNav = function(){
    console.log("toggle nav")
    for (let i = 0; i < htmlToggleNav.length; i++) {
        htmlToggleNav[i].addEventListener("click", function() {
            console.log("clicked")
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

    htmlHeader = document.querySelector('.js-header');
    htmlToggleNav = document.querySelectorAll(".js-toggle-nav");

    htmlHome = document.querySelector('.js-home');
    htmlAnalysis = document.querySelector('.js-data');
    htmlSettings = document.querySelector('.js-settings');
    htmlAbout = document.querySelector('.js-about');
    htmlUserManuals = document.querySelector('.js-usermanuals');

    htmlCapacity = document.querySelector('.js-status-percentage')
    htmlTemp = document.querySelector('.js-watertemp');
    htmlWaterlevel = document.querySelector('.js-waterlevel');
    htmlInfoMessage = document.querySelector('.js-status-message')
    htmlBtnFeedManually = document.querySelector('.js-btn-feedmanually');
    htmlBtnSave = document.querySelector('.js-btn-save');
    htmlGrams = document.querySelector('.js-grams');
    htmlTime = document.querySelector('.js-time');
    htmlStateSpeaker = document.querySelector('.js-state-speaker')

    htmlBar = document.querySelector('.js-status-bar');
    htmlBars = document.querySelectorAll('.js-bar');

    htmlTable = document.querySelectorAll('.js-table');
    htmlTableDatetime = document.querySelector('.js-table-datetime');
    htmlTableCapacity = document.querySelector('.js-table-capacity');
    htmlTableLevelTemp = document.querySelector('.js-tabel-level-temp');
    
    
    listenToSocket();
    listenToUI();

    if(htmlHome){
        console.log("on home page")
        listenToClickFeedManually();
    }

    // if(htmlData){
    //     console.log("on data page")
    //     getDataFromDb()
    // }

    if (htmlSettings){
        console.log("on settings page")
        listenToClickSave();
    }

};
//#endregion

document.addEventListener('DOMContentLoaded', init);
