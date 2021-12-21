import csv
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product, Category, Author

with open('books.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        print(row)
        category = Category.objects.get_or_create(name=row['Category'])[0]
        author = Author.objects.get_or_create(name=row['Author'])[0]
        product = Product.objects.get_or_create(name=row['Name'],
        price=row['Price'],
        author=author, 
        category=category)
        
        