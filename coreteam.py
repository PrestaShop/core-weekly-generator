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
    'Julievrz',           # Julie V.
)

##
# List of PrestaShop project repositories
#
PROJECTS = {
    # tools and libs
    'core-weekly-generator': 'Core Weekly Generator tool',
    'CsaGuzzleBundle': 'CsaGuzzle Bundle (fork)',
    'docker': 'Docker images',
    'docker-ci': 'PrestaShop on Docker',
    'docker-internal-images': 'Docker internal images',
    'docs': 'Changes in developer documentation',
    'php-coding-standards': 'PHP Coding Standards',
    'php-dev-tools': 'PHP Developer Tools',
    'prestashop-ui-kit': 'Prestashop UI Kit',
    'QANightlyResults': 'QA nightly results',
    'TranslationFiles': 'Translation Files repository',
    'TranslationToolsBundle': 'TranslationTools Bundle',
    'vagrant': 'PrestaShop Virtual Machine',
    'decimal': 'Decimal',
    'example-modules': 'Example modules',
    'example_module_mailtheme': 'Mail theme example',
    'PrestaShop-modules': 'PrestaShop modules registry',
    'issuebot': 'Issues Bot',
    'PrestaShop-webservice-lib': 'Webservices PHP Client',
    'stylelint-config': 'stylelint configuration',
    'eslint-config': 'eslint configuration',
    'jquery.live-polyfill': 'jQuery Live Polyfill library',
    'stylelint-browser-compatibility': 'Stylelint browser compatibility plugin',
    'mjml-theme-converter': 'MJML Theme Converter',
    # modules
    'autoupgrade': 'Auto Upgrade module',
    'blockreassurance': 'Customer reassurance block module',
    'blockwishlist': 'Wishlist block module',
    'contactform': 'Contact Form module',
    'cronjobs': 'Cronjobs module',
    'dashactivity': 'Dashboard Activity module',
    'dashgoals': 'Dashboard Goals module',
    'dashproducts': 'Dashboard Products module',
    'dashtrends': 'Dashboard Trends module',
    'gadwords': 'Google Ads module',
    'gamification': 'Gamification module',
    'gridhtml': 'Simple HTML table display module',
    'gsitemap': 'Google Sitemap module',
    'graphnvd3': 'NVD3 Charts module',
    'nightly-board': 'Nightly board',
    'pagesnotfound': 'Pages not found',
    'productcomments': 'Product Comments module',
    'ps_banner': 'Banner module',
    'ps_buybuttonlite': 'Buy button lite module',
    'ps_cashondelivery': 'Cash on delivery module',
    'ps_categoryproducts': 'Products in the same category module',
    'ps_categorytree': 'Category tree links module',
    'ps_checkpayment': 'Check payment module',
    'ps_contactinfo': 'Contact informations module',
    'ps_crossselling': 'Cross-selling module',
    'ps_currencyselector': 'Currency selector',
    'ps_customeraccountlinks': 'Customer account links module',
    'ps_customersignin': 'Customer "Sign in" link module',
    'ps_customtext': 'Custom text module',
    'ps_dataprivacy': 'Customer data privacy block module',
    'ps_faviconnotificationbo': 'Order Notifications on the Favicon module',
    'ps_emailalerts': 'Email Alerts module',
    'ps_emailsubscription': 'Email subscription module',
    'ps_facetedsearch': 'Faceted search module',
    'ps_featuredproducts': 'Featured products module',
    'ps_googleanalytics': 'Google Analytics module',
    'ps_imageslider': 'Image slider module',
    'ps_legalcompliance': 'Legal Compliance',
    'ps_languageselector': 'Language selector module',
    'ps_linklist': 'Links list module',
    'ps_livetranslation': 'Live translation module',
    'ps_mainmenu': 'Main menu module',
    'ps_newproducts': 'New Products module',
    'ps_productinfo': 'Product tooltips module',
    'ps_reminder': 'Reminder module',
    'ps_searchbar': 'Search Bar module',
    'ps_searchbarjqauto': 'Search bar autocomplete module',
    'ps_sharebuttons': 'Share Buttons module',
    'ps_shoppingcart': 'Shopping cart module',
    'ps_socialfollow': 'Social Follow module',
    'ps_themecusto': 'Theme customization module',
    'ps_wirepayment': 'Wire payment module',
    'pscleaner': 'PrestaShop Cleaner module',
    'psgdpr': 'GDPR module',
    'sekeywords': 'Search engine keywords statistics module',
    'statsbestcategories': 'Best categories statistics module',
    'statsbestcustomers': 'Best customers statistics module',
    'statsbestmanufacturers': 'Best manufacturers statistics module',
    'statsbestproducts': 'Best-selling products statistics module',
    'statsbestsuppliers': 'Best suppliers statistics module',
    'statsbestvouchers': 'Best vouchers statistics module',
    'statscarrier': 'Carrier distribution statistics module',
    'statscatalog': 'Catalog statistics module',
    'statscheckup': 'Catalog evaluation statistics module',
    'statsdata': 'Data mining for statistics module',
    'statsequipment': 'Browsers and operating systems statistics module',
    'statsforecast': 'Stats Dashboard module',
    'statslive': 'Visitors online statistics module',
    'statsnewsletter': 'Newsletter statistics module',
    'statsorigin': 'Visitors origin statistics module',
    'statspersonalinfos': 'Registered customer information statistics module',
    'statsproduct': 'Product details statistics module',
    'statsregistrations': 'Registrations statistics modules',
    'statssales': 'Sales and orders statistics module',
    'statssearch': 'Shop search statistics module',
    'statsstock': 'Available quantities statistics module',
    'statsvisits': 'Visits and Visitors statistics module',
    'vatnumber': 'European VAT number module',
    'watermark': 'Watermark module',
    'welcome': 'OnBoarding module',
    'ps_carriercomparison': 'Carriers comparison module',
    'ps_qualityassurance': 'Quality Assurance module',
    'ps_brandlist': 'Brands list module',
    'ps_advertising': 'Advertising module',
    # misc
    'ADR': 'Architecture Decision Records repository',
    'classic-rocket': 'Classic-rocket theme',
    'prestashop-specs': 'PrestaShop Specifications',
    'prestonbot': 'PrestonBot',
    'traces': 'Traces',
    'TopContributors': 'PrestaShop contributors website',
    'open-source': 'The PrestaShop open source project',
    'test-scenarios': 'PrestaShop test scenarios',
    'php-ps-info': 'PrestaShop PHP Informations Tool',
    'user-documentation-landing': 'User documentation landing page',
    'phpstan-prestashop': 'PrestaShop PHPStan extension',
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

CATEGORIES_REJECT_LIST = ['ME', 'PM']

CORE_BRANCHES = (
    'develop',
    '1.7.7.x',
    '1.7.6.x',
    '1.7.5.x',
    '1.7.4.x'
)

BOT_USERS = (
    'dependabot[bot]',
)
