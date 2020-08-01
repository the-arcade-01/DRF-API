# DRF-API
## Description
An API backend for an application with entity relation table.

<b>Country</b><br>
key | Data type | Description
------------ | ------------- | -------------
id | Primary Key | 
Name | Character Field | Name of the country
Description | Text Field | Description of country
Population | Integer Field |
GDP | Float Field |

<b>State</b><br>
key | Data type | Description
------------ | ------------- | -------------
id | Primary Key | 
Country | Foreign Key | Relation to country
Name | Character Field | Name of the state
Description | Text Field | Description of state
Population | Integer Field |
GDP | Float Field |

<b>City</b><br>
key | Data type | Description
------------ | ------------- | -------------
id | Primary Key | 
State | Foreign Key | Relation to State
Country | Foreign Key | Relation to Country
Name | Character Field | Name of the city
Description | Text Field | Description of city
Population | Integer Field |
GDP | Float Field |
Pin Code | Character Field |

<b>Town</b><br>
key | Data type | Description
------------ | ------------- | -------------
id | Primary Key | 
State | Foreign Key | Relation to State
Country | Foreign Key | Relation to Country
Name | Character Field | Name of the Town
Description | Text Field | Description of Town
Population | Integer Field |
GDP | Float Field |
Pin Code | Character Field |

<b>Person</b><br>
key | Data type | Description
------------ | ------------- | -------------
id | Primary Key | 
Name | Character Field | Name of the Person
State | Foreign Key | Relation to State
Country | Foreign Key | Relation to Country
City | Foreign Key | Relation to city
Town | Foreign Key | Relation to town
## Setup
1. Initial Setup
- Clone this repository : `https://github.com/the-arcade-01/DRF-API.git`
- Install Requirements : `pip install -r requirements.txt`
2. Backend Setup
- cd to Backend and run following sets of commands
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Create super user by `python manage.py createsuperuser`<br>
<b>NOTE: API required Basic Authentication, creating superuser is must</b><br>
## API Overview
API url set
```
admin/
country-viewset/
country-viewset/<int:id>/
state-viewset/
state-viewset/<int:id>/
city-viewset/
city-viewset/<int:id>/
town-viewset/
town-viewset/<int:id>/
person-viewset/
person-viewset/<int:id>/

```
1. Country Viewset
URLs:
- For entire data with Pagination `http://127.0.0.1:8000/country-viewset/`
- For individual data `http://127.0.0.1:8000/country-viewset/<int:id>/`<br>

Response examples:
```javascript
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 3,
    "next": "http://127.0.0.1:8000/country-viewset/api/?page=2",
    "previous": null,
    "results": [
        {
            "id": 8,
            "name": "India",
            "description": "India is a diverse country",
            "population": 1300,
            "gdp": 3.202,
            "state_country": [
                {
                    "id": 12,
                    "country": 8,
                    "name": "Madhya Pradesh",
                    "description": "Central state of India",
                    "population": 45,
                    "gdp": 0.002,
                    "city_state": [
                        {
                            "id": 6,
                            "country": 8,
                            "state": 12,
                            "name": "Bhopal",
                            "description": "City of Lakes",
                            "population": 20,
                            "gdp": 0.00134,
                            "pin_code": "400001",
                            "person_city": [
                                {
                                    "id": 6,
                                    "name": "Anish",
                                    "country": 8,
                                    "state": 12,
                                    "city": 6,
                                    "town": 4
                                }
                            ]
                        }
                    ],
                    "town_state": [
                        {
                            "id": 4,
                            "country": 8,
                            "state": 12,
                            "name": "GandhiNagar",
                            "description": "Town in MP",
                            "population": 5,
                            "gdp": 0.00015,
                            "pin_code": "400101",
                            "person_town": [
                                {
                                    "id": 6,
                                    "name": "Anish",
                                    "country": 8,
                                    "state": 12,
                                    "city": 6,
                                    "town": 4
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 11,
                    "country": 8,
                    "name": "Maharashtra",
                    "description": "Jai Maharashtra!!",
                    "population": 123,
                    "gdp": 0.0034,
                    "city_state": [],
                    "town_state": []
                }
            ]
        }
    ]
}
```
2. Person Viewset
URLs:
- For entire data with Pagination `http://127.0.0.1:8000/person-viewset/`
- For individual data `http://127.0.0.1:8000/person-viewset/<int:id>/`<br>

Response examples:
 - Url : `/person-viewset/api/?page=2`
```javascript
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 4,
    "next": "http://127.0.0.1:8000/person-viewset/api/?page=3",
    "previous": "http://127.0.0.1:8000/person-viewset/api/",
    "results": [
        {
            "id": 6,
            "name": "Anish",
            "country": 8,
            "state": 12,
            "city": 6,
            "town": 4
        }
    ]
}
```
- Ordering and Search Filter Response : `/person-viewset/api/?ordering=name&search=India`

Ordering on Person Name and Search Filter on Country Name
```javascript
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": "http://127.0.0.1:8000/person-viewset/api/?ordering=name&page=2&search=India",
    "previous": null,
    "results": [
        {
            "id": 6,
            "name": "Anish",
            "country": 8,
            "state": 12,
            "city": 6,
            "town": 4
        }
    ]
}
```
## Postman Collection
Postman Collections can be found [Here](https://github.com/the-arcade-01/DRF-API/tree/master/Postman%20Collections)
## Tasks
- [X] API for Country, City, Town, State and Person
- [X] CRUD for all
- [X] ModelSerializer with Nested serializer
- [X] Person relation with City and Town
- [X] Pagination API for all
- [X] Filter, Ordering and Searching for Person based on related keys
- [X] selected_related() for speeding queries
- [X] Postman Collections for all API
- [X] Implemented views using ModelViewSet
- [X] Comments and modular code

### Created By [AASHISH RAMESH KOSHTI](https://github.com/the-arcade-01)
