from django.core.management.base import BaseCommand, no_translations
import requests
from django.core.exceptions import ObjectDoesNotExist
from search.models import Category, Product


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        dic = ["Produits à tartiner", "Plats préparés", "Céréales pour petit-déjeuner", "Pizzas", "Confiseries",
               "Boissons"]
        cpt = 0
        cpt_product = 0
        cpt_boucle = 0
        while len(dic) > cpt:
            category = Category(name=dic[cpt])
            print(category.name)
            category.save()
            cpt += 1

        while cpt_boucle <= 5:
            while cpt_product < 100:
                try:
                    r = requests.get("https://fr.openfoodfacts."
                                     "org/cgi/search.pl?action=process"
                                     "&tagtype_0=categories&tag_contains_"
                                     "0=contains&tag_0=" + str(dic[cpt_boucle]) + "&json=true&page_size=200")
                    results = r.json()["products"]
                    name = results[cpt_product]["product_name"]
                    score = results[cpt_product]["nutriscore_grade"]
                    img_url = results[cpt_product]["image_small_url"]
                    url = results[cpt_product]["url"]
                    ingredients = results[cpt_product]["ingredients_text_fr"]

                    print(name, score, img_url)
                    cpt_product += 1
                    print(cpt_product)
                    try:
                        Product.objects.get(name=name)
                    except ObjectDoesNotExist:
                        cat = Category.objects.get(id=cpt_boucle + 1)
                        product_add = Product(name=name, score=score, img_url=img_url, category_product=cat, url=url,
                                              ingredient=ingredients)
                        product_add.save()

                except KeyError:
                    r = requests.get("https://fr.openfoodfacts."
                                     "org/cgi/search.pl?action=process"
                                     "&tagtype_0=categories&tag_contains_"
                                     "0=contains&tag_0=" + str(dic[cpt_boucle]) + "&json=true&page_size=200")
                    results = r.json()["products"]
                    name = results[cpt_product]["product_name"]
                    score = 'e'
                    try:
                        img_url = results[cpt_product]["image_thumb_url"]
                    except KeyError:
                        img_url = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    print(name, score, img_url)
                    cpt_product += 1
                    print(cpt_product)
                    try:
                        Product.objects.get(name=name)
                    except ObjectDoesNotExist:
                        cat = Category.objects.get(id=cpt_boucle + 1)
                        product_add = Product(name=name, score=score, img_url=img_url, category_product=cat, url=url,
                                              ingredient=ingredients)
                        product_add.save()

            cpt_product = 0
            cpt_boucle += 1
