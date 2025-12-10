"use strict";
{
    function show() {
        console.log("ok")
    }
}

show();

function hide() {
    function stealth() {
        console.log("stealth")
    }

    return {
        stealth
    }
}

const {stealth} = hide();

stealth();