## Why

Necesitamos una base de conocimiento sólida y estructurada para probar y validar un agente de IA basado en RAG. Para que el RAG enfrente retos reales, se requiere información con condiciones, excepciones y estructuras complejas propias de una Fintech o Banco Digital ficticio (AluraBank).

## What Changes

Se crearán cinco documentos en formato Markdown que simularán la documentación oficial de un banco digital. Estos incluirán casos límite y reglas de negocio específicas:
- Política de privacidad y protección de datos
- Términos y condiciones de uso
- Preguntas frecuentes sobre transacciones y límites
- Política de seguridad y prevención de fraudes
- Tarifas y comisiones del servicio

Estos documentos servirán como la fuente de verdad (source of truth) para el sistema de recuperación del agente.

## Capabilities

### New Capabilities
- `fake-bank-docs`: Conjunto de documentos Markdown con las reglas de negocio de AluraBank, que formarán el corpus de datos para el agente RAG.

### Modified Capabilities
Ninguna.

## Impact

Esta base de conocimiento permitirá realizar pruebas de extracción de información (RAG), evaluar estrategias de fragmentación (chunking) y probar la capacidad de razonamiento del agente frente a condiciones lógicas dentro del texto. Son archivos de datos de prueba, por lo que no afectan los componentes del sistema principal actual.
