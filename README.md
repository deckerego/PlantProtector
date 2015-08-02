PlantProtector
==============

A plant soil & light exposure detector with a WebUI using the Adafruit Trinket

Hardware Punch List
-------------------

<table>
  <tr>
    <td>Adafruit Trinket 3.3v</td>
    <td>http://www.adafruit.com/products/1500</td>
  </tr>
  <tr>
    <td>Mini Breadboard</td>
    <td>http://www.adafruit.com/products/65</td>
  </tr>
  <tr>
    <td>Steel/Nickel Nails</td>
  </tr>
  <tr>
    <td>4.7k Ohm Resistor, 3.3k Ohm Resistor, 100 Ohm Resistor, Jumper Wires</td>
    <td>Available at Sparkfun, Adafruit, Radio Shack or from de-soldering unused electronics.</td>
  </tr>
</table>


Hardware Installation
---------------------

See https://hackaday.io/project/7037-plant-protector for hardware installation. A Fritzing layout is also provided with the project to illustrate component layouts.


Software Installation
---------------------

1. sudo apt-get install python-distribute python-dev
2. sudo easy_install pip
3. Clone this repository or download the .ZIP, which will include the Bottle webapp
4. Install PlantProtector's dependencies using pip install -r sensor-ui/requirements.txt
5. Start up the HTTP server using `./run_server.py`
