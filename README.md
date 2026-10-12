ABERIGUAR TODO DE (PODMAN Y DOCKER)para el 5 de octubre  

1. ¿Qué es Docker?
Docker es una plataforma que permite crear, ejecutar y compartir aplicaciones dentro de contenedores. Facilita que un programa funcione de manera similar en diferentes computadoras.

2. ¿Qué es Podman?
Podman es una herramienta que permite crear, ejecutar y administrar contenedores. Es similar a Docker y puede ejecutar contenedores sin necesitar un servicio central permanente.

3. ¿Qué es un contenedor?
Es un entorno aislado que contiene una aplicación y los elementos necesarios para ejecutarla.
Ejemplo: ejecutar una aplicación de Python sin tener que configurar todo manualmente en cada computadora.

4. ¿Qué es una imagen?
Es una plantilla que contiene los archivos y las dependencias necesarias para crear un contenedor.

5. ¿Para qué sirven Docker y Podman?
- Ejecutar aplicaciones de forma aislada.
- Facilitar el desarrollo de software.
- Probar programas sin modificar todo el sistema.
- Compartir aplicaciones entre computadoras.
- Desplegar aplicaciones en servidores.
  
6. Diferencias entre Docker y Podman
Docker	Podman
Utiliza normalmente el servicio Docker Engine.	No necesita un servicio central permanente.
Usa Docker Desktop en Windows.	Usa Podman Desktop en Windows.
Permite administrar contenedores e imágenes.	También administra contenedores e imágenes.
Es muy utilizado en el desarrollo de software.	Destaca por su funcionamiento sin privilegios de administrador.

7. Ventajas y desventajas
Docker
- Ventajas: fácil de utilizar, popular y con amplia documentación.
- Desventajas: su configuración puede requerir más recursos y permisos, según el entorno.
Podman
- Ventajas: puede ejecutarse sin privilegios elevados y es compatible con muchos comandos de Docker.
- Desventajas: algunas configuraciones y herramientas pueden requerir pasos adicionales.
  
8. Comandos básicos
Acción	Docker	Podman
Ver versión	docker --version	podman --version
Descargar imagen	docker pull nginx	podman pull nginx
Ver contenedores	docker ps	podman ps
Ver imágenes	docker images	podman images
Ejecutar contenedor	docker run nginx	podman run nginx

9. ¿Qué es Docker Desktop y Podman Desktop?
Son aplicaciones con interfaz gráfica que permiten administrar contenedores e imágenes de manera visual, sin escribir todos los comandos manualmente.

10.  Conclusión
Docker y Podman son herramientas importantes para el desarrollo de software porque permiten ejecutar aplicaciones mediante contenedores. Ambas facilitan las pruebas, el desarrollo y la distribución de programas. La principal diferencia es que Docker utiliza normalmente un servicio central, mientras que Podman puede trabajar sin él
