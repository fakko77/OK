from django.test import TestCase
from search.models import Category, Product, Favorite


class TestProduct(TestCase):

    def test_product_category(self):
        """Test for check category"""
        category = Category.objects.create(name="Test")
        objectTest = Product.objects.create(name="objectTest", score="A", img_url="", url="", ingredient="",
                                            category_product=category)
        self.assertEqual(objectTest.categoryName(), "Test")

    def test_product_score(self):
        """Test for score is not equal"""
        objectTest = Product.objects.create(name="objectTest1", score="A", img_url="", url="", ingredient="")
        objectTest1 = Product.objects.create(name="objectTest2", score="B", img_url="", url="", ingredient="")
        self.assertNotEqual(objectTest.score, objectTest1.score)

    def test_product_name(self):
        """Test for name is not equal"""
        objectTest = Product.objects.create(name="objectTest1", score="A", img_url="", url="", ingredient="")
        objectTest1 = Product.objects.create(name="objectTest2", score="B", img_url="", url="", ingredient="")
        self.assertNotEqual(objectTest, objectTest1)


class TestFavorite(TestCase):

    def test_favorite_match(self):
        """Test for check if product name of product is correctly """
        fav = Favorite.objects.create(user=1)
        objectTest = Product.objects.create(name="objectTest1", score="A", img_url="", url="", ingredient="")
        fav.products.add(objectTest)
        self.assertEqual(fav.products.name, objectTest.favorites.name)

