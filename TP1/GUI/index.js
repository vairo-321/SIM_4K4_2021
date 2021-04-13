/*
    index.js

    Lógica para el cliente
*/
$(document).ready(function(){
    console.log("hello world")

    // Objecto de conexión websocket
    let socket = new WebSocket("ws://localhost:8080");

    // Hacer algo cuando se conecte al servidor ws
    socket.onopen = function(e) {
        //alert("Hello World, ws working in the client")
    }

    // Para testear si el servidor ws funciona -> borrar en versión final
    $("#ws_test").click(function() {
        console.log("ws test clicked");
        socket.send("ws-test");
    });

    // Manejo de eventos
    socket.onmessage = function(event) {
        console.log(event.data)
    }

});
