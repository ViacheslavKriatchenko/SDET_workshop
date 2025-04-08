from faker import Faker

faker = Faker()

body = {
        "addition": {
            "additional_info": faker.random_element(['что', 'здесь', 'происходит']),
            "additional_number": faker.random_number(digits=3),
        },
        "important_numbers": [
            7,
            17,
            27
            ],
        "title": faker.random_element(['кино', 'вино', 'домино']),
        "verified": True,
}

update_body = {
        "addition": {
            "additional_info": faker.random_element(['que', 'здесь', 'происходит']),
            "additional_number": faker.random_number(digits=3),
        },
        "important_numbers": [
            8,
            18,
            27
            ],
        "title": faker.random_element(['кино', 'вино', 'домино']),
        "verified": True,
}
