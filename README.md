## Instrucciones para llenar la base de datos

Para llenar la base de datos, necesitas usar el **Shell de Django**. Antes de ello, deberás crear un superusuario.

### Paso 1: Crear un superusuario

1. Abre la consola y ejecuta el siguiente comando:

   ```bash
   python manage.py createsuperuser
   ```

2. LLena las crendenciales:

   ```
   Username: tu_nombre_de_usuario
   ```

   ```
   Password: tu_password
   ```

   ```
   Password Again: tu_password
   ```

### Paso 2: Llenar la base de datos

1. Abre la consola y ejecuta el siguiente comando:

   ```bash
   python manage.py shell
   ```

2. Importa la funcion:

   ```bash
   from utils.crear_registros import llenar_vias_accidentes
   ```

3. Llama la funcion:

   ```bash
   llenar_vias_accidentes()
   ```

4. Esperar, generalmente se demora un buen tiempo en llenar la base de datos, te invito a optimizar la funcion, que se puede mejorar ampliamente, luego de que se complete dejara de funcionar el contador en la consola y tendras la base de datos llena.