{
    'name': 'Maximum Order Quantity',
    'version': '1.0',
    'category': 'eCommerce',
    'author': 'Ahex Technologies',
    'summary': 'Our app helps you set maximum order limits to protect stock and prevent bulk buying',
    'website': 'https://www.ahex.co',
    'description': """
Maximum Order Quantity for eCommerce
====================================
This module allows you to restrict the maximum order quantity of any product in your eCommerce store.

Key Features:
-------------
* **Admin-configurable limits:** Easily set maximum purchase limits for specific products directly from the product template form in the backend.
* **Front-end validation:** Prevents customers from increasing the quantity beyond the specified limit on the website product page.
* **Error message alerts:** Displays clear user-friendly notifications when users attempt to add or checkout with more than the allowed maximum quantity.
* **Cart-wide enforcement:** The maximum limit is verified and enforced dynamically on the cart page and throughout the checkout process.
* **Inventory protection:** Helps protect stock from bulk buyers, controls promotional abuse, and ensures a fairer distribution of high-demand items.
    """,
    'depends': ['base', 'web', 'sale', 'website_sale_stock', 'website_sale', 'website_sale_comparison'],
    'images': [
        'static/description/banner.png',
    ],
    'data': [
        'views/products_view.xml',
        'views/website_product_view.xml',
    ],
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
}
