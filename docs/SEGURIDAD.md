# Seguridad

## Seguridad por diseño

El proyecto incorpora seguridad por diseño como criterio transversal desde la definición de contratos hasta la ejecución local.

## Validación de entradas

Toda entrada debe validarse por tipo, formato y límites antes de procesarse.

## Control de salidas

Las salidas deben seguir contratos explícitos y registrar advertencias cuando existan incertidumbres.

## Trazabilidad

Las ejecuciones deben conservar trazas locales para permitir auditoría, depuración y revisión de decisiones.

## Separación lógica local y proveedor LLM

La lógica de negocio local y la integración con proveedores LLM se mantienen separadas para reducir acoplamiento y riesgo operativo.

## No incluir claves reales

No se deben almacenar claves reales en el repositorio. Solo se permite el uso de `.env.example` como plantilla.

## Revisión humana para acciones sensibles

Las acciones de impacto deben pasar por control y aprobación humana documentada.

## Límites del proyecto

Este repositorio no pretende cubrir por sí solo requisitos legales o regulatorios completos de cada sector.

## Alcance de seguridad

No se promete seguridad absoluta; se establecen medidas de validación, trazabilidad, revisión humana y límites explícitos.
Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
