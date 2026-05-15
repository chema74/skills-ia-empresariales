# Arquitectura

## Arquitectura modular

El repositorio se organiza por componentes desacoplados para permitir evolucion incremental y reutilizacion entre productos.

## Nucleo comun

`src/skillforge/core` centraliza contratos y reglas minimas compartidas por todas las skills.

## Contratos

Los contratos definen la forma de salida, estado, trazas y advertencias para garantizar interoperabilidad y pruebas reproducibles.

## Seguridad

Se aplica seguridad por diseno con validacion, limites explicitos y revision humana en acciones sensibles.

## Trazabilidad

Cada ejecucion debe generar trazas locales para auditoria tecnica y analisis posterior.

## Fallback local

La operacion local es la ruta base para que las pruebas y demos no dependan de Internet ni de APIs externas.

## Capa LLM opcional futura

La integracion con proveedor LLM sera opcional en fases posteriores y no condiciona la ejecucion local base.

## Skills independientes

Cada skill debe poder ejecutarse y validarse de forma autonoma con contratos estables del nucleo comun.

## Demos

`demos/` contiene escenarios de ejecucion para mostrar capacidades en entornos controlados.

## Evidencias

`evidencias/capturas` y `evidencias/salidas` almacenan pruebas demostrables y auditables de cada demo.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
