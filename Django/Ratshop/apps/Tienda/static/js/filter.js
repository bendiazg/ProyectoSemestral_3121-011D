document.addEventListener("DOMContentLoaded", function() {
    // Obtener todas las tarjetas de producto
    var productos = document.querySelectorAll(".card");

    // Recorrer cada tarjeta de producto
    productos.forEach(function(producto) {
        // Obtener el stock del producto
        var stock = producto.querySelector(".stock-value").textContent;

        // Verificar si el stock es igual a 0
        if (stock === "0") {
            // Ocultar la tarjeta de producto
            producto.style.display = "none";
        }
    });
});