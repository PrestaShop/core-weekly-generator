##
# List of PrestaShop employees or subcontractors
#
CORE_TEAM = (
    'PierreRambaud',      # Pierre R.
    'LittleBigDev',       # Bastien B.
    'Quetzacoalt91',      # Thomas N.
    'azouz-jribi',        # Azouz Jribi (Sifast)
    'eternoendless',      # Pablo B.
    'fatmaBouchekoua',    # Fatma B. (Sifast)
    'jocel1',             # Jocelyn F.
    'mickaelandrieu',     # Mickael A.
    'rGaillard',          # Remi G.
    'tomlev',             # Thomas L.
    'toutantic',          # Aurelien
    'slorenzini',         # Sarah L.
    'LouiseBonnard',      # Louise B.
    'ttoine',             # Antoine T.
    'colinegin',          # Coline G.
    'marionf',            # Marion F.
    'matks',              # Matthieu F.
    'khouloudbelguith',   # Khouloud B. (Sifast)
    'fouratachour',       # Fourat A.
    'sLorenzini',         # Sarah L.
    'apacios',            # Adrien P.
    'jolelievre',         # Jonathan L.
    'clementdaubeuf',     # Clement D.
    'MrBaiame',           # Alexis V.
    'Joukz',              # Julien G.
    'david-piatek',       # David P.
    'yelnatss',           # Marvin S.
    'CaptainYouz',        # Anas M.
    'Matt75',             # Matthias R.
    'SimonGrn',           # Simon G.
    'mbadrani',           # Mehdi B.
    'boubkerbribri',      # Boubker B.
    'matthieu-rolland',   # Matthieu R.
    'Progi1984',          # Franck L.
    'Robin-Fischer-PS',   # Robin F.
    'samuel-pires',       # Samuel P.
    'atomiix',            # Thomas B. 
    'NeOMakinG',          # Valentin S.
    'sowbiba',            # Ibrahima S.
)

##
# List of PrestaShop project repositories
#
PROJECTS = {
  # tools and libs
    'core-weekly-generator': 'Core Weekly Generator tool',
    'CsaGuzzleBundle': 'CsaGuzzle Bundle (fork)',
    'docker': 'Docker images',
    'docker-internal-images': 'Docker internal images',
    'docs': 'Changes in developer documentation',
    'php-coding-standards': 'PHP Coding Standards',
    'php-dev-tools': 'PHP Developer Tools',
    'prestashop-ui-kit': 'Prestashop UI Kit',
    'QANightlyResults': 'QA nightly results',
    'TranslationFiles': 'Translation Files repository',
    'TranslationToolsBundle': 'TranslationTools Bundle',
    'vagrant': 'PrestaShop Virtual Machine',
  # modules
    'autoupgrade': 'Auto Upgrade module',
    'blockreassurance': 'Customer reassurance block',
    'blockwishlist': 'Wishlist block',
    'contactform': 'Contact Form',
    'cronjobs': 'Cronjobs module',
    'dashactivity': 'Dashboard Activity module',
    'dashgoals': 'Dashboard Goals',
    'dashproducts': 'Dashboard Products',
    'dashtrends': 'Dashboard Trends',
    'decimal': 'Decimal',
    'example-modules': 'Example modules',
    'gadwords': 'Google Ads',
    'gamification': 'Gamification module',
    'gridhtml': 'Simple HTML table display',
    'gsitemap': 'Google Sitemap module',
    'graphnvd3': 'NVD3 Charts',
    'issuebot': 'Issue Bot',
    'open-source': 'The PrestaShop open source project',
    'nightly-board': 'Nightly board',
    'pagesnotfound': 'Pages not found',
    'productcomments': 'Product Comments module',
    'ps_banner': 'Banner',
    'ps_buybuttonlite': 'Buy button lite',
    'ps_cashondelivery': 'Cash on delivery',
    'ps_categoryproducts': 'Products in the same category',
    'ps_categorytree': 'Category tree links',
    'ps_checkpayment': 'Check payment',
    'ps_contactinfo': 'Contact informations module',
    'ps_crossselling': 'Cross-selling',
    'ps_currencyselector': 'Currency selector',
    'ps_customeraccountlinks': 'Customer account links',
    'ps_customersignin': 'Customer "Sign in" link',
    'ps_customtext': 'Custom text',
    'ps_dataprivacy': 'Customer data privacy block',
    'ps_faviconnotificationbo': 'Order Notifications on the Favicon',
    'ps_emailalerts': 'Email Alerts module',
    'ps_emailsubscription': 'Email subscription module',
    'ps_facetedsearch': 'Faceted search module',
    'ps_featuredproducts': 'Featured products',
    'ps_googleanalytics': 'Google Analytics module',
    'ps_imageslider': 'Image slider',
    'ps_languageselector': 'Language selector',
    'ps_linklist': 'Link list',
    'ps_livetranslation': 'Live translation',
    'ps_mainmenu': 'Main menu module',
    'ps_newproducts': 'New Products module',
    'ps_productinfo': 'Product tooltips',
    'ps_reminder': 'Reminder module',
    'ps_searchbar': 'Search Bar module',
    'ps_searchbarjqauto': 'Search bar autocomplete',
    'ps_sharebuttons': 'Share Buttons module',
    'ps_shoppingcart': 'Shopping cart module',
    'ps_socialfollow': 'Social Follow module',
    'ps_themecusto': 'Theme customization',
    'ps_wirepayment': 'Wire payment module',
    'pscleaner': 'PS Cleaner module',
    'psgdpr': 'PSGDPR',
    'sekeywords': 'Search engine keywords',
    'statsbestcategories': 'Best categories',
    'statsbestcustomers': 'Best customers',
    'statsbestmanufacturers': 'Best manufacturers',
    'statsbestproducts': 'Best-selling products',
    'statsbestsuppliers': 'Best suppliers',
    'statsbestvouchers': 'Best vouchers',
    'statscarrier': 'Carrier distribution',
    'statscatalog': 'Catalog statistics',
    'statscheckup': 'Catalog evaluation',
    'statsdata': 'Data mining for statistics',
    'statsequipment': 'Browsers and operating systems',
    'statsforecast': 'Stats Dashboard',
    'statslive': 'Visitors online',
    'statsnewsletter': 'Newsletter',
    'statsorigin': 'Visitors origin',
    'statspersonalinfos': 'Registered customer information',
    'statsproduct': 'Product details',
    'statsregistrations': 'Registrations statistics modules',
    'statssales': 'Sales and orders',
    'statssearch': 'Shop search',
    'statsstock': 'Available quantities',
    'statsvisits': 'Visits and Visitors',
    'vatnumber': 'European VAT number',
    'watermark': 'Watermark',
    'welcome': 'OnBoarding',
  # misc
    'ADR': 'Architecture Decision Records repository',
    'classic-rocket': 'Classic-rocket theme',
    'prestashop-specs': 'PrestaShop Specifications',
    'prestonbot': 'PrestonBot',
    'traces': 'Traces',
    'TopContributors': 'PrestaShop contributors website',
}

##
# List of PrestaShop Categories
#
CATEGORIES = {
    'CO': 'Core',
    'BO': 'Back office',
    'FO': 'Front office',
    'IN': 'Installer',
    'WS': 'Web services',
    'TE': 'Tests',
    'ME': 'Merge',
    'Misc': 'Misc',
}

CORE_BRANCHES = (
    'develop',
    '1.7.7.x',
    '1.7.6.x',
    '1.7.5.x',
    '1.7.4.x'
)
