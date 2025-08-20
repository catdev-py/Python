-- INNER JOIN entre clientes y pedidos
SELECT clientes.nombre, pedidos.producto
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- LEFT JOIN
SELECT clientes.nombre, pedidos.producto
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
