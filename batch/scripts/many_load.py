import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, ISO, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    ISO.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justification, year, longtitude, latitude, area_hectares, category, state, region, iso
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        try:
            y = int(row[3])
        except:
            y = None
        try:
            a = float(row[6])
        except:
            a = None
        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = ISO.objects.get_or_create(name=row[10])


        ss = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=row[4], latitude=row[5], area_hectares=a,category=c, state=s, region=r, iso=i)
        ss.save()
