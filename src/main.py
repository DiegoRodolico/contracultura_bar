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
    # FUNCIÓN 3: MENÚ PRINCIPAL
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
                print("\n📍 Función: Tomar Pedido (próximamente)")
            elif opcion == '4':
                print("\n📍 Función: Gestión de Clientes (próximamente)")
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
