#!/bin/bash
echo "🍺 CONFIGURANDO CONTRACULTURA BAR 🍺"
echo "======================================"

# Pide la contraseña de MySQL
echo -n "Ingresa la contraseña de MySQL (root): "
read -s password
echo

# Crea la base de datos y tablas
echo "Creando base de datos..."
sudo mysql -u root -p$password < contracultura_bar.sql

# Inserta los datos iniciales
echo "Insertando productos y mesas..."
sudo mysql -u root -p$password < seed_data.sql

echo "✅ ¡Base de datos creada exitosamente!"
echo
echo "Para verificar, ejecuta:"
echo "sudo mysql -u root -p contracultura_bar -e 'SHOW TABLES;'"
