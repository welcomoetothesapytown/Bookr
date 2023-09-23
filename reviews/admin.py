from django.contrib.admin import AdminSite
from reviews.models import (Publisher, Contributor,Book, BookContributor, Review)

class BookrAdminSite(AdminSite):
    title_head="Bookr Admin"
    site_header = "Bookr Adminstration"
    index_title= "Boook site admin"

admin_site=BookrAdminSite(name="bookr")
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)



# Register your models here.
