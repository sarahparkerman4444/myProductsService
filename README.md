# "Products service (Django)"

## Overview

_Humanitec backend service for products and inventory. 
It provides the Product model and Property model. 
These models have many-to-many relation between them_


## Data models

### Product

A _Product_ has the following properties:

-  **uuid:** UUID of the product.
-  **name:** Name of the product.
-  **description:** Description of the product.
-  **workflowlevel2_uuid:** UUID of the workflow level 2 associated with the product.
-  **make:** Manufacturer of the product
-  **model:** Model of the product from the manufacturer
-  **style:** Distinguishing look or color of the product
-  **type:** Type of the product
-  **file:** File attached to the product (it could be specification or instruction)
-  **file_name:** File name for the attached file (if differs from original)
-  **status:** Status of the product (in-stock, on back order etc.)
-  **reference_id:** Unique ID for external tracking or third part data system

Endpoints:

-  `GET /products/`: Retrieves a list of products.
-  `POST /products/`: Creates a new product.
-  `GET /products/{uuid}/`: Retrieves a products by its UUID.
-  `PUT /products/{uuid}/`: Updates product with the given UUID (all field).
-  `PATCH /products/{uuid}/`: Updates product with the given UUID (only specified fields).
-  `DELETE /products/{uuid}/`: Deletes product with the given UUID.
-  `GET /products/{uuid}/file/`: Download the file attached to product with the given UUID.

[Click here for the full API documentation.](#point-this-link-to-swagger-docs)

### Property

A _Property_ provides the custom fields for a product, it has the following properties:

-  **product:** List of products associated with the property (many-to many relation).
-  **name:** Name of the property.
-  **value:** Value of the property.
-  **type:** Type of the property.

Endpoints:

-  `GET /property/`: Retrieves a list of properties.
-  `POST /property/`: Creates a new property.
-  `GET /property/{id}/`: Retrieves a property by its ID.
-  `PUT /property/{id}/`: Updates property with the given ID (all field).
-  `PATCH /property/{id}/`: Updates property with the given ID (only specified fields).
-  `DELETE /property/{id}/`: Deletes property with the given ID.

[Click here for the full API documentation.](#point-this-link-to-swagger-docs)

## Local development

<!-- Just Django instructions for now -->
Here are some instructions for developing this service locally:

### Prerequisites

You must have [Docker](https://www.docker.com/) installed.

### Build & run service locally

Build the Docker image:

```bash
docker-compose build
```

Run a web server with this service:

```bash
docker-compose up
```

Now, open your browser and go to [http://localhost:8080](http://localhost:8080).

For the admin panel, go to [http://localhost:8080/admin](http://localhost:8080/admin)
(user: `admin`, password: `admin`).

### Run tests

To run the tests once:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' {name-of-service}
```

To run the tests and leave bash open inside the container so that it's possible to
re-run the tests faster again using `bash scripts/run-tests.sh [--keepdb]`:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh --bash-on-finish' {name-of-service}
```

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' {name-of-service}
```

## API documentation (Swagger)

[Click here to go to the full API documentation.](/{path-to-the-api-docs})

## License

Copyright &#169;2019 Humanitec GmbH.

This code is released under the [Humanitec Affero GPL](LICENSE).
