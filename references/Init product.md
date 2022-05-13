# Insert Data via models.py in Django

```python
from products.models import Product

Product.objects.create(title='Hello World', content='This is awesome', price=10.99)
Product.objects.create(title='Hello World Again', content='This is awesome', price=12.99)
```
