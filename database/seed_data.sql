-- ============================================
-- DATOS INICIALES para CONTRACULTURA BAR
-- ============================================

USE contracultura_bar;

-- Limpiar todo
-- DELETE FROM detalle_pedido;
-- DELETE FROM pedidos;
-- DELETE FROM productos;
-- DELETE FROM categorias;
-- DELETE FROM clientes;
-- DELETE FROM mesas;

-- Resetear AUTO_INCREMENT
-- ALTER TABLE categorias AUTO_INCREMENT = 1;
-- ALTER TABLE productos AUTO_INCREMENT = 1;
-- ALTER TABLE clientes AUTO_INCREMENT = 1;
-- ALTER TABLE mesas AUTO_INCREMENT = 1;
-- ALTER TABLE pedidos AUTO_INCREMENT = 1;
-- ALTER TABLE detalle_pedido AUTO_INCREMENT = 1;

-- CATEGORÍAS 
INSERT INTO categorias (nombre, descripcion, icono) VALUES
('CERVEZAS ARTESANALES', 'Nuestras cervezas elaboradas artesanalmente', '🍺'),
('CERVEZAS INDUSTRIALES', 'Los clásicos de siempre', '🍺'),
('TRAGOS', 'Tragos tradiciones del bar', '🍸'),
('BURGERS', 'Hamburguesas americanas', '🍔'),
('PA PICAR', 'Para picar mientras tomas', '🍟'),
('PIZZAS', 'Tradicionales pizzas al molde', '🍕'),
('VINOS', 'Vinos de la casa', '🍷'),
('CAFÉ', 'Cafeteria clásica para despabilar', '☕'),
('BEBIDAS FRÍAS', 'Bebidas frias alternativas al café', '🥤'),
('COSAS RICAS', 'Acompañamientos para el café o la bebida fría', '🥐'),
('ALMUERZO', 'Comidas para llenarse la mediodía', '🍞'),
('PROMOS', 'Diferentes promos,tanto de día como de noche', '💡')

;

-- PRODUCTOS - 
INSERT INTO productos (nombre, categoria_id, precio, costo, stock, descripcion) VALUES

-- Cervezas Artesanales (categoría_id = 1)
('IPA', 1, 4300, 2150, 40, 'Nuestra cerveza insignia, amarga y aromática'),
('Honey', 1, 4300, 2150, 40, 'Otra cerveza insignia, dulce y liviana'),
('Stout Negra', 1, 4600, 2300, 10, 'Oscura, cremosa, con notas a café tostado'),
('Golden Ale', 1, 4600, 2300, 10, 'Suave, refrescante, perfecta para empezar'),
('Irish Red', 1, 4600, 2300, 10, 'Color Ambar, cuerpo medio, cerveza amable'),

-- Cervezas Industriales (categoria_id = 2) 
('Imperial', 2, 7500, 2800, 12, 'Stout, Lager, IPA, Roja, APA'),
('Heineken', 2, 8500, 3500, 12, 'Clasica'),
('Grolsch', 2, 8500, 3500, 12, 'Parecida a la heineken'),

-- Tragos (categoría_id = 3)
('Fernet con Coca', 3, 8000, 2500, 30, 'El clásico argentino'),
('Gin Tónic', 3, 8000, 2500, 30, 'Gin Merle con tónica Cunnington'),
('Gancia Batido', 3, 8000, 2500, 30, 'Gancia con Seven'),
('Campari Orange', 3, 8000, 2500, 30, 'Campari con Naranja'),
('Cynar Pomelo', 3, 8000, 2500, 30, 'Cynar con Pomelo'),

-- Burgers (categoría_id = 4)
('Ant-Man', 4, 10000, 5000 , 9, 'Carne y Cheddar'),
('Capitan America', 4, 12000, 6000, 9, 'Carne, Cheddar y Panceta'),
('Spider-Man', 4, 12000, 6000, 9, 'Carne, Cheddar, Lechuga, Tomate y Cebolla'),
('Mystique', 4, 14000, 7500, 9, 'Carne, Cheddar, Queso Azul, Cebolla Caramelizada'),
('Wolverine', 4, 14000, 7500, 9, 'Carne, Muzza, Panceta, BBQ+Cebolla'),
('Coloso', 4, 14000, 7500, 9, 'Carne, Cheddar, Cebolla Caramelizada, Huevo'),
('Thor', 4, 15000, 8000, 9, 'Carne, Cheddarx4, Pancetax4'),

-- Pa Picar (categoría_id = 5)
('Papas Rusticas', 5, 8000, 2500, 15, 'Papas Fritas'),
('Papas con Cheddar, Panceta y Verdeo', 5, 9000, 3500, 60, 'Papas con Cheddar, Panceta y Verdeo'),
('Papas Fritas Picantes', 5, 9000, 3500, 60, 'Papas Fritas con Salsa Picantes'),

-- Pizzas (categoría_id = 6)
('Muzzarela', 6, 12000, 5000, 9, 'Tipica pizza de Muzza'),
('Margarita', 6, 13000, 6000, 9, 'Pizza con Tomate,Muzza, Albahaca'),
('Napolitana', 6, 14000, 7000, 9, 'Pizza con Tomate y Ajo'),
('Jamon y Morrones', 6, 15000, 7500, 9, 'Pizza con Jamon y Morrones'),
('Fugazzeta', 6, 12000, 5000, 9, 'Tipica pizza de Cebolla'),
('Roquefort', 6, 15000, 7500, 9, 'Pizza con Muzza y Roquefort'),

-- Vinos (categoría_id = 7)
('Malbec', 7, 13000, 6000, 4, 'Vino tinto clasico , aroma frutal'),
('Cabernet', 7, 13000, 6000, 3, 'Vino tinto suave, aroma mas astringente'),
('Blanco Dulce', 7, 13000, 6000, 1, 'Vino blanco, uva dulce, se toma frio'),

-- Café (categoria_id = 8)
('Cafe', 8, 2000, 900, 24, 'Cafe clasico, en jarrito o Americano con mas agua'),
('Cafe con Leche', 8, 2500, 1200, 25, 'Cafe con leche clasico, Latte'),
('Cappuccino', 8, 3000, 1200, 23, 'Cafe con leche, espumado con canela y cacao'),
('Submarino', 8, 3500, 1500, 5, 'Chocolate con leche caliente'),
('Te en Hebras', 8, 2000, 400, 20, 'Te en Hebras Rojo, Negro o Verde'),
('Mate Cocido', 8, 2000, 500, 18, 'Mate cosido perro'),

-- Bebidas Frías (categoria_id = 9)
('Exprimido', 9, 4500, 1000, 10, 'Exprimido de Naranja'),
('Limonada', 9, 4500, 1000, 10, 'Limonada de Limon JA'),
('Licuado', 9, 4500, 1500, 8, 'Licuado de Banana o Frutillas'),
('Milkshake', 9, 5000, 2000, 5, 'Helado con Leche y Crema Batida'),
('Frappucino', 9, 5000, 2000, 4, 'Cafe Frio, con Helado y Crema Batida'),
('Gaseosa', 9, 3000, 1200, 25, 'Coca, Coca Cero, SevenUp, Pepsi, Fanta'),
('Agua Saborizada', 9, 2500, 1000, 18, 'Aquarius o Levite, Manzana,Naranja o Pomelo'),
('Agua', 9, 2000, 700, 12, 'Agua con o sin Gas'),

-- Cosas Ricas (categoria_id = 10)
('Medialuna', 10, 900, 400, 72, 'Medialuna de Manteca Clasica'),
('Medialuna de Jamon y Queso', 10, 2000, 1000, 12, 'Medialuna de Manteca Rellena de Jamon y Queso'),
('Tostado de Miga de Jamon y Queso', 10, 5000, 2000, 24, '4 Triangulos de Miga de Jamon y Queso (2 Sanguches)'),
('Tostado Árabe de Jamon y Queso', 10, 3500, 1200, 12, 'Pan Arabe con Jamon y Queso'),
('Porción Budin', 10, 2500, 1200, 8, 'Budin Artesanal de Frutos Rojos, Chocolate, Vainilla, Limon, Zanahoria'),

-- Almuerzo (categoria_id = 11)
('Empanadas', 11, 2200, 800, 45, 'Empanadas Clasicas de Carne, o Pollo'),
('Porcion de Pizza', 11, 2000, 800, 8, 'Porcion de pizza de Muzza'),

-- Promos (categoria_id = 12)
('Cafe con Leche + 2 Medialunas', 12, 4000, 2500, 9, 'Clasico Desayuno'),
('Cafe con Leche + Tostados de Miga', 12, 8000, 3500, 9, 'Clasico Desayuno ++'),
('Cafe con Leche + Tostado Árabe', 12, 6000, 3000, 9, 'Clasico Desayuno +'),
('Gaseosa + Tostado Árabe', 12, 6000, 3000, 9, 'Arabe + Gaseosa'),
('Cafe con Leche + Porcion de Budin', 12, 7000, 3500,  9, 'Cafe + Porcion de Budin'),
('Cafe con Leche + 2 Medialunas de Jamon y Queso', 12, 8000, 3500, 9, 'Clasico Desayuno +++'),
('Cafe con Leche + Tostadas', 12, 8000, 3500, 9, 'Tostadas con queso o manteca, mermelada o dulce'),
('Exprimido o Limonada + Tostado de Miga', 12, 9000, 3000, 7, 'Exprimido/Limonada + Miga'),
('2 Exprimidos o Limonadas + Tostado de Miga', 12, 14000, 7000, 7, '2 Exprimidos/Limonadas + Miga'),
('Licuado + Porcion de Budin', 12, 8000, 3000, 7, 'Licuado + Porcion de Budin'),
('2 Licuados Promo', 12, 7500, 3000, 9, '2 Licuados, segundo al 50%'),
('3 Empanadas Promo', 12, 6000, 3000, 9, 'Que Miseria'),
('3 Empanadas + Gaseosa', 12, 8000, 4000, 9, 'Que Miseria ++'),
('2 Porciones + Gaseosa', 12, 7000, 3000, 9, '2 Porciones de Muzza + Gaseosa'),
('2 Porciones + Pinta', 12, 8000, 4000, 9,'2 Porciones de Muzza + Pinta'),
('Muzzarela + Imperial', 12, 16000, 10000, 9, 'Una Muzza + una Imperial de litro'),
('Papas Cheddar, Panceta y Verdeo + Imperial', 12, 16000, 10000, 12, 'Papas completas + una Imperial de litro'),
('Muzzarela + 2 Pintas', 12, 16000, 10000, 12, 'Una Muzza + 2 Pintas'),
('Papas Cheddar, Panceta y Verdeo + 2 Pintas', 12, 16000, 10000, 12,'Papas completas + 2 Pintas')

;

-- CLIENTES 
INSERT INTO clientes (nombre, telefono, puntos) VALUES
('NoCierto', '11-1234-5678', 100)

;

-- MESAS 
INSERT INTO mesas (numero, capacidad, ubicacion) VALUES
(1, 4, 'EXTERIOR'),
(2, 4, 'EXTERIOR'),
(3, 4, 'EXTERIOR'),
(4, 8, 'BARRA'),
(5, 4, 'SILLON'),
(6, 6, 'SILLON'),
(7, 4, 'SILLON'),
(8, 4, 'INTERIOR'),
(9, 4, 'INTERIOR'),
(10, 4, 'INTERIOR'),
(11, 8, 'BARRA'),
(12, 8, 'BARRA'),
(13, 8, 'BARRA')

;

-- PEDIDOS
INSERT INTO pedidos (mesa_id, cliente_id, estado, tipo, total, observaciones) VALUES
('1,','1','ENTREGADO','MESA',50000, 'Cerveza sin espuma')

;

-- DETALLE_ PEDIDOS
INSERT INTO detalle_pedido (pedido_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 2, 4000)

;
