// Javascript

let state = {side:"none" , front:"none"};

// For side buttons
function l_rel(){
    state.side = "none";
    send_status();
}

function l_pre(){
    state.side = "L";
    send_status();
}

function r_rel(){
    state.side = "none";
    send_status();
}

function r_pre(){
    state.side = "R";
    send_status();
}

// For front buttons

function u_rel(){
    state.front = "none";
    send_status();
}

function u_pre(){
    state.front = "U";
    send_status();
}

function d_rel(){
    state.front = "none";
    send_status();
}

function d_pre(){
    state.front = "D";
    send_status();
}

// POST request

function send_status(){
    $.ajax({
        type : 'POST',
        url : '/status_update',
        contentType: 'application/json;charset=UTF-8',
        data : JSON.stringify(state),
        success : ()=>{
            //console.log("sent btn update", state);
        },
        error : function(error){console.log(error);}
    });
}

