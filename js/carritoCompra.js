$(function() {
  // Configurar variables
  var items = [];
  var cart = [];
  
  // Función para agregar un producto al carrito
  function addToCart(name, price) {
  for (var i in cart) {
  if (cart[i].name === name) {
  cart[i].count ++;
  saveCart();
  return;
  }
  }
  var item = new Item(name, price);
  cart.push(item);
  saveCart();
  }
  
  // Función para remover un producto del carrito
  function removeItemFromCart(name) {
  for (var i in cart) {
  if (cart[i].name === name) {
  cart[i].count --;
  if (cart[i].count === 0) {
  cart.splice(i, 1);
  }
  break;
  }
  }
  saveCart();
  }
  
  // Función para eliminar todo el carrito
  function removeAllItemsFromCart() {
  cart = [];
  saveCart();
  }
  
  // Función para crear un objeto de producto
  function Item(name, price) {
  this.name = name;
  this.price = price;
  this.count = 1;
  }
  
  // Función para guardar el carrito en el almacenamiento local
  function saveCart() {
  localStorage.setItem('shoppingCart', JSON.stringify(cart));
  updateCartCounter();
  }
  
  // Función para cargar el carrito desde el almacenamiento local
  function loadCart() {
  cart = JSON.parse(localStorage.getItem('shoppingCart')) || [];
  updateCartCounter();
  }
  
  // Función para actualizar el contador de carrito de compras
  function updateCartCounter() {
  var count = 0;
  for (var i in cart) {
  count += cart[i].count;
  }
  $('#cart-count').text(count);
  }
  
  // Agregar evento de clic al botón de agregar al carrito
  $('.add-to-cart').click(function() {
  var name = $(this).data('name');
  var price = $(this).data('price');
  addToCart(name, price);
  });
  
  // Agregar evento de clic al botón de carrito de compras
  $('#cart-button').click(function() {
  $('#cart-items').empty();
  for (var i in cart) {
  var item = cart[i];
  var html = '<li class="list-group-item d-flex justify-content-between lh-condensed">' +
  '<div>' +
  '<h6 class="my-0">' + item.name + '</h6>' +
  '<small class="text-muted">$' + item.price.toFixed(2) + '</small>' +
  '</div>' +
  '<div>' +
  '<button class="btn btn-sm btn-outline-danger remove-from-cart" data-name="' + item.name + '">Quitar</button>' +
  '</div>' +
  '</li>';
  $('#cart-items').append(html);
  }
  $('#cart-modal').modal('show');
  });
  
  // Agregar evento de clic al botón de eliminar del carrito
  $('#cart-items').on('click', '.remove-from-cart', function() {
  var name = $(this).data('name');
  removeItemFromCart(name);
  $(this).closest('li').remove();
  });
  
  // Agregar evento de clic al botón de vaciar carrito
  $('#clear-cart').click(function() {
  removeAllItemsFromCart();
  $('#cart-items').empty();
  $('#cart-modal').modal('hide');
  });
  loadCart();
});