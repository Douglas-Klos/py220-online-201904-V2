#!/usr/bin/env python3

import csv
import json

# After making this, I realize I have no use for it.
#   C'est la vie, was still fun to code.


def customers_csv_to_json():
    _f = open("./data/customers.csv", "r")
    reader = csv.DictReader(
        f,
        fieldnames=(
            "user_id",
            "name",
            "address",
            "zip_code",
            "phone_number",
            "email",
        ),
    )
    next(reader)
    out = json.dumps([row for row in reader])
    _f = open("./data/customers.json", "w")
    f.write(out)
    return out


def product_csv_to_json():
    _file = open("./data/product.csv", "r")
    reader = csv.DictReader(
        f,
        fieldnames=(
            "product_id",
            "description",
            "product_type",
            "quantity_available",
        ),
    )
    next(reader)
    out = json.dumps([row for row in reader])
    _f = open("./data/product.json", "w")
    f.write(out)
    return out


def rental_csv_to_json():
    _f = open("./data/rental.csv", "r")
    reader = csv.DictReader(f, fieldnames=("product_id", "user_id"))
    next(reader)
    out = json.dumps([row for row in reader])
    _f = open("./data/rental.json", "w")
    f.write(out)
    return out


def main():
    customers = customers_csv_to_json()
    product = product_csv_to_json()
    rental = rental_csv_to_json()

    for customer in customers.split("},"):
        print(customer + "},")

    for product in product.split("},"):
        print(product + "},")

    for rental in rental.split("},"):
        print(rental + "},")


if __name__ == "__main__":
    main()
