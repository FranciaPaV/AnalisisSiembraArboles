let boton=document.getElementById("generarboton")
boton.addEventListener("click", function(evento){
    evento.preventDefault()
    let reporte=document.getElementById("reporte")
    reporte.classList.remove("d-none") //para quitar el d-none del html q me oculta la tabla
}) 