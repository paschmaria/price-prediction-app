import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin

from .models import Car


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name_plural.capitalize()}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not \
                field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])

    # Write data rows
    for obj in queryset:
        data_row = []

        for field in fields:
            value = getattr(obj, field.name)

            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')

            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin):
    list_display = ['brand', 'model', 'fuel_type', 
                    'transmission', 'power', 'seats',
                    'price']
    list_filter = ['brand', 'model']
    actions = [export_to_csv]
