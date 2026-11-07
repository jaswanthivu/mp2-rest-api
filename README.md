# MP2 Data Processing API

This project is a FastAPI app that lets users upload CSV files, store them in memory, view the data, and process datasets using different cleaning and validation settings.

The processing options include checking required and numeric columns, removing duplicates, handling missing values, and working with outliers. I reused the data-processing functions from MP1 and connected them to the API through a new processing endpoint.

I also added middleware that creates a request ID for each request, logs the request status and duration, and returns the same request ID in the response headers.

The project includes pytest tests for uploading a CSV, processing and retrieving a dataset, and handling a request for a dataset that does not exist.