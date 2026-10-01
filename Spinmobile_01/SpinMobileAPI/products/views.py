import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# In-memory "database" — the same list-of-dicts pattern from Week 3
_products = [
    {"id": 1, "name": "Wireless Mouse", "price": 1500.00, "stock": 50},
    {"id": 2, "name": "Keyboard", "price": 3200.00, "stock": 30},
    {"id": 3, "name": "USB-C Cable", "price": 500.00, "stock": 100},
]
_next_id = 4   # tracks the next ID to assign

@csrf_exempt
def product_list(request):
    """ GET  /api/products/ — return all products
    POST /api/products/ — create a new product """
    if request.method == "GET":
        return JsonResponse(_products, safe=False, status=200)

    return JsonResponse({"error": "Method not allowed"}, status=405)