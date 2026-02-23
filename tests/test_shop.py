import pytest
from django.contrib.auth.models import User
from shop.models import Category, Product, Tag
from orders.models import Order, OrderItem


@pytest.mark.django_db
def test_category_creation():
    """Test 1: Category model creation"""
    category = Category.objects.create(
        name='Electronics',
        slug='electronics',
        description='Electronic devices'
    )
    assert category.name == 'Electronics'
    assert str(category) == 'Electronics'
    assert Category.objects.count() == 1


@pytest.mark.django_db
def test_product_category_relationship():
    """Test 2: Many-to-One relationship (Product → Category)"""
    category = Category.objects.create(name='Books', slug='books')
    product = Product.objects.create(
        name='Django Book',
        slug='django-book',
        price=29.99,
        stock=10,
        category=category
    )
    assert product.category == category
    assert product in category.products.all()
    assert category.products.count() == 1


@pytest.mark.django_db
def test_product_tags_many_to_many():
    """Test 3: Many-to-Many relationship (Product ↔ Tag)"""
    category = Category.objects.create(name='Tech', slug='tech')
    product = Product.objects.create(
        name='Laptop',
        slug='laptop',
        price=999.99,
        category=category
    )
    tag1 = Tag.objects.create(name='new')
    tag2 = Tag.objects.create(name='sale')
    
    product.tags.add(tag1, tag2)
    
    assert product.tags.count() == 2
    assert tag1 in product.tags.all()
    assert tag2 in product.tags.all()


@pytest.mark.django_db
def test_order_creation_with_items():
    """Test 4: Order with OrderItems and total calculation"""
    user = User.objects.create_user('testuser', password='pass123')
    category = Category.objects.create(name='Food', slug='food')
    product1 = Product.objects.create(
        name='Pizza',
        slug='pizza',
        price=15.00,
        category=category
    )
    product2 = Product.objects.create(
        name='Soda',
        slug='soda',
        price=3.00,
        category=category
    )
    
    order = Order.objects.create(user=user, address='123 Main St')
    OrderItem.objects.create(order=order, product=product1, price=15.00, quantity=2)
    OrderItem.objects.create(order=order, product=product2, price=3.00, quantity=3)
    
    assert order.get_total() == 39.00  # (15*2) + (3*3)
    assert order.items.count() == 2


@pytest.mark.django_db
def test_product_availability():
    """Test 5: Product availability filtering"""
    category = Category.objects.create(name='Clothing', slug='clothing')
    Product.objects.create(
        name='Shirt',
        slug='shirt',
        price=25.00,
        category=category,
        available=True
    )
    Product.objects.create(
        name='Pants',
        slug='pants',
        price=40.00,
        category=category,
        available=False
    )
    
    available_products = Product.objects.filter(available=True)
    assert available_products.count() == 1
    assert available_products.first().name == 'Shirt'


@pytest.mark.django_db
def test_homepage_loads(client):
    """Test 6: Homepage returns 200 status"""
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_checkout_requires_login(client):
    """Test 7: Checkout redirects unauthenticated users"""
    response = client.get('/orders/create/')
    assert response.status_code == 302  # Redirect
    assert '/accounts/login/' in response.url