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
    global _next_id

    if request.method == "GET":
        return JsonResponse(_products, safe=False, status=200)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

        name = data.get("name")
        price = data.get("price")

        if not name or price is None:
            return JsonResponse(
                {"error": "Both 'name' and 'price' are required fields"},
                status=400
            )

        try:
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be positive")
        except (ValueError, TypeError):
            return JsonResponse({"error": "Price must be a positive number"}, status=400)

        new_product = {
            "id": _next_id,
            "name": str(name).strip(),
            "price": price,
            "stock": int(data.get("stock", 0))
        }
        _products.append(new_product)
        _next_id += 1

        return JsonResponse(new_product, status=201)

    return JsonResponse({"error": "Method not allowed"}, status=405)