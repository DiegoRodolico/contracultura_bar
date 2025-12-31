#!/usr/bin/env python3
"""
Sistema de Gestión - Contracultura Bar
Autor: Diego Rodolico
Descripción: Sistema de gestión para bar/restaurante con Python + MySQL
"""

import mysql.connector
from mysql.connector import Error
import os
import sys

# ============================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ============================================
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'casla1908',  
    'database': 'contracultura_bar'
}

# ============================================
# CLASE PRINCIPAL DEL SISTEMA
# ============================================
class ContraculturaBarSystem:
    def __init__(self):
        """Inicializa el sistema y conecta a la base de datos"""
        self.connection = None
        self.cursor = None
        self.connect_to_db()
    
    def connect_to_db(self):
        """Establece conexión con la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("✅ Conectado a la base de datos: Contracultura Bar")
                return True
        except Error as e:
            print(f"❌ Error conectando a MySQL: {e}")
            print(f"   Configuración usada: {DB_CONFIG['user']}@{DB_CONFIG['host']}")
            return False
    
    # ============================================
    # FUNCIÓN 1: VER MENÚ COMPLETO 
    # ============================================
    
    def ver_menu_completo(self):
        """Muestra todos los productos organizados por categoría"""
        print("\n" + "="*60)
        print("                  🍺 MENÚ CONTRACULTURA BAR")
        print("="*60)
        
        try:
            # 1. Primero obtenemos todas las categorías
            query_categorias = """
                SELECT id, nombre, icono 
                FROM categorias 
                ORDER BY id
            """
            self.cursor.execute(query_categorias)
            categorias = self.cursor.fetchall()
            
            if not categorias:
                print("❌ No hay categorías en la base de datos")
                return
            
            # 2. Para cada categoría, mostramos sus productos
            for categoria in categorias:
                cat_id = categoria['id']
                cat_nombre = categoria['nombre']
                cat_icono = categoria.get('icono', '🍽️')
                
                print(f"\n{cat_icono} {cat_nombre.upper()}")
                print("-" * 40)
                
                # Obtener productos de esta categoría
                query_productos = """
                    SELECT nombre, precio, stock, descripcion 
                    FROM productos 
                    WHERE categoria_id = %s AND activo = TRUE
                    ORDER BY nombre
                """
                self.cursor.execute(query_productos, (cat_id,))
                productos = self.cursor.fetchall()
                
                if productos:
                    for producto in productos:
                        nombre = producto['nombre']
                        precio = producto['precio']  
                        stock = producto['stock']
                        desc = producto['descripcion'] or ""
                        
                        # Formato bonito
                        precio_formato = f"${precio:,.0f}".replace(",", ".")
                        stock_info = f"[Stock: {stock}]" if stock < 10 else ""
                        
                        print(f"  • {nombre:30} {precio_formato:>10} {stock_info}")
                        if desc:
                            print(f"    {desc[:50]}...")
                else:
                    print("  (No hay productos en esta categoría)")
                
                print()  # Línea en blanco entre categorías
            
            # 3. Mostrar resumen
            print("\n" + "="*60)
            query_resumen = """
                SELECT COUNT(*) as total_productos, 
                       SUM(stock) as total_stock
                FROM productos 
                WHERE activo = TRUE
            """
            self.cursor.execute(query_resumen)
            resumen = self.cursor.fetchone()
            
            if resumen:
                print(f"📊 Resumen: {resumen['total_productos']} productos activos")
                print(f"           {resumen['total_stock']} unidades en stock total")
            
        except Error as e:
            print(f"❌ Error al obtener el menú: {e}")
    
    # ============================================
    # FUNCIÓN 2: GESTIÓN DE MESAS
    # ============================================
    
    def gestion_mesas(self):
        """Muestra el estado de las mesas"""
        print("\n" + "="*50)
        print("              📍 ESTADO DE MESAS")
        print("="*50)
        
        try:
            # Obtener todas las mesas
            query = """
                SELECT numero, capacidad, ubicacion, estado 
                FROM mesas 
                ORDER BY numero
            """
            self.cursor.execute(query)
            mesas = self.cursor.fetchall()
            
            if not mesas:
                print("❌ No hay mesas configuradas en la base de datos")
                return
            
            # Contadores por estado
            libre = ocupada = reservada = 0
            
            print("\n" + "-"*50)
            print("MESA  CAPACIDAD  UBICACIÓN      ESTADO")
            print("-"*50)
            
            for mesa in mesas:
                numero = mesa['numero']
                capacidad = mesa['capacidad']
                ubicacion = mesa['ubicacion']
                estado = mesa['estado']
                
                # Emojis según estado
                if estado == 'LIBRE':
                    emoji = '🟢'
                    libre += 1
                elif estado == 'OCUPADA':
                    emoji = '🔴'
                    ocupada += 1
                elif estado == 'RESERVADA':
                    emoji = '🟡'
                    reservada += 1
                else:
                    emoji = '⚪'
                
                # Emojis según ubicación
                if ubicacion == 'INTERIOR':
                    ubic_emoji = '🏠'
                elif ubicacion == 'EXTERIOR':
                    ubic_emoji = '🌳'
                elif ubicacion == 'BARRA':
                    ubic_emoji = '🍻'
                elif ubicacion == 'SILLON':
                    ubic_emoji = '🛋️'
                elif ubicacion == 'AFUERA':
                    ubic_emoji = '🌞'
                else:
                    ubic_emoji = '📍'
                
                print(f"{emoji} {numero:2}     {capacidad:2}       {ubic_emoji} {ubicacion:12} {estado}")
            
            # Mostrar resumen
            print("\n" + "="*50)
            print("📊 RESUMEN DE OCUPACIÓN:")
            print(f"  🟢 Libres:    {libre} mesas")
            print(f"  🔴 Ocupadas:  {ocupada} mesas")
            print(f"  🟡 Reservadas: {reservada} mesas")
            print(f"  📍 Total:     {len(mesas)} mesas")
            
            # Sugerencia según ocupación
            if libre >= 8:
                print("\n💡 Hay buena disponibilidad de mesas")
            elif libre >= 3:
                print("\n⚠️  Disponibilidad media, considerar reservas")
            else:
                print("\n🚨 Poca disponibilidad, sugerir barra o espera")
            
            # Mostrar mesas libres específicas
            if libre > 0:
                print("\n📋 Mesas disponibles:")
                query_libres = """
                    SELECT numero, capacidad, ubicacion 
                    FROM mesas 
                    WHERE estado = 'LIBRE' 
                    ORDER BY capacidad
                """
                self.cursor.execute(query_libres)
                libres = self.cursor.fetchall()
                
                for mesa_libre in libres:
                    print(f"  • Mesa {mesa_libre['numero']} ({mesa_libre['capacidad']} pers) - {mesa_libre['ubicacion']}")
        
        except Error as e:
            print(f"❌ Error al obtener mesas: {e}")
    
    # ============================================
    # FUNCIÓN 3: TOMAR PEDIDO (¡HOY IMPLEMENTAMOS!)
    # ============================================
    
    def tomar_pedido(self):
        """Permite tomar un nuevo pedido"""
        print("\n" + "="*50)
        print("              📝 NUEVO PEDIDO")
        print("="*50)
        
        try:
            # 1. Mostrar mesas disponibles
            print("\n📍 MESAS DISPONIBLES:")
            query_mesas = """
                SELECT id, numero, capacidad 
                FROM mesas 
                WHERE estado = 'LIBRE'
                ORDER BY numero
            """
            self.cursor.execute(query_mesas)
            mesas_libres = self.cursor.fetchall()
            
            if not mesas_libres:
                print("❌ No hay mesas disponibles. Intenta más tarde.")
                return
            
            for mesa in mesas_libres:
                print(f"  {mesa['numero']}. Mesa {mesa['numero']} ({mesa['capacidad']} pers)")
            
            # 2. Seleccionar mesa
            try:
                mesa_numero = int(input("\n👉 Número de mesa: "))
                
                # Verificar que la mesa existe y está libre
                query_mesa = """
                    SELECT id, numero, capacidad 
                    FROM mesas 
                    WHERE numero = %s AND estado = 'LIBRE'
                """
                self.cursor.execute(query_mesa, (mesa_numero,))
                mesa_seleccionada = self.cursor.fetchone()
                
                if not mesa_seleccionada:
                    print(f"❌ Mesa {mesa_numero} no disponible o no existe")
                    return
                
                mesa_id = mesa_seleccionada['id']
                
                # 3. Mostrar categorías para seleccionar productos
                print("\n" + "="*50)
                print("          🍽️  SELECCIONAR PRODUCTOS")
                print("="*50)
                
                pedido_terminado = False
                productos_pedido = []  # Lista de (producto_id, cantidad, precio)
                total_pedido = 0
                
                while not pedido_terminado:
                    print(f"\n💰 Total actual: ${total_pedido:,.0f}".replace(",", "."))
                    
                    # Mostrar categorías
                    query_cats = "SELECT id, nombre FROM categorias ORDER BY id"
                    self.cursor.execute(query_cats)
                    categorias = self.cursor.fetchall()
                    
                    print("\n📋 Categorías disponibles:")
                    for cat in categorias:
                        print(f"  {cat['id']}. {cat['nombre']}")
                    print("  0. Terminar pedido")
                    
                    try:
                        cat_id = int(input("\n👉 Número de categoría: "))
                        
                        if cat_id == 0:
                            pedido_terminado = True
                            continue
                        
                        # Verificar categoría válida
                        cat_valida = any(cat['id'] == cat_id for cat in categorias)
                        if not cat_valida:
                            print("❌ Categoría no válida")
                            continue
                        
                        # Mostrar productos de esa categoría
                        query_prod = """
                            SELECT id, nombre, precio, stock 
                            FROM productos 
                            WHERE categoria_id = %s AND activo = TRUE AND stock > 0
                            ORDER BY nombre
                        """
                        self.cursor.execute(query_prod, (cat_id,))
                        productos = self.cursor.fetchall()
                        
                        if not productos:
                            print("❌ No hay productos disponibles en esta categoría")
                            continue
                        
                        print(f"\n📦 Productos en categoría {cat_id}:")
                        for prod in productos:
                            precio_fmt = f"${prod['precio']:,.0f}".replace(",", ".")
                            print(f"  {prod['id']}. {prod['nombre']:30} {precio_fmt:>10} [Stock: {prod['stock']}]")
                        
                        # Seleccionar producto
                        try:
                            prod_id = int(input("\n👉 ID del producto: "))
                            cantidad = int(input("👉 Cantidad: "))
                            
                            # Verificar producto válido y stock
                            producto_seleccionado = None
                            for prod in productos:
                                if prod['id'] == prod_id:
                                    producto_seleccionado = prod
                                    break
                            
                            if not producto_seleccionado:
                                print("❌ Producto no válido")
                                continue
                            
                            if cantidad <= 0:
                                print("❌ Cantidad debe ser mayor a 0")
                                continue
                            
                            if cantidad > producto_seleccionado['stock']:
                                print(f"❌ Stock insuficiente. Disponible: {producto_seleccionado['stock']}")
                                continue
                            
                            # Agregar al pedido
                            subtotal = producto_seleccionado['precio'] * cantidad
                            productos_pedido.append({
                                'id': prod_id,
                                'nombre': producto_seleccionado['nombre'],
                                'precio': producto_seleccionado['precio'],
                                'cantidad': cantidad,
                                'subtotal': subtotal
                            })
                            
                            total_pedido += subtotal
                            
                            print(f"✅ Agregado: {cantidad}x {producto_seleccionado['nombre']}")
                            print(f"   Subtotal: ${subtotal:,.0f}".replace(",", "."))
                            
                        except ValueError:
                            print("❌ Ingresa números válidos")
                            continue
                            
                    except ValueError:
                        print("❌ Ingresa un número válido")
                        continue
                
                # 4. Finalizar pedido
                if not productos_pedido:
                    print("\n❌ Pedido vacío. No se creó ningún pedido.")
                    return
                
                print("\n" + "="*50)
                print("              📄 RESUMEN DEL PEDIDO")
                print("="*50)
                
                print(f"\nMesa: {mesa_numero}")
                print("\nProductos:")
                for item in productos_pedido:
                    precio_fmt = f"${item['precio']:,.0f}".replace(",", ".")
                    subtotal_fmt = f"${item['subtotal']:,.0f}".replace(",", ".")
                    print(f"  • {item['cantidad']}x {item['nombre']:30} {precio_fmt} = {subtotal_fmt}")
                
                total_fmt = f"${total_pedido:,.0f}".replace(",", ".")
                print(f"\n💰 TOTAL: {total_fmt}")
                
                # 5. Confirmar pedido
                confirmar = input("\n¿Confirmar pedido? (s/n): ").lower().strip()
                
                if confirmar == 's':
                    # Insertar pedido
                    query_insert_pedido = """
                        INSERT INTO pedidos (mesa_id, estado, total)
                        VALUES (%s, 'PENDIENTE', %s)
                    """
                    self.cursor.execute(query_insert_pedido, (mesa_id, total_pedido))
                    pedido_id = self.cursor.lastrowid
                    
                    # Insertar detalles del pedido
                    for item in productos_pedido:
                        query_insert_detalle = """
                            INSERT INTO detalle_pedido 
                            (pedido_id, producto_id, cantidad, precio_unitario)
                            VALUES (%s, %s, %s, %s)
                        """
                        self.cursor.execute(query_insert_detalle, 
                                          (pedido_id, item['id'], item['cantidad'], item['precio']))
                        
                        # Actualizar stock del producto
                        query_update_stock = """
                            UPDATE productos 
                            SET stock = stock - %s 
                            WHERE id = %s
                        """
                        self.cursor.execute(query_update_stock, (item['cantidad'], item['id']))
                    
                    # Actualizar estado de la mesa
                    query_update_mesa = """
                        UPDATE mesas 
                        SET estado = 'OCUPADA' 
                        WHERE id = %s
                    """
                    self.cursor.execute(query_update_mesa, (mesa_id,))
                    
                    # Commit de todas las transacciones
                    self.connection.commit()
                    
                    print(f"\n✅ Pedido #{pedido_id} creado exitosamente!")
                    print(f"   Total: ${total_pedido:,.0f}".replace(",", "."))
                    print(f"   Mesa {mesa_numero} ahora está OCUPADA")
                    
                else:
                    print("\n❌ Pedido cancelado")
                    self.connection.rollback()
            
            except ValueError:
                print("❌ Ingresa un número válido")
                return
                
        except Error as e:
            print(f"❌ Error al tomar pedido: {e}")
            self.connection.rollback()

    # ============================================
    # FUNCIÓN 4: GESTIÓN DE CLIENTES (¡HOY IMPLEMENTAMOS!)
    # ============================================
    
    def gestion_clientes(self):
        """Gestión de clientes frecuentes"""
        print("\n" + "="*50)
        print("              👥 GESTIÓN DE CLIENTES")
        print("="*50)
        print("\n1. 🔍 Ver todos los clientes")
        print("2. 👤 Buscar cliente por nombre/teléfono")
        print("3. ➕ Agregar nuevo cliente")
        print("4. 📊 Ver puntos y pedidos de cliente")
        print("0. ↩️  Volver al menú principal")
        
        try:
            opcion = input("\n👉 Selecciona una opción: ").strip()
            
            if opcion == '1':
                self.ver_todos_clientes()
            elif opcion == '2':
                self.buscar_cliente()
            elif opcion == '3':
                self.agregar_cliente()
            elif opcion == '4':
                self.ver_cliente_detalle()
            elif opcion == '0':
                return
            else:
                print("❌ Opción no válida")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def ver_todos_clientes(self):
        """Muestra todos los clientes registrados"""
        try:
            query = """
                SELECT id, nombre, telefono, puntos, fecha_registro
                FROM clientes
                ORDER BY puntos DESC, nombre
            """
            self.cursor.execute(query)
            clientes = self.cursor.fetchall()
            
            if not clientes:
                print("\n📭 No hay clientes registrados")
                return
            
            print("\n" + "="*60)
            print("                    📋 CLIENTES REGISTRADOS")
            print("="*60)
            print("\nID  NOMBRE                      TELÉFONO       PUNTOS  REGISTRO")
            print("-" * 60)
            
            for cliente in clientes:
                registro = cliente['fecha_registro'].strftime('%d/%m/%Y') if cliente['fecha_registro'] else 'N/A'
                print(f"{cliente['id']:2}  {cliente['nombre']:25}  {cliente['telefono'] or 'N/A':12}  {cliente['puntos']:6}  {registro}")
            
            # Resumen
            print("\n" + "-" * 60)
            print(f"📊 Total clientes: {len(clientes)}")
            
            # Top 3 clientes por puntos
            if len(clientes) >= 3:
                print("\n🏆 TOP 3 CLIENTES:")
                for i, cliente in enumerate(clientes[:3], 1):
                    print(f"  {i}. {cliente['nombre']} - {cliente['puntos']} puntos")
        
        except Error as e:
            print(f"❌ Error: {e}")
    
    def buscar_cliente(self):
        """Busca cliente por nombre o teléfono"""
        try:
            termino = input("\n🔍 Ingresa nombre o teléfono a buscar: ").strip()
            
            if not termino:
                print("❌ Ingresa un término de búsqueda")
                return
            
            query = """
                SELECT id, nombre, telefono, puntos, fecha_registro
                FROM clientes
                WHERE nombre LIKE %s OR telefono LIKE %s
                ORDER BY nombre
            """
            self.cursor.execute(query, (f"%{termino}%", f"%{termino}%"))
            clientes = self.cursor.fetchall()
            
            if not clientes:
                print(f"\n🔎 No se encontraron clientes con '{termino}'")
                return
            
            print(f"\n✅ Se encontraron {len(clientes)} cliente(s):")
            for cliente in clientes:
                print(f"  • {cliente['nombre']} - Tel: {cliente['telefono']} - Puntos: {cliente['puntos']}")
        
        except Error as e:
            print(f"❌ Error: {e}")
    
    def agregar_cliente(self):
        """Agrega un nuevo cliente"""
        try:
            print("\n" + "="*50)
            print("              👤 NUEVO CLIENTE")
            print("="*50)
            
            nombre = input("\n👉 Nombre completo: ").strip()
            if not nombre:
                print("❌ El nombre es obligatorio")
                return
            
            telefono = input("👉 Teléfono (opcional): ").strip() or None
            email = input("👉 Email (opcional): ").strip() or None
            
            puntos_iniciales = 0 
            
            query = """
                INSERT INTO clientes (nombre, telefono, email, puntos)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (nombre, telefono, email, puntos_iniciales))
            self.connection.commit()
            
            cliente_id = self.cursor.lastrowid
            print(f"\n✅ Cliente #{cliente_id} agregado exitosamente!")
            print(f"   Nombre: {nombre}")
            print(f"   Puntos iniciales: {puntos_iniciales}")
            
        except Error as e:
            print(f"❌ Error: {e}")
            self.connection.rollback()
    
    def ver_cliente_detalle(self):
        """Muestra detalle y pedidos de un cliente específico"""
        try:
            cliente_id = input("\n👉 ID del cliente: ").strip()
            
            if not cliente_id.isdigit():
                print("❌ Ingresa un ID válido (número)")
                return
            
            # Obtener info del cliente
            query_cliente = """
                SELECT id, nombre, telefono, email, puntos, fecha_registro
                FROM clientes
                WHERE id = %s
            """
            self.cursor.execute(query_cliente, (int(cliente_id),))
            cliente = self.cursor.fetchone()
            
            if not cliente:
                print(f"❌ Cliente #{cliente_id} no encontrado")
                return
            
            print("\n" + "="*50)
            print(f"           👤 DETALLE CLIENTE #{cliente['id']}")
            print("="*50)
            print(f"\n📋 Información:")
            print(f"  Nombre: {cliente['nombre']}")
            print(f"  Teléfono: {cliente['telefono'] or 'No registrado'}")
            print(f"  Email: {cliente['email'] or 'No registrado'}")
            print(f"  Puntos acumulados: {cliente['puntos']}")
            print(f"  Registrado desde: {cliente['fecha_registro'].strftime('%d/%m/%Y')}")
            
            # Obtener pedidos del cliente
            query_pedidos = """
                SELECT p.id, p.fecha_creacion, p.total, p.estado,
                       m.numero as mesa_numero
                FROM pedidos p
                LEFT JOIN mesas m ON p.mesa_id = m.id
                WHERE p.cliente_id = %s
                ORDER BY p.fecha_creacion DESC
                LIMIT 10
            """
            self.cursor.execute(query_pedidos, (int(cliente_id),))
            pedidos = self.cursor.fetchall()
            
            if pedidos:
                print(f"\n📦 Últimos pedidos ({len(pedidos)}):")
                for pedido in pedidos:
                    fecha = pedido['fecha_creacion'].strftime('%d/%m/%Y %H:%M')
                    total_fmt = f"${pedido['total']:,.0f}".replace(",", ".")
                    mesa_info = f"Mesa {pedido['mesa_numero']}" if pedido['mesa_numero'] else "Para llevar"
                    
                    print(f"  • Pedido #{pedido['id']} - {fecha}")
                    print(f"    {mesa_info} - {total_fmt} - Estado: {pedido['estado']}")
            else:
                print("\n📭 El cliente no tiene pedidos registrados")
            
            # Sugerir canjear puntos si tiene muchos
            if cliente['puntos'] >= 100:
                print(f"\n🎁 ¡Tiene {cliente['puntos']} puntos!")
                print("   Puede canjear 100 puntos por una bebida gratis")
        
        except Error as e:
            print(f"❌ Error: {e}")



    # ============================================
    # FUNCIÓN 0: MENÚ PRINCIPAL
    # ============================================
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*50)
        print("       🍺 CONTRACULTURA BAR - SISTEMA DE GESTIÓN")
        print("="*50)
        print("\n1. 📋 Ver Menú Completo")
        print("2. 🍽️  Gestión de Mesas")
        print("3. 📝 Tomar Pedido")
        print("4. 👥 Gestión de Clientes")
        print("5. 📊 Reportes y Estadísticas")
        print("6. 🛒 Control de Inventario")
        print("0. 🚪 Salir")
    
    # ============================================
    # FUNCIONES DE UTILIDAD
    # ============================================
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def pausa(self):
        """Pausa la ejecución hasta que el usuario presione Enter"""
        input("\n⏎ Presiona Enter para continuar...")

# ============================================
# PROGRAMA PRINCIPAL
# ============================================
def main():
    """Función principal que ejecuta el sistema"""
    sistema = ContraculturaBarSystem()
    
    if not sistema.connection:
        print("No se pudo conectar a la base de datos. Saliendo...")
        return
    
    while True:
        sistema.limpiar_pantalla()
        sistema.mostrar_menu_principal()
        
        try:
            opcion = input("\n👉 Selecciona una opción (0-6): ").strip()
            
            if opcion == '0':
                print("\n👋 ¡Hasta luego! Gracias por usar Contracultura Bar System")
                if sistema.connection and sistema.connection.is_connected():
                    sistema.cursor.close()
                    sistema.connection.close()
                break
            elif opcion == '1':
                sistema.ver_menu_completo()
            elif opcion == '2':
                sistema.gestion_mesas()
            elif opcion == '3':
                sistema.tomar_pedido()
            elif opcion == '4':
                sistema.gestion_clientes()
            elif opcion == '5':
                print("\n📍 Función: Reportes (próximamente)")
            elif opcion == '6':
                print("\n📍 Función: Inventario (próximamente)")
            else:
                print("\n❌ Opción no válida. Intenta de nuevo.")
            
            sistema.pausa()
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupción detectada. Saliendo...")
            if sistema.connection and sistema.connection.is_connected():
                sistema.cursor.close()
                sistema.connection.close()
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            sistema.pausa()

# ============================================
# EJECUCIÓN
# ============================================
if __name__ == "__main__":
    main()

