let mainloopSpeed = 1;


function mainloop(){
    if (document.getElementById('textbox').value == 'Suguru'){
        console.log("Suguru is my name");
    }
}

setInterval(mainloop, mainloopSpeed);