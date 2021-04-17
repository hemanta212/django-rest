gen-schema:
	#DRF 3.2 only supports openapi otherwiser coreapi schema will be geenrated
	poetry run python manage.py generateschema > openapi-schema.yml
