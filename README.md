+++
title = "Products service (Django)"
api_url = "marketplace/products-service"
+++

# Products service (Django)

## Overview

The products service provides the backend for a products and inventory feature for your app. It exposes the **Product** and **Property** data models. These data models have a many-to-many relationship.

## Data models

### Product

A **Product** is a type of product. It includes the following properties:

-  **uuid:** UUID of the product.
-  **name:** Name of the product.
-  **description:** Description of the product.
-  **workflowlevel2_uuid:** UUID of the workflow level 2 associated with the product.
-  **make:** Manufacturer of the product.
-  **model:** Model of the product from the manufacturer.
-  **style:** Distinguishing look or color of the product.
-  **type:** Type of the product.
-  **file:** File attached to the product (e.g., a product specification or instruction manual).
-  **file_name:** Name of the attached file (if it should differ from the original).
-  **status:** Status of the product (e.g., "in stock", "on back order", etc.).
-  **reference_id:** Unique ID for external tracking or third party data system.

Endpoints:

-  `GET /products/`: Retrieves a list of products.
-  `POST /products/`: Creates a new product.
-  `GET /products/{uuid}/`: Retrieves a products by its UUID.
-  `PUT /products/{uuid}/`: Updates the product with the given UUID (all field).
-  `PATCH /products/{uuid}/`: Updates the product with the given UUID (only specified fields).
-  `DELETE /products/{uuid}/`: Deletes the product with the given UUID.
-  `GET /products/{uuid}/file/`: Retrieves the file attached to the product with the given UUID.

[Click here for the full API documentation.](https://docs.walhall.io/api/marketplace/products-service)

### Property

A **Property** is a custom field for a product. It includes the following properties:

-  **product:** List of products associated with the property (many-to-many relation).
-  **name:** Name of the property.
-  **value:** Value of the property.
-  **type:** Type of the property.

Endpoints:

-  `GET /property/`: Retrieves a list of properties.
-  `POST /property/`: Creates a new property.
-  `GET /property/{id}/`: Retrieves a property by its ID.
-  `PUT /property/{id}/`: Updates the property with the given ID (all fields).
-  `PATCH /property/{id}/`: Updates the property with the given ID (only specified fields).
-  `DELETE /property/{id}/`: Deletes the property with the given ID.

[Click here for the full API documentation.](https://docs.walhall.io/api/marketplace/products-service)

## Local development

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

<!-- ## BiFrost API implementation

-  How does this service connect to BiFrost?
-  How does it use the core data model? -->

## License

Copyright &#169;2019 Humanitec GmbH.

This code is released under the Humanitec Affero GPL. See the **LICENSE** file for details.
