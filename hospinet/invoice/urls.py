# -*- coding: utf-8 -*-
#
# Copyright (C) 2011-2013 Carlos Flores <cafg10@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url
from invoice.views import (IndexView, ReciboPersonaCreateView, ReciboAnularView,
     ReciboDetailView, VentaCreateView, ReporteReciboView, ReporteProductoView,
     ReciboRemiteView, ReciboRadView, EmergenciaPeriodoView, ReciboCerrarView,
     ReciboExamenCreateView, EmergenciaDiaView, AdmisionAltaView,
    EmergenciaFacturarView, AdmisionFacturarView)

urlpatterns = patterns('',
    
    url(r'^$',
        IndexView.as_view(),
        name='invoice-index'),

    url(r'^(?P<persona>\d+)/crear',
        ReciboPersonaCreateView.as_view(),
        name='invoice-create'),

    url(r'^examen/(?P<examen>\d+)/crear',
        ReciboExamenCreateView.as_view(),
        name='invoice-create-examen'),
    
    url(r'^(?P<pk>\d+)$',
        ReciboDetailView.as_view(),
        name='invoice-view-id'),
    
    url(r'^(?P<pk>\d+)/anular$',
        ReciboAnularView.as_view(),
        name='invoice-nullify'),

    url(r'^(?P<pk>\d+)/cerrar$',
        ReciboCerrarView.as_view(),
        name='invoice-close'),
    
    url(r'^(?P<recibo>\d+)/venta/add$',
        VentaCreateView.as_view(),
        name='venta-add'),

    url(r'^periodo$',
        ReporteReciboView.as_view(),
        name='invoice-periodo'),

    url(r'^periodo/producto$',
        ReporteProductoView.as_view(),
        name='invoice-periodo-producto'),

    url(r'^periodo/remite',
        ReciboRemiteView.as_view(),
        name='invoice-periodo-remite'),

    url(r'^periodo/radiologo',
        ReciboRadView.as_view(),
        name='invoice-periodo-radiologo'),

    url(r'^periodo/emergencia',
        EmergenciaPeriodoView.as_view(),
        name='invoice-periodo-emergencia'),

    url(r'^dia/emergencia',
        EmergenciaDiaView.as_view(),
        name='invoice-dia-emergencia'),

    url(r'^dia/altas',
        AdmisionAltaView.as_view(),
        name='invoice-dia-altas'),
    
    url(r'^emergencia/(?P<pk>\d+)$',
        EmergenciaFacturarView.as_view(),
        name='emergency-invoice'),
    
    url(r'^admision/(?P<pk>\d+)$',
        AdmisionFacturarView.as_view(),
        name='admision-invoice'),
)
