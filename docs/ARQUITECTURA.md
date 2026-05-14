# Arquitectura

## Arquitectura modular

El repositorio se organiza por componentes desacoplados para permitir evolución incremental y reutilización entre productos.

## Núcleo común

`src/skillforge/core` centraliza contratos y reglas mínimas compartidas por todas las skills.

## Contratos

Los contratos definen la forma de salida, estado, trazas y advertencias para garantizar interoperabilidad y pruebas reproducibles.

## Seguridad

Se aplica seguridad por diseño con validación, límites explícitos y revisión humana en acciones sensibles.

## Trazabilidad

Cada ejecución debe generar trazas locales para auditoría técnica y análisis posterior.

## Fallback local

La operación local es la ruta base para que las pruebas y demos no dependan de Internet ni de APIs externas.

## Capa LLM opcional futura

La integración con proveedor LLM será opcional en fases posteriores y no condiciona la ejecución local base.

## Skills independientes

Cada skill debe poder ejecutarse y validarse de forma autónoma con contratos estables del núcleo común.

## Demos

`demos/` contendrá escenarios de ejecución para mostrar capacidades en entornos controlados.

## Evidencias

`evidencias/capturas` y `evidencias/salidas` almacenarán pruebas demostrables y auditables de cada demo.
Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
