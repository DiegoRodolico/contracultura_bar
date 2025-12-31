# 🍺 Contracultura Bar - Sistema de Gestión

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)
![GitHub](https://img.shields.io/badge/GitHub-Repository-lightgrey.svg)

Sistema de gestión completo para **Contracultura Bar**, desarrollado en Python con MySQL. Diseñado específicamente para las necesidades de un bar/restaurante moderno con menú extenso y control de operaciones.

## 🎯 Características Principales

### 📋 Gestión de Productos
- **12 categorías** organizadas (Cervezas Artesanales, Tragos, Burgers, Pizzas, etc.)
- **50+ productos** con precios, costos y control de stock
- Visualización por categorías con iconos y descripciones
- Alertas de stock bajo

### 🍽️ Control de Mesas
- **13 mesas** con ubicaciones específicas (Interior, Exterior, Barra, Sillón)
- Estados en tiempo real (Libre, Ocupada, Reservada)
- Capacidad por mesa y sugerencias de ubicación
- Resumen de ocupación del local

### 📊 Sistema de Pedidos
- Creación de pedidos vinculados a mesas y clientes
- Cálculo automático de totales
- Detalle de pedido con productos y cantidades
- Estados de pedido (Pendiente, En Proceso, Listo, Entregado)

### 👥 Gestión de Clientes
- Registro de clientes frecuentes
- Sistema de puntos por compras
- Historial de pedidos por cliente

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso | Versión |
|------------|-----|---------|
| **Python** | Lógica de negocio e interfaz | 3.8+ |
| **MySQL** | Base de datos relacional | 8.0+ |
| **mysql-connector-python** | Conexión Python-MySQL | 8.0+ |
| **Git** | Control de versiones | 2.25+ |
| **Debian** | Sistema operativo | 11+ |

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
```bash
# En Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip mysql-server mysql-client

👨💻 Autor
Diego Rodolico - Desarrollador y propietario de Contracultura Bar

GitHub: @DiegoRodolico

Proyecto desarrollado para automatizar la gestión del bar

🍻 Hecho con pasión por la buena cerveza y el buen código
