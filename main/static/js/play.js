let mainloopSpeed = 100;
//!Since javascript cannot keep up with this, I need to make it 10 milliseconds
let mainLoopAdjust = 1000 / mainloopSpeed;
let fiveSecCountdown = 5 * mainLoopAdjust;
let fortyFiveSecCountdown = 5 * mainLoopAdjust;
let lblTimer = document.getElementById('lblTimer');
let lblColour = document.getElementById('lblColour')
let run = true;
let score = 0;
let colourList = ['Yellow', 'GreenYellow', 'Green', 'SkyBlue', 'White', 'Gray', 'Orange', 'Pink', 'Magenta', 'Red', 'Purple', 'Blue', 'Black'];
let 


function mainloop(){
    if (run){
        if (document.getElementById('textbox').value == 'Suguru'){
            //*I need to research all the colors I will need in the color form
            if (fiveSecCountdown > 0)
                fiveSecFun();
            else if (fiveSecCountdown > -1 * mainLoopAdjust){
                showStart();
            }
            else if (fortyFiveSecCountdown > 0){
                fortyfiveSecFunc();
            }
            else{
                run = false;
                clearInterval(loop);
                promptFun();
            }

        }
    }
}

function fiveSecFun(){

    fiveSecCountdown -= 1;
    //?Somehow it is taking 5 seconds to change one second
    lblTimer.innerHTML = (Math.floor(fiveSecCountdown / mainLoopAdjust) + 1).toString();
    
}

function showStart(){
    fiveSecCountdown -= 1;
    lblTimer.innerHTML = "START";
}



function fortyfiveSecFunc(){
    fortyFiveSecCountdown -= 1;
    lblTimer.innerHTML = (Math.floor(fortyFiveSecCountdown / mainLoopAdjust) + 1).toString();
    
}

function promptFun(){
    let bringhome = confirm(`Your score is ${score}. Click 'OK' to return to homepage.`)
    if (bringhome == true){
        console.log("Bring to homepage");
    }
}

//!Javascript cannot keep up with the speed
let loop = setInterval(mainloop, mainloopSpeed);