import pygal
from pygal.style import RedBlueStyle

# World map with few countries with specified value

# create a world map
worldmap = pygal.maps.world.World()

# set the title of map
worldmap.title = 'Minimum deaths by capital punishment (source: Amnesty International)'

# adding counties with data
worldmap.add('In 2012', {
    'af': 14,
    'bd': 1,
    'by': 3,
    'cn': 1000,
    'gm': 9,
    'in': 1,
    'ir': 314,
    'iq': 129,
    'jp': 7,
    'kp': 6,
    'pk': 1,
    'ps': 6,
    'sa': 79,
    'so': 6,
    'sd': 5,
    'tw': 6,
    'ae': 1,
    'us': 43,
    'ye': 28})

# save into the file
worldmap.render_to_file('world_deaths.svg')

print("Success")


# World map of continents

# create a world map
worldmap1 = pygal.maps.world.SupranationalWorld()

# set the title of map
worldmap1.title = 'Continents'

# adding the continents
worldmap1.add('Africa', [('africa')])
worldmap1.add('North america', [('north_america')])
worldmap1.add('Oceania', [('oceania')])
worldmap1.add('South america', [('south_america')])
worldmap1.add('Asia', [('asia')])
worldmap1.add('Europe', [('europe')])
worldmap1.add('Antartica', [('antartica')])

# save into the file
worldmap1.render_to_file('world_continents.svg')

print("Success")


# World map of continents and countries

# create a world map,
# Style class is used for using the custom colors in the map,
worldmap2 = pygal.maps.world.World(fill=True, style=RedBlueStyle)

# set the title of the map
worldmap2.title = 'Continents and Countries'

# adding the continents and countries

worldmap2.add('Antartica', [('aq')])
worldmap2.add('Asia', ['bd', 'cn', 'af', 'am', 'az', 'bh', 'db', 'bt', 'bn',
                       'kh', 'tw', 'tl', 'ge', 'in', 'id', 'iq', 'ir', 'il',
                       'jp', 'jo', 'kz', 'kw', 'kg', 'lb', 'la', 'my', 'mv',
                       'mn', 'mm', 'np', 'kp', 'kr', 'om', 'pk', 'ps', 'ph',
                       'ru', 'sa', 'sg', 'lk', 'sy', 'tj', 'tr', 'tm', 'uz',
                       'vn', 'ye', 'ae', 'th'])
worldmap2.add('Europe', ['al', 'ad', 'at', 'by', 'ba', 'bg', 'hr', 'cy', 'cz',
                         'dk', 'ee', 'fi', 'fr', 'ge', 'gr', 'de', 'hu', 'is',
                         'ie', 'it', 'rs', 'lv', 'li', 'lt', 'lu', 'mk', 'md',
                         'mt', 'mc', 'me', 'nl', 'no', 'pl', 'pt', 'ro', 'sm',
                         'rs', 'si', 'sk', 'es', 'se', 'ch', 'ua', 'gb', 'va'])
worldmap2.add('Africa', ['ng', 'dz', 'ao', 'bj', 'bw', 'bf', 'bi', 'cm', 'cv',
                         'cf', 'td', 'cd', 'cg', 'ci', 'dj', 'gq', 'eg', 'er',
                         'et', 'ga', 'gm', 'gh', 'gn', 'gw', 'ke', 'lr', 'ls',
                         'ly', 'mg', 'ml', 'mw', 'mr', 'mu', 'ma', 'mz', 'na',
                         'ne', 're', 'rw', 'st', 'sn', 'sc', 'sl', 'so', 'za',
                         'sd', 'sz', 'tz', 'tg', 'tn', 'ug', 'eh', 'zm', 'zw'])
worldmap2.add('North america', ['ca', 'mx', 'us', 'pr', 'do', 'cu', 'gl', 'ht',
                                'bz', 'cr', 'sv', 'gt', 'hn', 'ni', 'pa', 'jm',
                                'do'])
worldmap2.add('South america', ['br', 'ar', 'bo', 'cl', 'co', 'ec', 'gf', 'gy',
                                'py', 'pe', 'sr', 'uy', 've'])
worldmap2.add('Oceania', ['au', 'nz', 'ca', 'ca', 'ca',
                          'ca', 'ca', 'ca', 'ca', 'pg', 'gu'])


# save into the file
worldmap2.render_to_file('world_continents_countries.svg')

print("Success")
