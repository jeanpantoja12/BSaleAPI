# BSaleAPI

## Descripción
Tienda online realizada en Django Framework (API Backend) y Javascript (Vanilla) con consumo de datos brindados por la empresa BSale.

## API's
Las API's utilizadas en el ejercicio son las siguientes:

**Search**
----
  Retorna los datos de una búsqueda de producto en formato JSON paginados en 10 productos.

* **URL**

  /api/search

* **Método:**
  
  `GET`

*  **Parámetros en URL**

   **Requerido:**
 
   `s=[string]` // Palabra de búsqueda

   **Opcional:**
 
   `order=[asc/desc]` // Orden de búsqueda
   `from_s=[numeric]` // Precio desde
   `to_s=[numeric]` // Precio hasta
    `page=[integer]` // Número de página
    
* **Parámetros de Data**

  Ninguno.

* **Respuesta Success:**

  * **Code:** 200 <br />
    **Content:** `{ 
    results : obj, 
    num_pages: integer,
    has_next: boolean,
    has_prev: boolean
    }`
 
* **Respuesta Error:**

 Ninguno.

* **Ejemplo:**

  ```javascript
    fetch('api/search?s=pisco&page=1')
    .then(response => response.json())
    .then(responses =>{
        console.log(responses);
    });
  ```
**Category Search**
----
  Retorna los datos de todos los productos pertenecientes a una categoría en formato JSON, paginados en 8 artículos.

* **URL**

  /api/categories/search/<str:cat>/<int:num>

* **Método:**
  
  `GET`

*  **Parámetros en URL**

   **Requerido:**
 
   `<str:cat>` // Categoría
    `<int:num>` // Número de página
    
   **Opcional:**
 
   `order=[asc/desc]`
    
* **Parámetros de Data**

  Ninguno.

* **Respuesta Success:**

  * **Code:** 200 <br />
    **Content:** `{ 
    results : obj, 
    has_next: boolean
    }`
 
* **Respuesta Error:**


  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Categoría no encontrada" }`

* **Ejemplo:**

  ```javascript
    fetch('api/categories/search/ron/1')
    .then(response => response.json())
    .then(responses =>{
        console.log(responses);
    });
  ```
**Categories**
----
  Retorna los datos de todas las categorías en formato JSON

* **URL**

  /api/categories

* **Método:**
  
  `GET`

*  **Parámetros en URL**

   Ninguno.
    
* **Parámetros de Data**

  Ninguno.

* **Respuesta Success:**

  * **Code:** 200 <br />
    **Content:** `{ 
    categories : obj
    }`
 
* **Respuesta Error:**

  Ninguno.

* **Ejemplo:**

  ```javascript
    fetch('api/categories')
    .then(response => response.json())
    .then(responses =>{
        console.log(responses);
    });
  ```
  
 ## Organización
Para el backend del proyecto, se toman diferentes carpetas organizadas:
- URL's: Contiene todos los URLs de la aplicación ordenados en HTML y llamadas a API.
- Views: Contienen las funciones de renderizado de las páginas y la lógica de cada API creada en el framework Django.
- Models: Contiene los modelos de base de datos usados en el proyecto, extraidos del servidor de pruebas de BSale (Category y Product).
