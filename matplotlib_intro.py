
"""

    Las instalaciones de macOS vienen precargadas con la versión Python 2.x
    sin embargo para desarrollo se recomienda utilizar 'brew' para actualizar a la versión 3.x
    Homebrew es un gestor de paquetes popular para macOS, para instalarlo:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install python
    ~ tuve un problema con unos links, tuve que crear una carpeta con permisos por mi cuenta y reinstalar
    /usr/local/Frameworks/Python.framework/Versions

    Los enlaces hacia los binarios de Python 3.x se deben de colocar en el PATH
    export PATH=/usr/local/opt/python/libexec/bin:$PATH

    Para instalar paquetes en Python una opción es utilizar 'pip' (package manager)
    Con dicha herramienta es posible gestionar paquetes fácilmente p.e. matploblib ...
    p.e. en este caso para disponer del paquete que deseamos hay que ejecutar la sentencia:

    pip install matploblib

"""

pop = [31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.392226, 8.078314, 9.119152, 4.552198, 1.639131, 190.010647, 7.322858, 14.326203, 8.390505, 14.131858, 17.696293, 33.390141, 4.369038, 10.238807, 16.284741, 1318.683096, 44.22755, 0.71096, 64.606759, 3.80061, 4.133884, 18.013409, 4.493312, 11.416987, 10.228744, 5.46812, 0.496374, 9.319622, 13.75568, 80.264543, 6.939688, 0.551201, 4.906585, 76.511887, 5.23846, 61.083916, 1.454867, 1.688359, 82.400996, 22.873338, 10.70629, 12.572928, 9.947814, 1.472041, 8.502814, 7.483763, 6.980412, 9.956108, 0.301931, 1110.396331, 223.547, 69.45357, 27.499638, 4.109086, 6.426679, 58.147733, 2.780132, 127.467972, 6.053193, 35.610177, 23.301725, 49.04479, 2.505559, 3.921278, 2.012649, 3.193942, 6.036914, 19.167654, 13.327079, 24.821286, 12.031795, 3.270065, 1.250882, 108.700891, 2.874127, 0.684736, 33.757175, 19.951656, 47.76198, 2.05508, 28.90179, 16.570613, 4.115771, 5.675356, 12.894865, 135.031164, 4.627926, 3.204897, 169.270617, 3.242173, 6.667147, 28.674757, 91.077287, 38.518241, 10.642836, 3.942491, 0.798094, 22.276056, 8.860588, 0.199579, 27.601038, 12.267493, 10.150265, 6.144562, 4.553009, 5.447502, 2.009245, 9.118773, 43.997828, 40.448191, 20.378239, 42.292929, 1.133066, 9.031088, 7.554661, 19.314747, 23.174294, 38.13964, 65.068149, 5.701579, 1.056608, 10.276158, 71.158647, 29.170398, 60.776238, 301.139947, 3.447496, 26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143]

gdp_cap = [974.5803384, 5937.029525999998, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995, 36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885, 4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.222719999998, 8948.102923, 22833.30851, 35278.41874, 2082.4815670000007, 6025.3747520000015, 6873.262326000001, 5581.180998, 5728.353514, 12154.08975, 641.3695236000002, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442, 1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.2317429999998, 1201.637154, 3548.3308460000007, 39724.97867, 18008.94444, 36180.78919, 2452.210407, 3540.651564, 11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.8802620000015, 31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.139730000006, 47306.98978, 10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 12451.6558, 1042.581557, 1803.151496, 10956.99112, 11977.57496, 3095.7722710000007, 9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778, 36797.93332, 25185.00911, 2749.320965, 619.6768923999998, 2013.977305, 49357.19017, 22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016, 15389.924680000002, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639000002, 1598.435089, 21654.83194, 1712.472136, 9786.534714, 862.5407561000002, 47143.17964, 18678.31435, 25768.25759, 926.1410683, 9269.657808, 28821.0637, 3970.095407, 2602.394995, 4513.480643, 33859.74835, 37506.41907, 4184.548089, 28718.27684, 1107.482182, 7458.396326999998, 882.9699437999999, 18008.50924, 7092.923025, 8458.276384, 1056.380121, 33203.26128, 42951.65309, 10611.46299, 11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]

life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000002, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.38800000000001, 60.916, 70.19800000000001, 82.208, 73.33800000000002, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000002, 71.993, 42.592, 45.678, 73.952, 59.44300000000001, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.90600000000001, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999998, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000002, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.56800000000001, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000002, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]

col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']


"""

    Entre las gráficas manejadas en matplotlib se encuentran:

    plot - útil cuando se tiene una escala de tiempo en el eje horizontal
    scatter - existe una correlación entre las dos variables gráficadas
    hist - mostrar como está distribuida la información (histograma)

"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


# PLOT LINE
"""
d = [11,12,13,14,15,16,17]
t0 = [15.3,15.4,12.6,12.7,13.2,12.3,11.4]
t1 = [26.1,26.2,24.3,25.1,26.7,27.8,26.9]
t2 = [22.3,20.6,19.8,21.6,21.3,19.4,21.4]

plt.plot(d,t1,label='México DF', linewidth=3.5, color='orange', linestyle='-.')
plt.plot(d,t0,label='New York')
plt.plot(d,t2,label='Tokyo')

plt.title("Daily temperature of 3 cities in December", size=12, fontweight='bold')
plt.grid(True,linewidth=0.5,color='#aaaaaa',linestyle='-')
plt.xlabel('Date',size=10,fontweight='semibold')
plt.ylabel('Temperature (°C)',size=10,fontweight='semibold')
plt.xlim(11,15)
plt.ylim(0,30)
plt.legend()
# Si no se indica extensión se guardará como PNG
plt.savefig('Temperature.pdf', dpi=300)
"""


# SCATTER
"""
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xscale('log')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.grid(True)
"""


# HISTOGRAM
"""
np.random.seed(19680801)

mu = 100
sigma = 15
x = mu + sigma * np.random.randn(437)
num_bins = 50

fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))

ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
"""


# TRENDLINE OVER SCATTER
"""
np.random.seed(100)
x = np.arange(10)
y = (x * x) + (np.random.rand(10) * 17) - 3.5

# Polyfit permite hacer el ajuste necesario al grado indicado ...
fit = np.polyfit(x, y, 2)

yfit = [(n * n) * fit[0] + n * fit[1] for n in x] + fit[2]
plt.scatter(x,y)
plt.plot(yfit,'red')
"""


# DASH PATTERNS - SPINES
"""
y = [np.sin(i) for i in np.arange(0.0, 10.0, 0.1)]
dash_capstyles = ['-','--','-.','.',':']
for i,x in enumerate(dash_capstyles) :
    plt.plot([n*(i+1) for n in y],x,label=x)
plt.legend(fontsize=16,loc='lower left')

ax = plt.gca()

ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_color('darkblue')
ax.spines['bottom'].set_color('darkblue')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
"""


# BAR PLOT
"""
cc_labels = ['BTC','XRP','ETH','BCH','ADA']
cap_values = [282034,131378,107393,49999,26137]

plt.bar(cc_labels, cap_values, color='orange', width=0.85)
plt.title('Market capitalization of five top cryptocurrencies in Jan 2018')
plt.xlabel('Crytocurrency')
plt.ylabel('Market capitalization (million USD)')
"""


# PIE CHART
"""
plt.figure(figsize=(4,4))
x = [0.31,0.3,0.14,0.1,0.15]
labels = ['nginx','Apache','IIS','Varnish','Others']
plt.pie(x,labels=labels, autopct='%1.1f%%', explode=[0.1] * 5)
plt.title('Web Server Usage Statistics')
# Las coordenadas aparecen al mover el mouse sobre la gráfica ...
plt.text(0.76,-1,'Dionisos!',fontsize = 10)
"""


# POLAR CHART
"""
theta = np.arange(0., 2., 1./180.) * np.pi
plt.polar(3 * theta, theta/6)
plt.polar(theta, np.cos(6 * theta))
plt.polar(theta, [1.2] * len(theta))
"""


plt.show()

"""
PENDIENTE
Matplotlib for Python Developers
> Initiating a figure with plt.figure()
"""
