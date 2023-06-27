$(document).ready(function () {
    // Mostrar u ocultar el menú de ayuda al hacer clic en el botón de ayuda
    $('.help-btn').click(function () {
      $('.help-menu').toggle();
    });
  
    // Ocultar el menú de ayuda al hacer clic fuera del menú
    $(document).click(function (event) {
      if (!$(event.target).closest('.help-menu, .help-btn').length) {
        $('.help-menu').hide();
      }
    });
  });
