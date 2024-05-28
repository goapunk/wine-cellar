# Generated by Django 5.0.1 on 2024-06-01 15:13

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import wine_cellar.apps.wine.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Classification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="FoodPairing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Grape",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("region_id", models.BigIntegerField(null=True)),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Wine",
            fields=[
                ("wine_id", models.BigIntegerField(null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "wine_type",
                    models.CharField(
                        choices=[
                            ("WH", "White"),
                            ("RE", "Red"),
                            ("RO", "Rose"),
                            ("SP", "Sparkling"),
                            ("DE", "Dessert"),
                            ("FO", "Fortified"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("DR", "Dry"),
                            ("SD", "Semi-Dry"),
                            ("MS", "Medium Sweet"),
                            ("SW", "Sweet"),
                            ("FH", "Feinherb"),
                        ],
                        max_length=2,
                    ),
                ),
                ("abv", models.FloatField()),
                ("capacity", models.FloatField(blank=True, null=True)),
                (
                    "vintage",
                    models.PositiveIntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2024),
                        ],
                    ),
                ),
                ("comment", models.CharField(blank=True, max_length=250)),
                (
                    "rating",
                    models.PositiveIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("AW", "Aruba"),
                            ("AF", "Afghanistan"),
                            ("AO", "Angola"),
                            ("AI", "Anguilla"),
                            ("AX", "Åland Islands"),
                            ("AL", "Albania"),
                            ("AD", "Andorra"),
                            ("AE", "United Arab Emirates"),
                            ("AR", "Argentina"),
                            ("AM", "Armenia"),
                            ("AS", "American Samoa"),
                            ("AQ", "Antarctica"),
                            ("TF", "French Southern Territories"),
                            ("AG", "Antigua and Barbuda"),
                            ("AU", "Australia"),
                            ("AT", "Austria"),
                            ("AZ", "Azerbaijan"),
                            ("BI", "Burundi"),
                            ("BE", "Belgium"),
                            ("BJ", "Benin"),
                            ("BQ", "Bonaire, Sint Eustatius and Saba"),
                            ("BF", "Burkina Faso"),
                            ("BD", "Bangladesh"),
                            ("BG", "Bulgaria"),
                            ("BH", "Bahrain"),
                            ("BS", "Bahamas"),
                            ("BA", "Bosnia and Herzegovina"),
                            ("BL", "Saint Barthélemy"),
                            ("BY", "Belarus"),
                            ("BZ", "Belize"),
                            ("BM", "Bermuda"),
                            ("BO", "Bolivia, Plurinational State of"),
                            ("BR", "Brazil"),
                            ("BB", "Barbados"),
                            ("BN", "Brunei Darussalam"),
                            ("BT", "Bhutan"),
                            ("BV", "Bouvet Island"),
                            ("BW", "Botswana"),
                            ("CF", "Central African Republic"),
                            ("CA", "Canada"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CH", "Switzerland"),
                            ("CL", "Chile"),
                            ("CN", "China"),
                            ("CI", "Côte d'Ivoire"),
                            ("CM", "Cameroon"),
                            ("CD", "Congo, The Democratic Republic of the"),
                            ("CG", "Congo"),
                            ("CK", "Cook Islands"),
                            ("CO", "Colombia"),
                            ("KM", "Comoros"),
                            ("CV", "Cabo Verde"),
                            ("CR", "Costa Rica"),
                            ("CU", "Cuba"),
                            ("CW", "Curaçao"),
                            ("CX", "Christmas Island"),
                            ("KY", "Cayman Islands"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czechia"),
                            ("DE", "Germany"),
                            ("DJ", "Djibouti"),
                            ("DM", "Dominica"),
                            ("DK", "Denmark"),
                            ("DO", "Dominican Republic"),
                            ("DZ", "Algeria"),
                            ("EC", "Ecuador"),
                            ("EG", "Egypt"),
                            ("ER", "Eritrea"),
                            ("EH", "Western Sahara"),
                            ("ES", "Spain"),
                            ("EE", "Estonia"),
                            ("ET", "Ethiopia"),
                            ("FI", "Finland"),
                            ("FJ", "Fiji"),
                            ("FK", "Falkland Islands (Malvinas)"),
                            ("FR", "France"),
                            ("FO", "Faroe Islands"),
                            ("FM", "Micronesia, Federated States of"),
                            ("GA", "Gabon"),
                            ("GB", "United Kingdom"),
                            ("GE", "Georgia"),
                            ("GG", "Guernsey"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GN", "Guinea"),
                            ("GP", "Guadeloupe"),
                            ("GM", "Gambia"),
                            ("GW", "Guinea-Bissau"),
                            ("GQ", "Equatorial Guinea"),
                            ("GR", "Greece"),
                            ("GD", "Grenada"),
                            ("GL", "Greenland"),
                            ("GT", "Guatemala"),
                            ("GF", "French Guiana"),
                            ("GU", "Guam"),
                            ("GY", "Guyana"),
                            ("HK", "Hong Kong"),
                            ("HM", "Heard Island and McDonald Islands"),
                            ("HN", "Honduras"),
                            ("HR", "Croatia"),
                            ("HT", "Haiti"),
                            ("HU", "Hungary"),
                            ("ID", "Indonesia"),
                            ("IM", "Isle of Man"),
                            ("IN", "India"),
                            ("IO", "British Indian Ocean Territory"),
                            ("IE", "Ireland"),
                            ("IR", "Iran, Islamic Republic of"),
                            ("IQ", "Iraq"),
                            ("IS", "Iceland"),
                            ("IL", "Israel"),
                            ("IT", "Italy"),
                            ("JM", "Jamaica"),
                            ("JE", "Jersey"),
                            ("JO", "Jordan"),
                            ("JP", "Japan"),
                            ("KZ", "Kazakhstan"),
                            ("KE", "Kenya"),
                            ("KG", "Kyrgyzstan"),
                            ("KH", "Cambodia"),
                            ("KI", "Kiribati"),
                            ("KN", "Saint Kitts and Nevis"),
                            ("KR", "Korea, Republic of"),
                            ("KW", "Kuwait"),
                            ("LA", "Lao People's Democratic Republic"),
                            ("LB", "Lebanon"),
                            ("LR", "Liberia"),
                            ("LY", "Libya"),
                            ("LC", "Saint Lucia"),
                            ("LI", "Liechtenstein"),
                            ("LK", "Sri Lanka"),
                            ("LS", "Lesotho"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("LV", "Latvia"),
                            ("MO", "Macao"),
                            ("MF", "Saint Martin (French part)"),
                            ("MA", "Morocco"),
                            ("MC", "Monaco"),
                            ("MD", "Moldova, Republic of"),
                            ("MG", "Madagascar"),
                            ("MV", "Maldives"),
                            ("MX", "Mexico"),
                            ("MH", "Marshall Islands"),
                            ("MK", "North Macedonia"),
                            ("ML", "Mali"),
                            ("MT", "Malta"),
                            ("MM", "Myanmar"),
                            ("ME", "Montenegro"),
                            ("MN", "Mongolia"),
                            ("MP", "Northern Mariana Islands"),
                            ("MZ", "Mozambique"),
                            ("MR", "Mauritania"),
                            ("MS", "Montserrat"),
                            ("MQ", "Martinique"),
                            ("MU", "Mauritius"),
                            ("MW", "Malawi"),
                            ("MY", "Malaysia"),
                            ("YT", "Mayotte"),
                            ("NA", "Namibia"),
                            ("NC", "New Caledonia"),
                            ("NE", "Niger"),
                            ("NF", "Norfolk Island"),
                            ("NG", "Nigeria"),
                            ("NI", "Nicaragua"),
                            ("NU", "Niue"),
                            ("NL", "Netherlands"),
                            ("NO", "Norway"),
                            ("NP", "Nepal"),
                            ("NR", "Nauru"),
                            ("NZ", "New Zealand"),
                            ("OM", "Oman"),
                            ("PK", "Pakistan"),
                            ("PA", "Panama"),
                            ("PN", "Pitcairn"),
                            ("PE", "Peru"),
                            ("PH", "Philippines"),
                            ("PW", "Palau"),
                            ("PG", "Papua New Guinea"),
                            ("PL", "Poland"),
                            ("PR", "Puerto Rico"),
                            ("KP", "Korea, Democratic People's Republic of"),
                            ("PT", "Portugal"),
                            ("PY", "Paraguay"),
                            ("PS", "Palestine, State of"),
                            ("PF", "French Polynesia"),
                            ("QA", "Qatar"),
                            ("RE", "Réunion"),
                            ("RO", "Romania"),
                            ("RU", "Russian Federation"),
                            ("RW", "Rwanda"),
                            ("SA", "Saudi Arabia"),
                            ("SD", "Sudan"),
                            ("SN", "Senegal"),
                            ("SG", "Singapore"),
                            ("GS", "South Georgia and the South Sandwich Islands"),
                            ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                            ("SJ", "Svalbard and Jan Mayen"),
                            ("SB", "Solomon Islands"),
                            ("SL", "Sierra Leone"),
                            ("SV", "El Salvador"),
                            ("SM", "San Marino"),
                            ("SO", "Somalia"),
                            ("PM", "Saint Pierre and Miquelon"),
                            ("RS", "Serbia"),
                            ("SS", "South Sudan"),
                            ("ST", "Sao Tome and Principe"),
                            ("SR", "Suriname"),
                            ("SK", "Slovakia"),
                            ("SI", "Slovenia"),
                            ("SE", "Sweden"),
                            ("SZ", "Eswatini"),
                            ("SX", "Sint Maarten (Dutch part)"),
                            ("SC", "Seychelles"),
                            ("SY", "Syrian Arab Republic"),
                            ("TC", "Turks and Caicos Islands"),
                            ("TD", "Chad"),
                            ("TG", "Togo"),
                            ("TH", "Thailand"),
                            ("TJ", "Tajikistan"),
                            ("TK", "Tokelau"),
                            ("TM", "Turkmenistan"),
                            ("TL", "Timor-Leste"),
                            ("TO", "Tonga"),
                            ("TT", "Trinidad and Tobago"),
                            ("TN", "Tunisia"),
                            ("TR", "Türkiye"),
                            ("TV", "Tuvalu"),
                            ("TW", "Taiwan, Province of China"),
                            ("TZ", "Tanzania, United Republic of"),
                            ("UG", "Uganda"),
                            ("UA", "Ukraine"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("UY", "Uruguay"),
                            ("US", "United States"),
                            ("UZ", "Uzbekistan"),
                            ("VA", "Holy See (Vatican City State)"),
                            ("VC", "Saint Vincent and the Grenadines"),
                            ("VE", "Venezuela, Bolivarian Republic of"),
                            ("VG", "Virgin Islands, British"),
                            ("VI", "Virgin Islands, U.S."),
                            ("VN", "Viet Nam"),
                            ("VU", "Vanuatu"),
                            ("WF", "Wallis and Futuna"),
                            ("WS", "Samoa"),
                            ("YE", "Yemen"),
                            ("ZA", "South Africa"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "stock",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WineImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=wine_cellar.apps.wine.models.user_directory_path
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Winery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("winery_id", models.BigIntegerField(null=True)),
                ("name", models.CharField(max_length=100)),
                ("website", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name="classification",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique classification"
            ),
        ),
        migrations.AddConstraint(
            model_name="foodpairing",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique food pairing"
            ),
        ),
        migrations.AddConstraint(
            model_name="grape",
            constraint=models.UniqueConstraint(fields=("name",), name="unique grape"),
        ),
        migrations.AddConstraint(
            model_name="region",
            constraint=models.UniqueConstraint(
                fields=("name", "country"), name="unique region"
            ),
        ),
        migrations.AddField(
            model_name="wine",
            name="classification",
            field=models.ManyToManyField(to="wine.classification"),
        ),
        migrations.AddField(
            model_name="wine",
            name="food_pairings",
            field=models.ManyToManyField(to="wine.foodpairing"),
        ),
        migrations.AddField(
            model_name="wine",
            name="grapes",
            field=models.ManyToManyField(to="wine.grape"),
        ),
        migrations.AddField(
            model_name="wine",
            name="region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wine.region",
            ),
        ),
        migrations.AddField(
            model_name="wine",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="wineimage",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="wineimage",
            name="wine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wine.wine"
            ),
        ),
        migrations.AddField(
            model_name="winery",
            name="region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wine.region",
            ),
        ),
        migrations.AddField(
            model_name="wine",
            name="winery",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wine.winery",
            ),
        ),
        migrations.AddConstraint(
            model_name="winery",
            constraint=models.UniqueConstraint(
                fields=("name", "region"), name="unique winery"
            ),
        ),
        migrations.AddConstraint(
            model_name="wine",
            constraint=models.UniqueConstraint(
                fields=(
                    "name",
                    "wine_type",
                    "abv",
                    "capacity",
                    "winery",
                    "vintage",
                    "country",
                ),
                name="unique wine",
            ),
        ),
    ]
