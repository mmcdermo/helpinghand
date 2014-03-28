
from django.conf.urls import include, patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('^api/login/$','main.middletier.login',name='login'),
    url('^api/logout/$','main.middletier.logout',name='logout'),
    url('^api/signup/$','main.middletier.signup',name='signup'),
    url('^api/page/Item/create/$','page.middletier.createItem',name='create_Item'),
    url('^api/page/Item/search/$','page.middletier.searchItem',name='search_Item'),
    url('^api/page/Page/create/$','page.middletier.createPage',name='create_Page'),
    url('^api/page/Page/search/$','page.middletier.searchPage',name='search_Page'),
    url('^getElement/(.{1,32})/$', 'page.middletier.getDisplayableElement',name='get element'),
    url('^/$','main.views.home',name='home'),
)
