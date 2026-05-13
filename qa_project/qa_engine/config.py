SPECIAL_CHAR_PATTERN = r'[@™©®ﾮ]'
URL_PATTERN = r'https?://\S+|www\.\S+'

FIXED_REQUIRED_COLUMNS = [
    "SKU",
    "MFRPart #",
    "Price",
    "Availability",
    "Description #1",
    "Description #2",
    "Product Page URL",
    "Image URL"
]

URL_COLUMNS = [
    "Product Page URL",
    "Image URL"
]

UNIQUE_COLUMNS = [
    "SKU",
    "MFRPart #",
    "Description #1"
]