from django.conf.urls import url
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from views import IPN
from django.core.urlresolvers import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from . import forms
from . import views

urlpatterns = [
    url(r'^$', views.home, name='main_page'),
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/buyer/', views.register_buyer, name='register_buyer'),
    url(r'^register/publisher/', views.register_publisher, name='register_publisher'),
    url(r'^password_reset/$',
        auth_views.password_reset,
        {'post_reset_redirect' : reverse_lazy('main:reset_done'),
         'template_name': 'new/password_reset/form.html',
         'email_template_name': 'new/password_reset/email.html',
         'password_reset_form': forms.PassResetForm},
        name="password_reset"),
    url(r'^reset_done/$',
        auth_views.password_reset_done,
        {'template_name': 'new/password_reset/done.html',},
        name='reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z_\-]+)/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect' : reverse_lazy('main:reset_complete'),
        'template_name': 'new/password_reset/confirm.html',
         'set_password_form': forms.SetPassForm,
         },
        name='password_reset_confirm'),
    url(r'^reset_complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'new/password_reset/complete.html'},
        name='reset_complete'),
    url(r'^new_account/(?P<network>[\w]+)/$', views.new_account,
        name='new_account'),
    url(r'^authenticate_successful/(?P<network>[\w]+)/$', views.authenticate_successful,
        name='authenticate_successful'),
    url(r'^account_overview/(?P<network>[\w]+)/(?P<model_id>[\d]+)/$', views.account_overview,
        name='account_overview'),
    url(r'^edit_account/(?P<network>[\w]+)/(?P<model_id>[\d]+)/$', views.edit_account,
        name='edit_account'),
    url(r'^accounts_page/(?P<network>\w+)/$', views.accounts_page,
        name='accounts_page'),
    url(r'^account_detail/$', views.account_detail,
        name='account_detail'),
    url(r'^get_uses/$', views.get_uses, name='get_uses'),
    url(r'^open_account/$', views.open_account, name='open_account'),
    url(r'^tos/', views.tos, name='tos'),
    url(r'^403/$', views.permission_denied, name='perm_denied'),
    url(r'^gen_pdf_ig/', views.gen_pdf_ig, name='gen_pdf_ig'),
    url(r'^gen_pdf_tw/', views.gen_pdf_tw, name='gen_pdf_tw'),
    url(r'^gen_pdf_ig_new/', views.gen_pdf_ig_new, name='gen_pdf_ig_new'),
    url(r'^instagram_invoice/', views.instagram_invoice,
        name='instagram_invoice'),
    url(r'^generate_instagram_invoice/', views.generate_instagram_invoice,
        name='generate_instagram_invoice'),
    url(r'^oauth/(?P<network>[\w]+)/$', views.oauth_redirect, name='oauth'),
    url(r'^subscribe/$', views.buy_subscription, name='subscribe'),
    url(r'^jvzipn/$', views.jvzipn, name='jvzipn'),
    url(r'^payment_success/$', views.payment_success, name='payment_success'),
    url(r'^search/suggest/$', views.search_autocomplete, name='autocomplete'),
]